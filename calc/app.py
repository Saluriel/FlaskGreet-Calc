from operations import *
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def sum():
    """Adds a and b"""
    answer = add(int(request.args['a']),int(request.args['b']))
    return str(answer)

@app.route('/sub')
def minus():
    """Subtracts a and b"""
    answer = sub(int(request.args['a']),int(request.args['b']))
    return str(answer)

@app.route('/mult')
def product():
    """multiplies a and b"""
    answer = mult(int(request.args['a']),int(request.args['b']))
    return str(answer)

@app.route('/div')
def divide():
    """divides a and b"""
    answer = div(int(request.args['a']),int(request.args['b']))
    return str(answer)

functions = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<calculation>')
"""does all operations on a and b"""
def all_functions(calculation):
    int1 = int(request.args['a'])
    int2 = int(request.args['b'])
    result = functions[calculation](int1, int2)

    return str(result)
