             document.addEventListener('DOMContentLoaded', function () {
                // Data diagram garis
                var data = {
                  labels: ['08.00', '08.01', '08.03', '08.04', '08.05', '08.06'],
                  datasets: [{
                    label: 'Frekuensi',
                    borderColor: 'rgb(255, 99, 132)',
                    borderWidth: 2,
                    data: [30, 42, 25, 38, 50, 48],
                  }]
                };
                
                // Opsi diagram garis
                var config = {
                    type: 'line',
                    data: data,
                    options: {
                      scales: {
                        y: {
                          beginAtZero: true,
                        },
                      },
                    },
                  };
                
                // Inisialisasi diagram garis
                var ctx = document.getElementById('linechart').getContext('2d');
                new Chart(ctx, config);
             });