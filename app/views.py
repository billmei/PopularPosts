from flask import render_template, send_from_directory
from flask import url_for, redirect, request
from app import app

# Templates
@app.route('/')
def render_index_page():
    return render_template('index.html')

