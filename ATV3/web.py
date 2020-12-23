# pip3 install flask
# which pip3
# which python3
# kill $(lsof -t -i:5000)

from flask import Flask, render_template
from operation import *
from random import *

app = Flask(__name__)

back = "<a href='/'>Go back</a>"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sum')
def soma():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    result = sum_two_numbers(number1, number2)
    return f'Sum of {number1} and {number2} is equal to  {result}<br>{back}'


@app.route('/sub')
def sub():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    result = subtract_two_numbers(number1, number2)
    return f' {number1} minus {number2} is equal to  {result}<br>{back}'
    render_tem


@app.route('/mul')
def mul():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    result = multiply_two_numbers(number1, number2)
    return f'{number1} multiplied by {number2} is equal to  {result}<br>{back}'


@app.route('/div')
def div():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    result = divide_two_numbers(number1, number2)
    return f'{number1} divided by {number2} is equal to  {result}<br>{back}'


app.run(debug=True)
