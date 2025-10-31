from datetime import datetime

def format_current_and_forecast(current, forecast):
    # current
    cur = {
        'city': current.get('name', 'Unknown'),
        'temp': round(current.get('main', {}).get('temp', 0), 1),
        'description': (current.get('weather') or [{}])[0].get('description', '').capitalize(),
        'humidity': current.get('main', {}).get('humidity', None),
        'wind': current.get('wind', {}).get('speed', None)
    }

    # forecast: aggregate forecast['list'] (3-hour intervals) into daily averages
    # We will use the date string in dt_txt to group by YYYY-MM-DD
    daily = {}
    for item in forecast.get('list', []):
        dt_txt = item.get('dt_txt')  # format "2025-11-01 12:00:00"
        if not dt_txt:
            continue
        date_key = dt_txt.split(' ')[0]  # YYYY-MM-DD
        temps = daily.setdefault(date_key + '_temps', [])
        hums = daily.setdefault(date_key + '_hums', [])
        temps.append(item.get('main', {}).get('temp'))
        hums.append(item.get('main', {}).get('humidity'))

    # build list preserving chronological order
    dates = sorted({k.split('_')[0] for k in daily.keys()})
    forecast_list = []
    count = 0
    for d in dates:
        if count >= 7:
            break
        temps = daily.get(d + '_temps', [])
        hums = daily.get(d + '_hums', [])
        if not temps:
            continue
        avg_temp = round(sum(temps) / len(temps), 1)
        avg_hum = int(sum(hums) / len(hums)) if hums else None
        # convert YYYY-MM-DD to weekday short name
        try:
            dt = datetime.strptime(d, "%Y-%m-%d")
            weekday = dt.strftime('%a')  # Mon, Tue...
        except Exception:
            weekday = d
        forecast_list.append({'date': weekday, 'temp': avg_temp, 'humidity': avg_hum})
        count += 1

    # If forecast_list is empty (unexpected), try fallback: take first 5 list items
    if not forecast_list and forecast.get('list'):
        temp_list = []
        for i, item in enumerate(forecast['list']):
            if i >= 7:
                break
            dt_txt = item.get('dt_txt', '')
            try:
                dt = datetime.strptime(dt_txt.split(' ')[0], "%Y-%m-%d")
                weekday = dt.strftime('%a')
            except Exception:
                weekday = dt_txt
            temp = item.get('main', {}).get('temp')
            hum = item.get('main', {}).get('humidity')
            forecast_list.append({'date': weekday, 'temp': round(temp,1) if temp is not None else None, 'humidity': hum})

    return {'current': cur, 'forecast': forecast_list}
