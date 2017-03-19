from flask import *
from datetime import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for("login"))
number_visitor = 0

image_list = [
    { "src" : "https://i.ytimg.com/vi/icSRtb0Vbcs/maxresdefault.jpg",
      "title" : " abc",
      "tag" : " abc"
      },
    { "src" : "https://s-media-cache-ak0.pinimg.com/originals/f9/d1/74/f9d17484e7445115a4e0360332147577.jpg",
      "title": "acb",
      "tag" : " acb"
      },
    { "src" : "http://tghinhanhdep.com/wp-content/uploads/2015/10/tai-hinh-nen-tinh-yeu-doi-lua-dep-nhat-11.jpg",
    "title" : " acb",
    "tag" : "acb",
      }
             ]

@app.route("/login")
def login():
    global number_visitor
    number_visitor += 1
    current_time_sever = str(datetime.now())
    return render_template("login.html", )
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/food")
def food():
    return render_template("food.html", image_list=image_list)
if __name__ == '__main__':
    app.run()
