// Chart.js helpers - exposes functions to create/update charts
let tempChartObj = null;
let humChartObj = null;

function createChart(ctx, labels, data, label){
  return new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: label,
        data: data,
        fill: false,
        tension: 0.2
      }]
    },
    options: {
      responsive: true,
      scales: {
        x: { display: true },
        y: { display: true }
      }
    }
  });
}

window.createOrUpdateTempChart = function(labels, data){
  const ctx = document.getElementById('tempChart').getContext('2d');
  if(tempChartObj) { tempChartObj.data.labels = labels; tempChartObj.data.datasets[0].data = data; tempChartObj.update(); }
  else tempChartObj = createChart(ctx, labels, data, 'Daily Temperature (°C)');
}

window.createOrUpdateHumChart = function(labels, data){
  const ctx = document.getElementById('humChart').getContext('2d');
  if(humChartObj) { humChartObj.data.labels = labels; humChartObj.data.datasets[0].data = data; humChartObj.update(); }
  else humChartObj = createChart(ctx, labels, data, 'Daily Humidity (%)');
}