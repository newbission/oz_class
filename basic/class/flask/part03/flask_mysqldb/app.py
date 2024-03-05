from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask_smorest import Api
from user_route import create_user_blueprint


app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "oz"

mysql = MySQL(app)

app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

user_blp = create_user_blueprint(mysql)
api = Api(app)
api.register_blueprint(user_blp)


@app.route("/users_interface")
def users_interface():
    return render_template("users.html")

if __name__ == "__main__":
    app.run(debug=True)
