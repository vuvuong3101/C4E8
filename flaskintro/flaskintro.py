from flask import *
from datetime import *
app = Flask(__name__)

@app.route("/")
def contact():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
