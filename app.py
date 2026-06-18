from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    result = a + b

    return render_template("index.html", a=a, b=b, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)