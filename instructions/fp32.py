# fp32.py

def add(y, x1, x2):
    return f"{y} = {x1} + {x2};"

def sub(y, x1, x2):
    return f"{y} = {x1} - {x2};"

def mul(y, x1, x2):
    return f"{y} = {x1} * {x2};"

def pdiv(y, x1, x2):
    return f"{y} = ({x2} != 0) ? {x1} / {x2} : {x1} + 10e6;"

def swap(a, b, tmp):
    return f"{tmp} = {a}; {a} = {b}; {b} = {tmp};"

def abs(y, x):
    return f"{y} = abs({x});"

def psqrt(y, x):
    return f"{y} = sqrt(abs({x}));"

def sin(y, x):
    return f"{y} = sinf({x});"

def cos(y, x):
    return f"{y} = cosf({x});"

def if_gt(a, b):
    return f"if ({a} > {b})"