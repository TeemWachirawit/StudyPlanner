import sqlite3

def get_db_connection():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
conn.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    deadline TEXT NOT NULL
)
""")
conn.commit()
conn.close()

from flask import Flask, render_template, request, redirect, url_for

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

@app.route("/", methods=["GET", "POST"])
def home():
    conn = get_db_connection()

    if request.method == "POST":
        title = request.form["title"]
        deadline = request.form["deadline"]

        conn.execute(
            "INSERT INTO tasks (title, deadline) VALUES (?, ?)",
            (title, deadline)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()

    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>", methods=["POST"])
def delete_task(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run()