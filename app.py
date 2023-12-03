from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home_page.html")


# 按下search之後顯示的頁面
@app.route("/result")
def search():
    return render_template("search_result.html")


# 用movie_id
@app.route("/movie")
def movie():
    return render_template("movie_page.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
