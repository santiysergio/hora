from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_madrid_time():
    response = requests.get("http://worldtimeapi.org/api/timezone/Europe/Madrid")
    data = response.json()
    madrid_time = data['datetime']
    return madrid_time

@app.route('/')
def index():
    madrid_time = get_madrid_time()
    return render_template('index.html', madrid_time=madrid_time)

if __name__ == '__main__':
    app.run()
