#FLASK

from flask import Flask

app = Flask(__name__)

@app.route("/")     # nếu người dùng vào trang chủ
def homepage():     # binding: thì gọi hàm homepage này ra          #hàm mà được đính với route gọi là #view function
    return "Hello world, this is flask homepage"




if __name__ == "__main__":
    app.run(debug=True)  # nếu gõ debug vô thì tắt Auto Save đi