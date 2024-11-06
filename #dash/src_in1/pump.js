        document.addEventListener('DOMContentLoaded', function() {
            var gauge = new JustGage({
                id: 'gauge',
                value: 0.10,
                min: 0,
                max: 10,
                title: 'Pressure',
                label: 'psi',
                valueFontColor: '#000',
                levelColors: [ '#00FF00','#FFA500','#FF0000']
            });

            var pumpRange = document.getElementById('pumpRange');
            var onButton = document.getElementById('onButton');
            var offButton = document.getElementById('offButton');

            pumpRange.addEventListener('input', function() {
                gauge.refresh(this.value);
            });

            onButton.addEventListener('click', function() {
                // Kode untuk mengaktifkan pompa air
            });

            offButton.addEventListener('click', function() {
                // Kode untuk menonaktifkan pompa air
            });
        });