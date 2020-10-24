from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    pokemon_name = request.args.get("pokemon")
    if not pokemon_name:
        return render_template('image.html')
    resp = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    try:
        resp_json = resp.json()
    except ValueError:
        return render_template('image.html', sprites={}, wrong_name=pokemon_name)
    images = resp_json['sprites']
    images = {k: v for k, v in images.items() if isinstance(v, str)}
    return render_template(
        'image.html',
        sprites=images
    )