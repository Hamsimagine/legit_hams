from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Inisialisasi database SQLite
DATABASE = 'sensor_data.db'

def create_table():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          sensor_id TEXT NOT NULL,
                          sensor_value TEXT NOT NULL
                        )''')
        connection.commit()

create_table()

@app.route('/update_sensor', methods=['POST'])
def update_sensor():
    data = request.json  # Menerima data dari permintaan POST
    sensor_id = data.get('sensor_id')
    sensor_value = data.get('sensor_value')

    if sensor_id is not None and sensor_value is not None:
        # Menyimpan data sensor ke dalam database
        with sqlite3.connect(DATABASE) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO sensor_data (sensor_id, sensor_value) VALUES (?, ?)",
                           (sensor_id, sensor_value))
            connection.commit()

        return jsonify({'message': 'Data sensor berhasil diperbarui'}), 200
    else:
        return jsonify({'error': 'Format data tidak sesuai'}), 400

@app.route('/get_sensor/<sensor_id>', methods=['GET'])
def get_sensor(sensor_id):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT sensor_id, sensor_value FROM sensor_data WHERE sensor_id=?", (sensor_id,))
        result = cursor.fetchone()

        if result is not None:
            return jsonify({'sensor_id': result[0], 'sensor_value': result[1]}), 200
        else:
            return jsonify({'error': 'Sensor tidak ditemukan'}), 404

if __name__ == '__main__':
    app.run(debug=True)