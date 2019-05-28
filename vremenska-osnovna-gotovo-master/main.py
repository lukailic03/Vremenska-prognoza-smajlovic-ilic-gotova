import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/zagreb", methods=["GET"])
def zagreb():

    grad = "Zagreb"

    unit = "metric"

    apikey = "efc23cf64fab778fb4dd9966b146b607"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("zagreb.html", data=data.json())

@app.route("/rijeka", methods=["GET"])
def rijeka():

    grad = "Rijeka"

    unit = "metric"

    apikey = "efc23cf64fab778fb4dd9966b146b607"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("rijeka.html", data=data.json())

@app.route("/split", methods=["GET"])
def split():

    grad = "Split"

    unit = "metric"

    apikey = "efc23cf64fab778fb4dd9966b146b607"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("split.html", data=data.json())


if __name__ == '__main__':
    app.run()
