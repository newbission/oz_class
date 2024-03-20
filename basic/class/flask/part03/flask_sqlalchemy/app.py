from flask import Flask, render_template
from flask_smorest import Api
from db import db
from flask_migrate import Migrate

from routes.user import user_blp
from routes.board import board_blp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/oz"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

migrate = Migrate(app, db)

app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(user_blp)
api.register_blueprint(board_blp)


@app.route("/manage-boards")
def manage_boards():
    return render_template("boards.html")


@app.route("/manage-users")
def manage_users():
    return render_template("users.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
