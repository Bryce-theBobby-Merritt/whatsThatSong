from flask import Flask, render_template, request, jsonify
from waitress import serve
from input_handling import get_playlist_id_from_link
from Game import Game

#overarching control variables
production = False
development = True


app = Flask(__name__)
game = Game()


@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    if request.method == 'GET':
        return render_template('index.html', preview=None)

    elif request.method == 'POST':
        user_playlist_id = get_playlist_id_from_link(request.form.get('playlist_link'))
        game.set_playlist_id(user_playlist_id)
        game.get_all_tracks_from_playlist_id()
        return render_template('index.html', preview=game.get_all_song_names())



@app.route('/guessingGame', methods=['GET'])
def guessingGame():
    game.ready_game()
    game.start()
    return render_template('guessingGame.html', current_song=game.get_current_song().get_name(), search_options=game.get_all_song_names())
        

@app.route("/guess", methods=['POST'])
def guess():
    guess = request.form.get('song_guess')
    #TODO game logic to see if the guess is right, if you have enough lives, etc.
    game.guess_song(guess)
    return render_template('guessingGame.html', user_guess=guess, current_song=game.get_current_song().get_name(), search_options=game.get_all_song_names())


if __name__ == "__main__":
    #For production, use serve:
    if production and not development:
        serve(app, host="0.0.0.0", port=8000)

    #For development (featuring live file updates), use localhost without serving:
    if development and not production:
        app.run(host="0.0.0.0", port=8000, debug=True)