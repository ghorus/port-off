import os
from flask import render_template, url_for, flash, redirect
from new_port import app


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/aboutme")
def aboutme():
    return render_template('aboutme.html')

@app.route("/socialmedia")
def socialmedia():
    return render_template('socialmedia.html')

@app.route("/process")
def process():
    return render_template('process.html')