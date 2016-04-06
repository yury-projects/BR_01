from _curses import flash

from flask import Blueprint, render_template, abort, redirect, request
from jinja2 import TemplateNotFound

from app.forms.organization import OrganizationCreateForm
from app.models.organization import Organization
from database import db_session

organization_blueprint = Blueprint("organization", __name__, template_folder="../templates")


@organization_blueprint.route("/create", methods=["POST", "GET"])
def organization_create():

    org_create_form = OrganizationCreateForm(request.form)

    if request.method == "POST" and org_create_form.validate():
        org = Organization(name=org_create_form.name.data)
        db_session.add(org)
        db_session.commit()

        return redirect("/organization/list")

    return render_template("organization/organization_create.html", form=org_create_form)


@organization_blueprint.route("/list", methods=["GET"])
def organization_list():

    organizations = Organization.query.all()

    return render_template("organization/organization_list.html", organizations=organizations)
