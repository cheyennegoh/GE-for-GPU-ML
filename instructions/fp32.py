# fp32.py

def add(dest, src):
    return f"{dest} += {src};"

def sub(dest, src):
    return f"{dest} -= {src};"

def mul(dest, src):
    return f"{dest} *= {src};"

def div(dest, src):
    return f"{dest} /= {src};"

def swap(src):
    return f"R8 = R0; R0 = {src}; {src} = R8;"

def abs():
    return "R0 = abs(R0);"

def sqrt():
    return "R0 = sqrt(R0);"

def sin():
    return "R0 = __sinf(R0);"

def cos():
    return "R0 = __cosf(R0);"
