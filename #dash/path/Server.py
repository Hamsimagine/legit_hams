 
from flask import Flask, jsonify

# MQTT Configuration
BROKER_ADDRESS = "localhost"  # Ganti dengan alamat IP broker MQTT Anda jika tidak berjalan di localhost
BROKER_PORT = 1883
TOPIC = "esp32/data"

# Data storage for monitoring
data_storage = []

# Flask app for monitoring
app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_storage)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f"Message received: {msg.topic} {str(msg.payload)}")
    data_storage.append({
        "topic": msg.topic,
        "payload": str(msg.payload.decode("utf-8"))
    })

# MQTT Client setup
client = mqtt.Client(callback_api_version=5)  # Menyertakan versi API callback
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_ADDRESS, BROKER_PORT, 60)

# Start MQTT loop in a separate thread
client.loop_start()

if __name__ == "__main__":
    app.run(debug=True, port=5000)