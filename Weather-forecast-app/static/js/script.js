document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('city-form');
    const cityInput = document.getElementById('city-input');
    const locBtn = document.getElementById('loc-btn');
    const currentDiv = document.getElementById('current');
    const chartContainer = document.getElementById('chart-container');
    const ctx = document.getElementById('weatherChart').getContext('2d');
    let chart = null;

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const city = cityInput.value.trim();
        if (!city) return alert('Please enter a city.');
        fetchWeather({ city });
    });

    locBtn.addEventListener('click', () => {
        if (!navigator.geolocation) return alert('Geolocation not supported.');
        navigator.geolocation.getCurrentPosition(pos => {
            fetchWeather({ lat: pos.coords.latitude, lon: pos.coords.longitude });
        }, () => alert('Unable to get location.'));
    });

    async function fetchWeather(payload) {
        // hide UI while loading
        currentDiv.style.display = 'none';
        chartContainer.style.display = 'none';

        try {
            const res = await fetch('/weather', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const j = await res.json();
            if (j.status !== 'ok') throw new Error(j.message || 'API error');
            renderAll(j.data);
        } catch (err) {
            alert('Error: ' + (err.message || err));
            console.error(err);
        }
    }

    function renderAll(data) {
        // show current
        document.getElementById('city-name').textContent = data.current.city;
        document.getElementById('temperature').textContent = `${data.current.temp}°C`;
        document.getElementById('description').textContent = data.current.description;
        document.getElementById('humidity').textContent = `Humidity: ${data.current.humidity}%`;
        document.getElementById('wind').textContent = `Wind: ${data.current.wind} m/s`;
        currentDiv.style.display = 'block';

        // dynamic background by temp
        const temp = data.current.temp;
        let cls = '';
        if (temp <= 10) cls = 'cold';
        else if (temp <= 20) cls = 'mild';
        else if (temp <= 30) cls = 'warm';
        else cls = 'hot';
        document.body.className = cls;

        // prepare chart data
        const labels = data.forecast.map(d => d.date);
        const temps = data.forecast.map(d => d.temp);
        const hums = data.forecast.map(d => d.humidity);

        if (chart) chart.destroy();

        chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Temperature (°C)',
                        data: temps,
                        borderColor: '#007bff',
                        backgroundColor: 'rgba(0,123,255,0.15)',
                        tension: 0.3,
                        fill: true
                    },
                    {
                        label: 'Humidity (%)',
                        data: hums,
                        borderColor: '#00b894',
                        backgroundColor: 'rgba(0,184,148,0.12)',
                        tension: 0.3,
                        fill: true
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { position: 'top' }
                },
                scales: {
                    x: { ticks: { color: '#333' } },
                    y: { ticks: { color: '#333' } }
                }
            }
        });

        chartContainer.style.display = 'block';
    }

    // On load: try geolocation then fallback to default
    window.addEventListener('load', () => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(pos => {
                fetchWeather({ lat: pos.coords.latitude, lon: pos.coords.longitude });
            }, () => {
                // ask server default
                fetchWeather({});
            });
        } else {
            fetchWeather({});
        }
    });
});
