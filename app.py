from flask import Flask, render_template

app = Flask(__name__)

cars = [
    {"id": 1, "brand": "Toyota", "model": "Camry", "year": 2020},
    {"id": 2, "brand": "Honda", "model": "Civic", "year": 2019},
    {"id": 3, "brand": "Ford", "model": "Focus", "year": 2021},
    {"id": 4, "brand": "Hyundai", "model": "Elantra", "year": 2022},
]

@app.route('/')
def index():
    return render_template('index.html', cars=cars)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
