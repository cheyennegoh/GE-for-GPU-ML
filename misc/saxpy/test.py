import os
import subprocess

dir = os.path.dirname(os.path.abspath(__file__))

input = 'saxpy.cu'
output = 'saxpy'

nvcc_args = ['nvcc',
             '-o',
             f"{dir}/{output}",
             f"{dir}/{input}"]

# Compile
subprocess.run(nvcc_args)

# Execute
subprocess.run(f"{dir}/{output}")