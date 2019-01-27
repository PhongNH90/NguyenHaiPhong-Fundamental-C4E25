from flask import Flask, render_template             #gõ fapp
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world, this is flask homepage"

@app.route("/c4e25")
def c4e25():
    return "this is C4E25, happy coding!!!"

@app.route("/hi/phong")
def hi_me():
    return "Hello Phong"

@app.route("/hi/<name>")
def hi(name):
    return "Hi " + name + " Hello"

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return str(a+b)

@app.route("/simple_html")
def simple_html():
    return "<h3>That 's ok</h3>"

@app.route("/html")
def html():
    return render_template("sample.html")  # hàm phải có ()

food_list = [
    "Bun dau",
    "Thit cho",
    "Xoi xeo",
    "Chim cut",

]

@app.route("/menu")
def menu():
    return render_template("menu.html", food_list=food_list)

@app.route("/food/<int:index>")     #trang detail
def food(index):
    return render_template("food.html", title=food_list[index])

detail = {
    'title': "Bun dau",
    "image": "https://vnn-imgs-f.vgcloud.vn/2019/01/23/19/hlv-park-hang-seo-600x400.jpg",

}
@app.route("/food_detail")
def food_detail():
    return render_template("food_detail.html", detail=detail)
    
if __name__ == '__main__':
  app.run(debug=True)