   // Data yang diberikan
    var data = {
      labels: ["8.00", "8.01", "8.02", "8.03", "8.04", "8.05", "8.06"],
      datasets: [
        {
          label: "Voltase 1 (V)",
          borderColor: 'rgb(255, 193, 7)',
          data: [219, 218, 220, 216, 218, 219, 219 ],
        },
        {
          label: "Voltase 2 (V)",
          borderColor: 'rgb(75, 192, 192)',
          data: [216, 215, 217, 212, 214, 217, 218],
        },
        {
          label: "Voltase 3 (V)",
          borderColor: 'rgb(255, 99, 132)',
          data: [180, 211, 211, 209, 210, 216, 217, 219],
        }
      ]
    };

    // Konfigurasi chart
    var options = {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true
        }
      },
      plugins: {
        tooltip: {
          callbacks: {
            label: function (context) {
              var label = context.dataset.label || '';
              if (label) {
                label += ': ';
              }
              label += context.parsed.y + ' V';
              return label;
            },
            title: function (context) {
              return 'Waktu: ' + data.labels[context[0].dataIndex];
            }
          }
        }
      }
    };

    // Mendapatkan elemen canvas dan menggambar chart
    var ctx = document.getElementById('myChartV').getContext('2d');
    var myChartV = new Chart(ctx, {
      type: 'line',
      data: data,
      options: options
    });