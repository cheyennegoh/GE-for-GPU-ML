# fp32.py

def add(dest, src):
    return f"{dest} += {src};"

def sub(dest, src):
    return f"{dest} -= {src};"

def mul(dest, src):
    return f"{dest} *= {src};"

def pdiv(dest, src):
    return f"{dest} = ({src} != 0) ? {dest} / {src} : {dest} + 10e6;"

def aq(dest, src):
    return f"{dest} = {dest} / sqrt(1 + pow({src}, 2));"

def swap(a, b, temp):
    return f"{temp} = {a}; {a} = {b}; {b} = {temp};"

def sin(x):
    return f"{x} = sinf({x});"

def cos(x):
    return f"{x} = cosf({x});"

def tanh(x):
    return f"{x} = tanhf({x});"

def if_gt(a, b):
    return f"if ({a} > {b})"
