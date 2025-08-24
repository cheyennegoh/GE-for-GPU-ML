# instructions.py

def add(dest, src):
    """Creates line of C code for addition assignment operator.

    # Arguments
        dest: Destination register as a string.
        src: Source register as a string.
    
    # Returns
        A string containing C instruction.
    """
    return f"{dest} += {src};"

def sub(dest, src):
    """Creates line of C code for subtraction assignment operator.

    # Arguments
        dest: Destination register as a string.
        src: Source register as a string.
    
    # Returns
        A string containing C instruction.
    """
    return f"{dest} -= {src};"

def mul(dest, src):
    """Creates line of C code for multiplication assignment operator.

    # Arguments
        dest: Destination register as a string.
        src: Source register as a string.
    
    # Returns
        A string containing C instruction.
    """
    return f"{dest} *= {src};"

def pdiv(dest, src):
    """Creates line of C code for protected division operator with assignment.

    # Arguments
        dest: Destination register as a string.
        src: Source register as a string.
    
    # Returns
        A string containing C instruction.
    """
    return f"{dest} = ({src} != 0) ? {dest} / {src} : {dest} + 10e6;"

def aq(dest, src):
    """Creates line of C code for analytic quotient operator with assignment.

    # Arguments
        dest: Destination register as a string.
        src: Source register as a string.
    
    # Returns
        A string containing C instruction.
    """
    return f"{dest} = {dest} / sqrt(1 + pow({src}, 2));"

def swap(a, b, temp):
    """Creates line of C code for swapping registers.

    # Arguments
        a: A register as a string.
        b: A register as a string.
        temp: The designated temporary register as a string.
    
    # Returns
        A string containing C instruction.
    """
    return f"{temp} = {a}; {a} = {b}; {b} = {temp};"

def sin(x):
    """Creates line of C code for sine function.

    # Arguments
        x: A register as a string.
    
    # Returns
        A string containing C instruction.
    """
    return f"{x} = sinf({x});"

def cos(x):
    """Creates line of C code for cosine function.

    # Arguments
        x: A register as a string.
    
    # Returns
        A string containing C instruction.
    """
    return f"{x} = cosf({x});"

def tanh(x):
    """Creates line of C code for hyperbolic tangent function.

    # Arguments
        x: A register as a string.
    
    # Returns
        A string containing C instruction.
    """
    return f"{x} = tanhf({x});"

def if_gt(a, b):
    """Creates line of C code for if greater than branching condition.

    # Arguments
        a: A register as a string.
        b: A register as a string.
    
    # Returns
        A string containing C instruction.
    """
    return f"if ({a} > {b})"
