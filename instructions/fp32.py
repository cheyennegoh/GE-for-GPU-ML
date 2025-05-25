# fp32.py

def add(dest, src):
    return f"{dest} += {src};"

def sub(dest, src):
    return f"{dest} -= {src};"

def mul(dest, src):
    return f"{dest} *= {src};"

def div(dest, src):
    return f"{dest} /= {src};"

def swap(a, b, temp):
    return f"{temp} = {a}; {a} = {b}; {b} = {temp};"

def abs(n):
    return f"{n} = abs({n});"

def sqrt(x):
    return f"{x} = sqrt({x});"

def sin(x):
    return f"{x} = sinf({x});"

def cos(x):
    return f"{x} = cosf({x});"

def if_gt(a, b):
    return f"if ({a} > {b})"