# codegen.py

import os
import subprocess
import tempfile
import struct
import numpy as np
import time

def generate_code_gcc(x, expressions, n_registers):
    include = ('#include <math.h>\n'
               '#include <stdio.h>\n'
               '#include <string.h>\n')
    
    write_data = ('void write_data(char *filename, float *data, size_t size)\n'
                  '{\n'
                  '\tFILE *file = fopen(filename, "wb");\n'
                  '\tfwrite(data, sizeof(float), size, file);\n'
                  '\tfclose(file);\n'
                  '}\n')

    evaluate = ''
    for i, expression in enumerate(expressions):
        indented_expression = '\n'.join([f'\t{line}' for line in expression.splitlines()])

        evaluate += (f'float evaluate{i}(float x[{x.shape[1]}])\n'
                     '{\n'
                     f'\tfloat r[{n_registers}];\n\n'
                     f'\tfor (int i = 0; i < {n_registers}; i++) r[i] = x[i % {x.shape[1]}];\n\n'
                     f'{indented_expression}\n\n'
                     f'\treturn r[0];\n'
                     '}\n')

    subarrays = []
    for row in x:
        subarrays.append(''.join(['{', ', '.join([str(val) for val in row.tolist()]), '}']))
    
    declare_input_array = ''.join([f'static float x[{x.shape[0]}][{x.shape[1]}] = ', '{', ', '.join(subarrays), '}'])

    pred = ''
    for i in range(len(expressions)):
        pred += f'\t\tpred[{i}][i] = evaluate{i}(x[i]);\n'

    main = (f'int main(int argc, char *argv[])\n'
            '{\n'
            f'\t{declare_input_array};\n'
            f'\tstatic float pred[{len(expressions)}][{x.shape[0]}];\n\n'
            f'\tfor (int i = 0; i < {x.shape[0]}; i++)\n'
            '\t{\n'
            f'{pred}'
            '\t}\n\n'
            '\tif (argc > 1)\n'
            '\t{\n'
            f'\t\twrite_data(argv[1], (float *)pred, {len(expressions)} * {x.shape[0]});\n'
            '\t}\n\n'
            '\treturn 0;\n'
            '}\n')
    
    return '\n'.join([include, write_data, evaluate, main])


def generate_code_nvcc(x, expressions, n_registers):
    include = ('#include "cuda_runtime.h"\n'
               '#include "device_launch_parameters.h"\n'
               '#include <stdio.h>\n')

    write_data = ('void write_data(char *filename, float *data, size_t size)\n'
                  '{\n'
                  '\tFILE *file = fopen(filename, "wb");\n'
                  '\tfwrite(data, sizeof(float), size, file);\n'
                  '\tfclose(file);\n'
                  '}\n')

    evaluate = ''
    for i, expression in enumerate(expressions):
        indented_expression = '\n'.join([f'\t{line}' for line in expression.splitlines()])

        evaluate += ('__global__\n'
                     f'void evaluate{i}(float *x, float *pred)\n'
                     '{\n'
                     '\tint tid = blockIdx.x * blockDim.x + threadIdx.x;\n'
                     f'\tif (tid >= {x.shape[0]}) return;\n\n'
                     f'\tx += {x.shape[1]} * tid;\n'
                     f'\tpred += {x.shape[0]} * {i};\n\n'
                     f'\tfloat r[{n_registers}];\n'
                     f'\tfor (int i = 0; i < {n_registers}; i++) r[i] = x[i % {x.shape[1]}];\n\n'
                     f'{indented_expression}\n\n'
                     f'\tpred[tid] = r[0];\n'
                     '}\n')
    
    subarrays = []
    for row in x:
        subarrays.append(''.join(['{', ', '.join([str(val) for val in row.tolist()]), '}']))
    
    declare_input_array = ''.join([f'static float x[{x.shape[0]}][{x.shape[1]}] = ', '{', ', '.join(subarrays), '}'])

    launch_kernels = ''
    for i in range(len(expressions)):
        launch_kernels += f'\tevaluate{i}<<<(({x.shape[0]} + 255) / 256), 256>>>(d_x, d_pred);\n'
    
    main = (f'int main(int argc, char *argv[])\n'
            '{\n'
            f'\t{declare_input_array};\n'
            f'\tstatic float pred[{len(expressions)}][{x.shape[0]}];\n\n'
            '\tfloat *d_x, *d_pred;\n\n'
            f'\tcudaMalloc(&d_x, {x.shape[0]} * {x.shape[1]} * sizeof(float));\n'
            f'\tcudaMalloc(&d_pred, {len(expressions)} * {x.shape[0]} * sizeof(float));\n\n'
            f'\tcudaMemcpy(d_x, x, {x.shape[0]} * {x.shape[1]} * sizeof(float), cudaMemcpyHostToDevice);\n\n'
            f'{launch_kernels}\n'
            f'\tcudaMemcpy(pred, d_pred, {len(expressions)} * {x.shape[0]} * sizeof(float), cudaMemcpyDeviceToHost);\n\n'
            '\tcudaFree(d_x);\n'
            '\tcudaFree(d_pred);\n\n'
            '\tif (argc > 1)\n'
            '\t{\n'
            f'\t\twrite_data(argv[1], (float *)pred, {len(expressions)} * {x.shape[0]});\n'
            '\t}\n\n'
            '\treturn 0;\n'
            '}\n')

    return '\n'.join([include, write_data, evaluate, main])


def run_program(x, expressions, compiler, n_registers):
    with tempfile.TemporaryDirectory() as tmpdirname:
        if compiler == 'gcc':
            code = generate_code_gcc(x, expressions, n_registers)
            program_path = os.path.join(tmpdirname, 'program.c')
        elif compiler == 'nvcc':
            code = generate_code_nvcc(x, expressions, n_registers)
            program_path = os.path.join(tmpdirname, 'program.cu')
        
        with open(program_path, 'w') as f:
            f.write(code)

        executable_path = os.path.join(tmpdirname, 'executable')

        if compiler == 'gcc':
            compile_command = ['gcc', program_path, '-o', executable_path, '-lm']
        elif compiler == 'nvcc':
            compile_command = ['nvcc', program_path, '-o', executable_path, '-use_fast_math', '-O0',  '-Xptxas', '-O0', '-Xcicc', '-O0']
        
        # start_time = time.time()

        subprocess.run(compile_command)

        # duration = time.time() - start_time
        # print("\nCompilation time:", duration, end='\t')

        input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.bin')
        data_path = os.path.join(tmpdirname, 'data.bin')

        # start_time = time.time()

        subprocess.run([executable_path, input_path, data_path])

        # duration = time.time() - start_time
        # print("Execution time:", duration, end='\n\n')

        with open(data_path, "rb") as file:
            file_content = file.read()
            array = struct.unpack(f'{len(file_content) // struct.calcsize("f")}f', 
                                  file_content)

    return np.array(array).reshape((len(expressions), x.shape[0]))