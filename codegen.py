# codegen.py

import os
import subprocess
import tempfile
import struct
import numpy as np


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
                     f'\tfor (int i = 0; i < {n_registers}; i++)\n'
                     '\t{\n'
                     f'\t\tr[i] = r[i % {x.shape[1]}];\n'
                     '\t}\n\n'
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
            f'\t{declare_input_array};\n\n'
            f'\tstatic float pred[{len(expressions)}][{x.shape[0]}];\n\n'
            f'\tfor (int i = 0; i < {x.shape[0]}; i++)\n'
            '\t{\n'
            f'{pred}'
            '\t}\n\n'
            '\tif (argc > 1)\n'
            '\t{\n'
            f'\t\twrite_data(argv[1], (float *)pred, {len(expressions)} * {x.shape[0]});\n'
            '\t}\n\n'
            '\treturn 0;\n\n'
            '}\n')
    
    return '\n'.join([include, write_data, evaluate, main])


def run_program(x, expressions, compiler, n_registers):
    tmpdir = tempfile.TemporaryDirectory()

    try:
        if compiler == 'gcc':
            code = generate_code_gcc(x, expressions, n_registers)
            program_path = os.path.join(tmpdir.name, 'program.c')
        
        with open(program_path, 'w') as f:
            f.write(code)

        executable_path = os.path.join(tmpdir.name, 'executable')

        if compiler == 'gcc':
            compile_command = ['gcc', program_path, '-lm', '-o', executable_path]
        
        subprocess.run(compile_command)

        data_path = os.path.join(tmpdir.name, 'data.bin')
        subprocess.run([executable_path, data_path])
        
        with open(data_path, "rb") as file:
            file_content = file.read()
            array = struct.unpack(f'{len(file_content) // struct.calcsize("f")}f', 
                                  file_content)
    
    finally:
        tmpdir.cleanup()

    return np.array(array).reshape((len(expressions), x.shape[0]))