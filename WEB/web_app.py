#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route("/")
def root():
    return flask.render_template(
        'index.html'
    )

@app.route("/gcd", methods = ['GET'])
def gcd():
    if request.method == 'GET':
        num1 = request.args.get('number1')
        num2 = request.args.get('number2')
    elif request.method == 'POST':
        name_param = request.form.get('number1', 'number2')

    if num1 == None: num1 = 0
    if num2 == None: num2 = 0

    num1, num2 = int(num1), int(num2)

    def algEv(a, b):
        if a < b:
            (a, b) = (b, a)

        if b == 0:
            return a
        else:
            return int(algEv(b, a % b))

    res= -1
    res= algEv(num1, num2)

    return flask.render_template(
        'gcd.html',
        res=res,
        num1=num1,
        num2=num2,
        method=request.method
    )

@app.route("/numSys", methods = ['GET'])
def numSys():
    if request.method == 'GET':
        number = request.args.get('number')
        base = request.args.get('base')

    if number == None: number = 0
    if base == None: base = 0

    number, base = int(number), int(base)

    def numsys(num: 'int', base: 'int') -> 'str':
        a = num
        b = base
        x = ""

        while a > 0:
            c = int(48 + a % b)  # c is a code number of a symbol.
            if a % b > 9: c += 7  # +7 because ord('9') = 57 and ord('A') = 65, so the difference is (7+1). 1 is for the next symbol.
            x = chr(c) + x  # We make "x" starting from the rightest symbol and moving left.
            a = a // b
        return x

    res = numsys(number, base)

    return flask.render_template(
        'numSys.html',
        number=number,
        base=base,
        res=res,
        method=request.method
    )

if __name__ == '__main__':
    app.run(debug=True)
