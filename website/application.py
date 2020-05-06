from flask import Flask, render_template, request, session

from models.database import DataBase

app = Flask(__name__)
app.secret_key = "hello"

start = True
db = DataBase()
VIBES = ["HAPPY", "SAD", "ENERGETIC", "CALM"]


@app.route("/playlist/<_id>")
def songs(_id):
    db = DataBase()
    play_list = db.get_playlists_by_vibe(VIBES[int(_id) - 1])
    cur_vibe = VIBES[int(_id) - 1]
    vibe = request.args.get("val")

    if vibe:
        session["vibe"] = vibe
    else:
        session["vibe"] = "0"

    rep = {"run": True, "playlist": play_list, "cur_vibe": cur_vibe, "session": session}
    return render_template("index.html", **rep)


@app.route("/")
def home():
    db = DataBase()
    play_list = db.get_playlists_by_vibe("None")
    ref = {"playlist": play_list, "session": session}
    return render_template("index.html", **ref)


if __name__ == "__main__":
    app.run(debug=True)
