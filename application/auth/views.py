from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db
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
        error = "Invalid username or password")

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

    u = User(request.form.get("name"), request.form.get("username"), request.form.get("password"))
    
    db.session.add(u)
    db.session.commit()

    return render_template("auth/loginform.html", form = LoginForm(), error = "now, try logging in")

@app.route("/auth/<account_id>/", methods=["GET"])
@login_required
def auth_view_by_id(account_id):
    account = User.query.get(account_id)
    # number_of_events = User.find_number_of_events_associated_with_specific_account(account_id)
    own_events = User.find_events_created_by_account(account_id)
    events_of_interest = User.find_events_associated_with_specific_account(account_id)

    return render_template("auth/single.html", account = account, form = AccountForm(), number_of_events = 0, own_events = own_events, events_of_interest = events_of_interest)

@app.route("/accounts/<account_id>/", methods=["POST"])
@login_required
def auth_modify(account_id):
    name = request.form.get("name")
    username = request.form.get("username")
    password = request.form.get("password")
    account = User.query.get(account_id)
    
    #katsotaan, mitä osoitteeseen on postattu, ja muutetaan arvoa sen mukaan
    if account.id == current_user.id:
        if name:
            account.name = name
        elif username:
            account.username = username
        elif password:
            account.password = password
            
    db.session.commit()
    return redirect(url_for("auth_view_by_id", account_id = account.id))

@app.route("/auth/delete/<account_id>", methods=["POST"])
@login_required
def auth_delete(account_id):
    account = User.query.get(account_id)
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for("events_index"))
        
    