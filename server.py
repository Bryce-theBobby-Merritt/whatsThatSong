from flask import Flask, render_template, request
from waitress import serve
from input_handling import get_playlist_id_from_link
from Game import Game

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/guessingGame', methods=['GET', 'POST'])
def guessingGame():
    user_playlist_id = get_playlist_id_from_link(request.args.get('playlist_link'))

    game = Game()
    game.set_playlist_id(user_playlist_id)
    game.get_all_tracks_from_playlist_id()

    if request.method == 'POST':
        guess = request.form.get('song_guess')
        print(guess)

    return render_template('guessingGame.html', playlist_id=user_playlist_id)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)