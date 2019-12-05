from flask import Flask, render_template, url_for, request, redirect
import requests
import os
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/<pokemon>')
def pokemon(pokemon):
	req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
	stats = req['stats']
	types = req['types']
	sprites = [req['sprites'][i] for i in req['sprites']]
	name = req['name']
	name = name.capitalize()
	weight = req['weight']
	sprites[0], sprites[1], sprites[2], sprites[3], sprites[4], sprites[5], sprites[6], sprites[7] = sprites[4], sprites[0], sprites[5], sprites[1], sprites[6], sprites[2], sprites[7], sprites[3]
	print(sprites)



	return render_template('pokemon.html', stats = stats, types = types, sprites = sprites, name = name, weight = weight)

@app.route('/get_pokemon', methods=['POST'])
def get_pokemon():
	try:
		pokemon = request.form['pokemon']
		return redirect(url_for('pokemon', pokemon=pokemon))
	except:
		return redirect(url_for('index'))

port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
	app.run(threaded=True, port=port)
