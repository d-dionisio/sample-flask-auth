from flask import Flask
from database import db
from models.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Responsável por criar minha conexão com o banco de dados
db.init_app(app)
# Session <- conexão ativa

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)