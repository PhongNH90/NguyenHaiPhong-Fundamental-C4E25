#CREATE FLASK APP

from flask import Flask, render_template , request
app = Flask(__name__)

@app.route('/new_bike', methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("bike_form.html")
    elif request.method == "POST":
        form = request.form
        m = form["model"]
        d = form["daily_fee"]
        i = form["image"]
        y = form["year"]
        print(m, d, i , y)
        return "OK"

if __name__ == '__main__':
  app.run(debug=True)