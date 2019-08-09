from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from application.auth.models import User
from application.auth.forms import LoginForm, AccountForm

@app.route("/auth/login", methods =["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("/auth/loginform.html", form = LoginForm())
    
    form = LoginForm(request.form)
    
    if not form.validate():
        return render_template("auth/loginform.html", form = form)

    user = User.query.filter_by(username = form.username.data, password = form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
        error = "Invalid username or password blyat")

    print("User "+ user.name + " was recognised")
    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/new", methods = ["GET", "POST"])
def auth_create_new():
    if request.method == "GET":
        return render_template("/auth/accountform.html", form = AccountForm())

    form = AccountForm(request.form)

    if not form.validate():
        return render_template("/auth/accountform.html", form = form)

    #if request.method == "POST"
    
    return redirect(url_for("index"))
        
    