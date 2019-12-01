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
	sprites = req['sprites']
	name = req['name']
	weight = req['weight']

	print(json.dumps(stats, indent=2))
	print(json.dumps(types, indent=2))
	print(json.dumps(sprites, indent=2))
	print(json.dumps(name, indent=2))
	print(json.dumps(weight, indent=2))



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
