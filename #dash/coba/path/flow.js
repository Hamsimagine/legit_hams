                document.addEventListener('DOMContentLoaded', function () {
                  // Data contoh (gantilah dengan data sebenarnya)
                  var data = {
                    labels: ['08.00', '08.01', '08.02', '08.03', '08.04', '08.05', '08.06'],
                    datasets: [{
                      label: 'Flow Data',
                      backgroundColor: 'rgba(255, 99, 132, 0.2)',
                      borderColor: 'rgba(255, 99, 132, 1)',
                      borderWidth: 2,
                      data: [0.81, 0.85, 0.81, 0.9, 0.87, 0.89, 0.85],
                    }],
                  };
              
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
              
                  var ctx = document.getElementById('lineChart').getContext('2d');
                  new Chart(ctx, config);
                });