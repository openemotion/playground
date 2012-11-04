import sqlite3
from flask import Flask, render_template, request, g

app = Flask(__name__)
app.config.from_object("config")

@app.route("/")
def main():
    messages = g.db.get_messages()
    return render_template("chat.html", messages=messages)

@app.route("/history")
def history():
    messages = g.db.get_messages()
    return render_template("messages.html", messages=messages)

@app.route("/message", methods=["POST"])
def message():
    g.db.store_message(request.form["author"], request.form["text"])
    return ""

@app.before_request
def before_request():
    g.db = Database(app.config["DATABASE"])

@app.teardown_request
def teardown_request(exception):
    g.db.close()

class Database(object):
    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)

    def get_messages(self):
        cmd = "select author, text from messages"
        cur = self.connection.execute(cmd)
        for row in cur:
            yield dict(author=row[0], text=row[1])

    def store_message(self, author, text):
        self.connection.execute("insert into messages (author, text) values (?, ?)", [author, text])
        self.connection.commit()

    def close(self):
        self.connection.close()

if __name__ == '__main__':
    app.debug = True
    app.run()