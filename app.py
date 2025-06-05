from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

cars = [
    {"id": 1, "brand": "Toyota", "model": "Camry", "year": 2020},
    {"id": 2, "brand": "Honda", "model": "Civic", "year": 2019},
]

@app.route('/')
def index():
    return render_template('index.html', cars=cars)

@app.route('/add', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        new_id = max(car['id'] for car in cars) + 1 if cars else 1
        cars.append({
            "id": new_id,
            "brand": request.form['brand'],
            "model": request.form['model'],
            "year": int(request.form['year'])
        })
        return redirect(url_for('index'))
    return render_template('add_car.html')

@app.route('/delete/<int:car_id>')
def delete_car(car_id):
    global cars
    cars = [car for car in cars if car['id'] != car_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

