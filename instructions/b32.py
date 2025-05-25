# b32.py

def and_(dest, src):
    return f"{dest} = {dest} & {src};"

def or_(dest, src):
    return f"{dest} = {dest} | {src};"

def nand(dest, src):
    return f"{dest} = ~({dest} & {src});"

def nor(dest, src):
    return f"{dest} = ~({dest} | {src});"

def not_(x):
    return f"{x} = ~{x};"
