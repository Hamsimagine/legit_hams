var data = {
  labels: ["8.00", "8.01", "8.02", "8.03", "8.04", "8.05", "8.06"],
  datasets: [
      {
          label: "Daya 1 (A)",
          borderColor: 'rgb(255, 193, 7)',
          data: [12, 15, 8, 13, 14, 16, 16],
      },
      {
          label: "Daya 2 (A)",
          borderColor: 'rgb(75, 192, 192)',
          data: [16, 10, 7, 12, 11, 9, 10, 11],
      },
      {
          label: "Daya 3 (A)",
          borderColor: 'rgb(255, 99, 132)',
          data: [15, 16, 7, 5, 6, 7, 6, 5, 7],
      }
  ]
};

var options = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
      y: {
          beginAtZero: true
      }
  }
};

var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'line',
  data: data,
  options: options
});

function exportToExcel() {
  console.log('Exporting to Excel...');
  var wb = XLSX.utils.book_new();
  var ws = XLSX.utils.json_to_sheet(data.datasets[0].data.map((value, index) => ({
      label: data.labels[index],
      "Daya 1 (A)": value,
      "Daya 2 (A)": data.datasets[1].data[index],
      "Daya 3 (A)": data.datasets[2].data[index]
  })));

  XLSX.utils.book_append_sheet(wb, ws, "Sheet1");
  XLSX.writeFile(wb, "chart_data.xlsx");
}