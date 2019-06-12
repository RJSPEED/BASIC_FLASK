
from flask import Flask, render_template, request, redirect, session, jsonify

import random

app = Flask(__name__)
app.secret_key = "The session needs this!"

@app.route('/randoms', methods=['GET'])
def return_random6():
    return_list = []
    for i in range (6):
        return_list.append(random.randint(1,6))
    return render_template('my_test.html', param=return_list)

@app.route('/cowsay/<speech>', methods=['GET'])
def return_cowsay(speech):
    return_dict = {'the cow says':[]}
    return_dict['the cow says'].append(speech + " moo !")
    return jsonify(return_dict)

@app.route('/word/<my_int>', methods=['GET'])
def word(my_int):
    my_int = int(my_int)-1
    text_list =[]
    return_dict = {'word is':[]}

    with open("test.txt", 'r') as file_object:
        #Read entire file
        whole_text = file_object.read()
        #Add items split by blank space into list
        text_list = whole_text.split()
        return_dict['word is'].append(text_list[my_int])
    return jsonify(return_dict)

@app.route('/add/<value1>/<value2>', methods=['GET'])
def add(value1, value2):
    return_dict = {'result':[]}
    return_dict['result'].append(int(value1) + int(value2))
    return jsonify(return_dict)

@app.route('/subtract/<value1>/<value2>', methods=['GET'])
def subtract(value1, value2):
    return_dict = {'result':[]}
    return_dict['result'].append(int(value1) - int(value2))
    return jsonify(return_dict)

@app.route('/multiply/<value1>/<value2>', methods=['GET'])
def multiply(value1, value2):
    return_dict = {'result':[]}
    if int(value1) == 0 or int(value2) == 0:
        return_dict['result'].append("One of the input values is zero, pls retry.")
    else:
        return_dict['result'].append(int(value1) * int(value2))
    return jsonify(return_dict)

@app.route('/divide/<value1>/<value2>', methods=['GET'])
def divide(value1, value2):
    return_dict = {'result':[]}
    if int(value1) == 0 or int(value2) == 0:
        return_dict['result'].append("One of the input values is zero, pls retry.")
    else:
        return_dict['result'].append(int(value1) / int(value2))
    return jsonify(return_dict)
   
def run():
    app.run(debug=True)