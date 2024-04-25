from flask import Flask, render_template, request
import requests

app = Flask(__name__)


KEY = "5e471357596d2ab9ec8df2d7b11c4ba8"


@app.get("/")
def Start():
    return render_template("base.html")


@app.post("/weather")
def Weather():
    city = request.form["city"]
    app = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units=metric"
    response = requests.get(app)
    data = response.json()
    weather = data["main"]
    temp = weather["temp"]
    feels = weather["feels_like"]
    humidity = weather["humidity"]
    main = data["weather"][0]["main"]
    descr = "No Information" if data["weather"][0]["description"] == 0 else data["weather"][0]["description"]

    wind = data["wind"]["speed"]
    return render_template('weather.html', city=city, temp=temp, feels=feels, descr=descr, humidity = humidity, wind = wind, main=main)





if __name__ == "__main__":
    app.run(debug=True)
