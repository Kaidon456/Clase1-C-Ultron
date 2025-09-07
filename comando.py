from random import randint

def cadenas(args):
    response = ""
    for arg in args:
        response = response + " " + arg
    return response

def random100():
    return randint(1, 100)