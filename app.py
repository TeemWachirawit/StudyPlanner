from flask import Flask, render_template

app = Flask(__name__)

tasks = [
    {
        "title": "Math Homework",
        "deadline": "2026-02-10"
    },
    {
        "title": "English Essay",
        "deadline": "2026-02-12"
    }
]

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

if __name__ == '__main__':
    app.run()