from geopy.geocoders import Nominatim

# NOTE: geopy is not in requirements. This file is optional and not used by default.
# If you want to use server-side geocoding, add `geopy` to requirements and enable this.


def get_coords_for_city(city_name):
    g = Nominatim(user_agent='weather_app')
    loc = g.geocode(city_name)
    if not loc:
        raise ValueError('Could not geocode city: ' + city_name)
    return loc.latitude, loc.longitude