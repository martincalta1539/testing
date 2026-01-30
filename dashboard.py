from flask import Flask, jsonify
import psutil
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>MartiMiner OS</title>
            <meta http-equiv="refresh" content="5">
            <style>
                body { background: #0f0f0f; color: #00ff00; font-family: monospace; padding: 50px; }
                .stat { font-size: 24px; border: 1px solid #00ff00; padding: 20px; display: inline-block; }
            </style>
        </head>
        <body>
            <h1>MartiMiner OS - Local Node</h1>
            <div class="stat">
                <p>Teplota CPU: <span id="temp">Načítání...</span></p>
                <p>Vytížení: <span id="load">Načítání...</span> %</p>
            </div>
            <script>
                fetch('/api/stats').then(r => r.json()).then(data => {
                    document.getElementById('temp').innerText = data.temp + " °C";
                    document.getElementById('load').innerText = data.load;
                });
            </script>
        </body>
    </html>
    """

@app.route('/api/stats')
def stats():
    temps = psutil.sensors_temperatures()
    cpu_temp = temps['coretemp'][0].current if 'coretemp' in temps else "N/A"
    return jsonify(temp=cpu_temp, load=psutil.cpu_percent())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)