from flask import Flask, render_template, request

from datetime import datetime, date, timedelta

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def results():

    today_date = datetime.today()

    #avoid empty date submission
    try:
        selected_date = datetime.strptime(request.form.get("item"), '%Y-%m-%d')
    except ValueError:
        return render_template("error.html", message = "Please enter a date.")

    #error checking for dates:
    if selected_date > today_date:
        return render_template("error.html", message = "You have entered a date beyond today. Please select a date before today.")

    #"calculation" of dates
    menstruation = (selected_date + timedelta(7)).date()

    follicular = (selected_date + timedelta(14)).date()

    ovulation = (follicular + timedelta(2))

    luteal = (ovulation + timedelta(14))

    #convert today_date datetime object to date object
    today_date = today_date.date()

    if today_date < menstruation or today_date == menstruation:
        return render_template("menstruation.html", phase = "menstruation", today_date=today_date)

    elif today_date < follicular or today_date == follicular:
        return render_template("follicular.html", phase = "follicular phase", today_date=today_date)

    elif today_date < ovulation or today_date == ovulation:
        return render_template("ovulation.html", phase = "ovulation phase", today_date=today_date)

    elif today_date < luteal or today_date == luteal:
        return render_template("luteal.html", phase = "luteal phase", today_date=today_date)

    return render_template("err.html")