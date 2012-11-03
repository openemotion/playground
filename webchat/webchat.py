from flask import Flask, render_template, request
import sqlalchemy as sql

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("chat.html")

@app.route("/message", methods=["POST"])
def message():
    text = request.form["text"]
    storage.store_message("bla", text)
    return ""

class Storage(object):
    def __init__(self):
        metadata = sql.MetaData()
        engine = sql.create_engine("sqlite:///data.db", isolation_level="SERIALIZABLE")
        self.messages = sql.Table('messages', metadata,
            sql.Column('id', sql.Integer, primary_key=True),
            sql.Column('author', sql.String),
            sql.Column('text', sql.String),
         )
        metadata.create_all(engine)
        self.connection = engine.connect()

    def get_messages(self):
        for row in self.connection.execute(self.messages.select()):
            yield dict(row)

    def store_message(self, author, text):
        self.connection.execute(self.messages.insert(), author=author, text=text)

if __name__ == '__main__':
    storage = Storage()
    app.debug = True
    app.run()