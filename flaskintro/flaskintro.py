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

image_food_list = [
    {"src" :"https://media.foody.vn/res/g65/645246/prof/s480x300/foody-mobile-17424938_17349033667-491-636257011981478757.jpg",

     "title": "Teastory Vietnam",

     "text" : "100 Phạm Ngọc Thạch,  Quận Đống Đa, Hà Nội"
     },

    {"src" : "https://media.foody.vn/res/g10/95877/prof/s480x300/foody-mobile-ghf546-jpg-171-636137015804800853.jpg",

     "title" : "Ngọc Thạch Quán - Sữa Chua & Caramen",

     "text": "C5 TT. Kim Liên, Lương Định Của,  Quận Đống Đa, Hà Nội"
     },

    {"src": "https://media.foody.vn/res/g29/287833/prof/s480x300/foody-mobile-hongtra-jpg-473-636136079398873434.jpg",

     "title":"Hồng Trà Coffee & Tea House - Thái Hà" ,

     "text" : "302 Thái Hà,  Quận Đống Đa, Hà Nội"
     },
    {"src": "https://media.foody.vn/res/g10/94216/prof/s480x300/foody-mobile-cocktail-jpg-635469825552153119.jpg",

    "title" : "Pharaoh's Bar & Upper - Lotte Center",

    "text" : "Tầng 63 - 64, Lotte Center, 54 Liễu Giai,  Quận Ba Đình, Hà Nội",
    }
]
@app.route("/addfood", methods=["GET", "POST"])
def add_food():
    if request.method == "GET":
        return render_template("addfood.html")
    if request.method == "POST":
        new_food = FoodItem()
        new_food.src = request.form["source"]
        new_food.imgae = request.files["image"]
        new_food.title = request.form["title"]
        new_food.description = request.form["description"]
        new_food.save()
        return render_template("addfood.html")



@app.route("/deletefood", methods=["GET", "POST"])
def delete_food():
    if request.method == "GET":
        return render_template("deletefood.html")
    if request.method == "POST":
        new_food = FoodItem.objects(title =request.form["title"]).first()
        if new_food is not None:
            new_food.delete()
        return render_template("deletefood.html")

@app.route("/editfood", methods=["GET", "POST"])
def edit_food():
    if request.method == "GET":
        return render_template("editfood.html")
    if request.method == "POST":
        edit_food = FoodItem.objects(title = request.form["title"]).first()
        if edit_food is not None:
            edit_food.src = request.form["source"]
            # edit_food.title = request.form["title"]
            edit_food.description = request.form["description"]
            edit_food.save()
        return render_template("editfood.html")

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

@app.route("/foodblog")
def foodblog():
    return render_template("foodblog.html", food_list = image_food_list)
if __name__ == '__main__':
    app.run()
