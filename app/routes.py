# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Volcano, State_volcano
from app.forms import VolcanoForm, StateVolcanoForm


@app.route('/')
@app.route('/index')
def index():
    volcanoes = Volcano.query.all()
    state_volcanoes = State_volcano.query.all()

    return render_template('index.html', volcanoes=volcanoes, state_volcanoes=state_volcanoes)


@app.route('/volcano', methods=['GET', 'POST'])
def volcano():
    volcanoes = Volcano.query.all()

    form = VolcanoForm()
    if form.validate_on_submit():
        v = Volcano(form.namev.data,
                    form.latitude.data,
                    form.longitude.data,
                    form.height.data)
        db.session.add(v)
        db.session.commit()
        return redirect(url_for('volcano'))
    return render_template('volcano.html', form=form, volcanoes=volcanoes)


@app.route('/state_volcanoes', methods=['GET', 'POST'])
def state_volcanoes():
    stvs = State_volcano.query.all()
    volcanoes = Volcano.query.all()

    form = StateVolcanoForm()
    if form.validate_on_submit():
        print('oy yea')
        for volcano in volcanoes:
            if (volcano.namev == form.namev.data):
                st = State_volcano(form.namev.data,
                                   form.date_state.data,
                                   form.thermal_anomaly.data,
                                   form.number_events.data,
                                   form.max_pgd_height.data,
                                   form.observ_ash_emissions.data,
                                   form.hazard_code.data)
                db.session.add(st)
                db.session.commit()
                return redirect(url_for('state_volcanoes'))
                break

    return render_template('state_volcanoes.html', form=form, state_volcanoes=stvs)


@app.route('/st')
def st():
    stvs = State_volcano.query.all()
    return render_template('st.html', state_volcanoes=stvs)


@app.route('/state_volcano/<namev>', methods=['GET', 'POST'])
def state_volcano(namev):
    stvs = State_volcano.query.filter_by(namev=namev)
    return render_template('state_volcano.html', state_volcanoes=stvs, namev=namev)