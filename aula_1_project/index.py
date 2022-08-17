from flask import Flask, render_template
from Dog import Dog

app = Flask(__name__)

@app.route('/')
def index():
    dogs = [
        Dog("Bobby", "Marcia", "10/10/2018", "Caramelo", "Vira-latas"),
        Dog("Snoopy", "Marcos", "08/07/2007", "Caramelo com Branco", "Pincher"),
        Dog("Brutus", "William", "06/11/20010", "Branco", "Bull Terrier"),
    ]
    return render_template('index.html', dogs=dogs, petShopName="Love dogs")

app.run(host='0.0.0.0', port=5000)