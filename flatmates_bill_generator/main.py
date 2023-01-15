import datetime
import math
import re

from flask import Flask, render_template, request, flash, url_for, redirect, session


app = Flask(__name__)
app.secret_key = "flatmate_application"
error = None
confirmation = None


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
