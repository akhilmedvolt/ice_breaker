from dotenv import load_dotenv

load_dotenv()

from flask import Flask, request, jsonify, render_template
from ice_breaker import ice_break_with

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary, profile_link = ice_break_with(name=name)
    return jsonify(
        {"summary_and_facts": summary.to_dict(), "picture_url": profile_link}
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
