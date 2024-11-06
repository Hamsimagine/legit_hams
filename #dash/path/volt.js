   // Data yang diberikan
    var data = {
      labels: ["8.00", "8.01", "8.02", "8.03", "8.04", "8.05", "8.06"],
      datasets: [
        {
          label: "Voltase 1 (V)",
          borderColor: 'rgb(255, 193, 7)',
          data: [221, 220, 220, 224, 222, 228, 226 ],
        },
        {
          label: "Voltase 2 (V)",
          borderColor: 'rgb(75, 192, 192)',
          data: [230, 229, 229, 231, 230, 232, 230],
        },
        {
          label: "Voltase 3 (V)",
          borderColor: 'rgb(255, 99, 132)',
          data: [230, 228, 232, 237, 240, 240, 239, 238],
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