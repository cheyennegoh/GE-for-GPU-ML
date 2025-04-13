import os
import subprocess

dir = os.path.dirname(os.path.abspath(__file__))

input = 'hello.c'
output = 'hello'

gcc_args = ['gcc',
             '-o',
             f"{dir}/{output}",
             f"{dir}/{input}"]

# Compile
subprocess.run(gcc_args)

# Execute
subprocess.run(f"{dir}/{output}")