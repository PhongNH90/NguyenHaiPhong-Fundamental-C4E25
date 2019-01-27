from flask import Flask, render_template

app = Flask(__name__)

users = {
    "phong": {
        "name": "Phong",
        "age": 29
    },
    "hieu": {
        "name": "Hieu",
        "age": 20
    }
}


@app.route("/user/<username>")
def user_check(username):
    if username in users:
        return render_template("user.html", username=users[username])
    else:
        return "User not Found"



if __name__ == '__main__':
  app.run(debug=True)