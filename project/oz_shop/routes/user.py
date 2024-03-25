from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import User
from schemas import UserCreateSchema

user_blp = Blueprint(
    "Users", "users", description="Operations on users", url_prefix="/users"
)


@user_blp.route("/")
class UserList(MethodView):
    @user_blp.response(200)
    def get(self):
        users = User.query.all()
        user_data = [
            {"id": user.id, "name": user.name, "password": user.email} for user in users
        ]  # Convert to list
        return jsonify(user_data)


@user_blp.route("/register")
class UserCreate(MethodView):
    @user_blp.arguments(UserCreateSchema)
    @user_blp.response(201, description="Item updated")
    def post(self):
        user_data = request.json
        new_user = User(name=user_data["name"], email=user_data["email"])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created"}), 201
