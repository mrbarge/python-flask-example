from demo.models import db, Thing
from demo.thing.tables import ThingResults
from demo.thing.forms import ThingForm
from flask import Blueprint, render_template, request, url_for, redirect, flash

thing_bp = Blueprint('thing_bp', __name__)


@thing_bp.route('/')
def list():
    things_cur = Thing.query.filter().all()
    all_things = []
    for thing in things_cur:
        all_things.append({'thing': thing.thing, 'rating': thing.rating})

    table = ThingResults(all_things)
    table.classes = ['table']
    return render_template('thing/list.html', table=table)


@thing_bp.route('/add', methods=['GET', 'POST'])
def add():
    thing_form = ThingForm()

    if request.method == 'POST':
        if thing_form.validate_on_submit():
            try:
                thing = request.form['thing']
                rating = request.form['rating']

                t = Thing(thing=thing, rating=rating)
                db.session.add(t)
                db.session.commit()

                return redirect(url_for('thing_bp.list'))
            except Exception as err:
                flash(f'An error occurred whilst searching: {err}', 'error')

    return render_template('thing/add.html', form=thing_form)
