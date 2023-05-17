from flask import Flask, render_template, request
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'w8BLuXnr4w'

@app.route('/', methods=['GET', 'POST'])
def index():
    value = 0.0
    if request.method == 'POST':
        quantity = request.form.get('quantity') 
        code = request.form.get('symbol')
        response = requests.get('https://api.nbp.pl/api/exchangerates/tables/a/')
        data = response.json()
       
        for item in data[0]['rates']:
           if item['code'] == code:
                rate = f"{item['mid']:.2f}"
        
        try:
            value = float(quantity) * float(rate)
            value = f'{quantity} {code} to {value:.2f} zł'
        except ValueError:
            value = 'Wpisz ilość waluty'

    return render_template('index.html', value = value)

@app.route('/tabela', methods=['GET', 'POST'])
def table():
    if request.method == 'GET':
        response = requests.get('https://api.nbp.pl/api/exchangerates/tables/c/')
        data = response.json()
        date = data[0]['effectiveDate']
        
            

    return render_template('table.html', data=data, date=date )
    

if __name__ == '__main__':
    app.run(debug=True)
