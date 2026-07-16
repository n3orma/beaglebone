from flask import Flask, render_template, redirect
import os

app = Flask(__name__)

LED = "/sys/class/leds/beaglebone:green:usr0"

# Disable the default heartbeat trigger
os.system(f"echo none | sudo tee {LED}/trigger > /dev/null")

@app.route("/")
def index():
    with open(f"{LED}/brightness") as f:
        state = f.read().strip()
    return render_template("index.html", state=state)

@app.route("/on")
def on():
    os.system(f"echo 1 | sudo tee {LED}/brightness > /dev/null")
    return redirect("/")

@app.route("/off")
def off():
    os.system(f"echo 0 | sudo tee {LED}/brightness > /dev/null")
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
