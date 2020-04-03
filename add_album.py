import json

from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request


def save_album(album_data):
    artist = album_data["artist"]
    genre = album_data["genre"]
    album = album_data["album"]
    year = album_data["year"]
    album_name = request.forms.get("album")
    filename = "{}-{}.json".format(artist, genre, album, year)

    with open(filename, "w") as fd:
        json.dump(album_data, fd)
    return filename


@route("/albums", method="POST")
def albums():
    album_data = {
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
        "album": request.forms.get("album"),
        "year": request.forms.get("year")
    }
    resource_path = save_album(album_data)
    print("Album saved at: ", resource_path)

    return "Данные успешно сохранены"


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)