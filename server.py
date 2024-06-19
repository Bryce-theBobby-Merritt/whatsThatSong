from flask import Flask, render_template, request
from waitress import serve
from input_handling import handle_input

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/guessingGame', methods=['GET', 'POST'])
def guessingGame():
    user_playlist_link_input = handle_input(request.args.get('playlist_link'))

    if request.method == 'POST':
        guess = request.form.get('song_guess')
        print(guess)

    return render_template('guessingGame.html', playlist_link=user_playlist_link_input)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)