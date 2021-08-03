# Checking if Request is Get or Post
from flask import Flask, render_template, redirect, url_for, request, jsonify
# GetRequest used for API
import requests


app = Flask(__name__)
all_user_urls = "https://jsonplaceholder.typicode.com/users/"
user_detail_and_album_url = "https://jsonplaceholder.typicode.com/albums/"


@app.route("/")
def home():
    return redirect(url_for('index'))


@app.route("/<name>")
def Name(name):
    # return f'hello {name}'
    return redirect(url_for('index'))


@app.route("/<name>/")
def Name2(name):
    return redirect(url_for('index'))


# All USERS PAGE FONK
@app.route("/users")
def index():
    response = requests.get(all_user_urls)
    user_info = response.json()
    return render_template("index.html", userSummaryInfo=user_info)

# ONE USER DETAİL PAGE FONK
@app.route("/users/<user_id>/albums")
def userDetail(user_id):
    response_user = requests.get(all_user_urls + str(user_id))  # ONLY ONE USER DICT
    response_albums = requests.get(user_detail_and_album_url) # All USER'S ALBUMS DICT

    user_info = response_user.json()
    user_albums = response_albums.json()

    # İF YOUSER İS NO FOUND
    if user_info == {}:
        return render_template("index.html", error="Not Find a User")
    else:
        return render_template("user-detail.html", userProfileDetaile=user_info, user_albums=user_albums)


if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         user_id = request.form.get("id")
#         response = requests.get(user_detail_and_album_url + user_id)
#         user_info = response.json()
#         return render_template("user-detail.html", userProfileDetaile=user_info)
#     else:
#         response = requests.get(user_detail_and_album_url)
#         user_info = response.json()
#         return render_template("index.html", userSummaryInfo=user_info)
