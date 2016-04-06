import time

from flask import Blueprint, render_template, request, redirect, flash

from app.forms.user import UserCreateForm
from app.models import User, Organization
from database import db_session

user_blueprint = Blueprint("user", __name__, template_folder="../templates")


@user_blueprint.route("/create", methods=["POST", "GET"])
def user_create():

    user_create_form = UserCreateForm(request.form)

    user_create_form.org_id.choices = [(org.id, org.name) for org in Organization.query.order_by("name")]

    if request.method == "POST" and user_create_form and user_create_form.validate():
        salt = time.time()
        # TODO: Better algorithm for passwords
        user = User(email=user_create_form.email.data,
                    password=user_create_form.password.data + "+" + str(salt),
                    salt=salt,
                    first_name=user_create_form.first_name.data,
                    last_name=user_create_form.last_name.data,
                    org_id=user_create_form.org_id.data,
                    role=user_create_form.role.data)

        db_session.add(user)
        db_session.commit()

        flash("Thanks for registering")

        return redirect("/user/list")

    return render_template("user/user_create.html",
                           form=user_create_form)


@user_blueprint.route("/list", methods=["GET"])
def user_list():

    users = User.query.all()

    return render_template("user/user_list.html", users=users)
