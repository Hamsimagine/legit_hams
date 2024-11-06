           // Data yang diberikan
           var data = {
            labels: ["8.00", "8.01", "8.02", "8.03", "8.04", "8.05", "8.06"],
      datasets: [
        {
          label: "Daya 1 (A)",
          borderColor: 'rgb(255, 193, 7)',
          data: [12,15,8,13,14,16,16],
        },
        {
          label: "Daya 2 (A)",
          borderColor: 'rgb(75, 192, 192)',
          data: [16,10,7,12,11,9,10,11],
        },
        {
          label: "Daya 3 (A)",
          borderColor: 'rgb(255, 99, 132)',
          data: [15,16,7,5,6,7,6,5,7],
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
      }
    };
  
    // Mendapatkan elemen canvas dan menggambar chart
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
      type: 'line',
      data: data,
      options: options
    });