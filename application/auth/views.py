from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user 
from sqlalchemy.exc import IntegrityError

from application import app, db, login_required
from application.auth.models import User, Role
from application.auth.forms import LoginForm
from application.auth.forms import UserForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Virheellinen käyttajänimi tai salasana")

    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))    

@app.route("/users/new/")
def users_form():
    return render_template("auth/userform.html", form = UserForm())

@app.route("/users/", methods=["POST"])
def users_create():
    form = UserForm(request.form)

    if not form.validate():
        return render_template("auth/userform.html", form = form)
        
    u = User(form.name.data, form.e_mail.data, form.address.data, form.username.data, 
    form.password.data)

    role = Role.query.filter_by(name=form.role.data).first()
    if not role:
        role = Role(form.role.data)
        db.session().add(role)

    u.roles.append(role)
    db.session().add(u)
    db.session().commit()
  
    return redirect(url_for("books_index"))

@app.route("/user/edit/", methods=["GET", "POST"])
@login_required()
def user_edit():
    id = request.args.get("user_id")
    user = User.query.get(id)
    form = UserForm(obj=user)
    if request.method == 'POST' and form.validate():
        role = Role.query.filter_by(name=form.role.data).first()
        if not role:
            role = Role(form.role.data)
            db.session().add(role)
        user.roles.clear()
        user.roles.append(role)
        form.populate_obj(user)
        db.session().commit()
 
        return redirect(url_for("books_index"))
    return render_template('auth/edit.html', form=form)

@app.route("/user/delete/", methods=["POST"])
@login_required()
def user_delete():
    id = request.args.get("user_id")
    user = User.query.get(id)
    db.session().delete(user)
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/users", methods=['GET'])
@login_required(role="ADMIN")
def users_index():
    users = User.query.all()
    form = UserForm(request.form)
    return render_template("auth/list.html", users=users, form=form)