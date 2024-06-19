from flask import Flask, render_template, request
from waitress import serve
from input_handling import get_playlist_id_from_link
from Game import Game

app = Flask(__name__)

game = Game()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/guessingGame', methods=['GET', 'POST'])
def guessingGame():
    guess = None

    if request.method == 'GET':
        user_playlist_id = get_playlist_id_from_link(request.args.get('playlist_link'))

        game.set_playlist_id(user_playlist_id)
        game.get_all_tracks_from_playlist_id()
        game.ready_game()
        game.start()

        return render_template('guessingGame.html', playlist_id=user_playlist_id)


    if request.method == 'POST':
        guess = request.form.get('song_guess')
        print(guess)

        return render_template('guessingGame.html', user_guess=guess)



if __name__ == "__main__":
    #For production, use serve:
    #serve(app, host="0.0.0.0", port=8000)

    #For development (featuring live file updates), use localhost without serving:
    app.run(host="0.0.0.0", port=8000)