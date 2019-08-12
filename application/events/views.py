from application import app, db
from flask import render_template, request, url_for, redirect
from flask_login import login_required
from application.events.models import Event
from application.events.forms import EventForm, ModifyForm

@app.route("/events/", methods=["GET"])
def events_index():
    return render_template("events/list.html", events = Event.query.all())


@app.route("/events/new/")
@login_required
def events_form():
    return render_template("events/new.html", form = EventForm())

@app.route("/events/delete/<event_id>", methods=["POST"])
@login_required
def events_delete(event_id):
    e = Event.query.get(event_id)
    db.session.delete(e)
    db.session.commit()
    return redirect(url_for("events_index"))


@app.route("/events/<event_id>/", methods=["POST"])
@login_required
def events_set_cancelled(event_id):
    name = request.form.get("name")
    desc = request.form.get("description")
    

    e = Event.query.get(event_id)
    if name:
        e.name = name
    elif desc:
        e.description = desc
    else:
        e.cancelled = False if e.cancelled else True
    
    db.session.commit()

    return render_template("events/one.html", event = e, form = ModifyForm())

@app.route("/events/<event_id>/", methods=["GET"])
def event_view_by_id(event_id):
    e = Event.query.get(event_id)

    return render_template("events/one.html", event = e, form = ModifyForm())

@app.route("/events/", methods=["POST"])
@login_required
def events_create():
    print(request.form.get("name"))
    print(request.form.get("description"))
    form = EventForm(request.form)

    if not form.validate():
        return render_template("events/new.html", form = form)

    e = Event(request.form.get("name"), request.form.get("description"))
        
    db.session().add(e)
    db.session().commit()

    return redirect(url_for("events_index"))

@app.route("/events/modify/<event_id>", methods=["POST"])
@login_required
def events_modify(event_id):
    
    return render_template("events/one.html", event = e)
