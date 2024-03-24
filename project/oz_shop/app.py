from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate

from routes.user import user_blp

from db import db

app = Flask(__name__)

# DB 설정
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/oz_shop"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app, db)

# OPENAPI 설정
app.config["API_TITLE"] = "OZ-SHOP API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(user_blp)



@app.route("/")
def index():
    return "This is OZ Shop!!"


if __name__ == "__main__":
    app.run(debug=True)
