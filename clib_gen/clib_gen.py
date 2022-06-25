import contextlib
import subprocess, sys, shutil

LIBNAME = "IntegLA"
TYPE_NAMES = {
    "double": "f64Vec",
    "float": "f32Vec",
    "int32_t": "i32Vec",
    "int64_t": "i64Vec"
}
CONVERT_LIST = {
    "Vec0": "x",
    "Vec1": "y",
    "Vec2": "z",
    "Val0": "alpha",
    "Val1": "beta",
    "Val2": "gamma",
    "INT": "size_t"
}


@contextlib.contextmanager
def read_and_formatting(filename1, filename2, filename3):
    file1 = open(filename1, 'a')
    file2 = open(filename2, 'a')
    file3 = open(filename3, 'a')
    yield file1, file2, file3
    file1.close()
    file2.close()
    file3.close()

    # check clang-format command is installed?
    if shutil.which('clang-format') == None:
        print('clang-format is not found.')
        sys.exit(1)

    # formatting..
    err = subprocess.run(['clang-format', '-i', filename1])
    if err.returncode != 0:
        print('clang-format failed for ' + filename1)
        sys.exit(1)

    err = subprocess.run(['clang-format', '-i', filename2])
    if err.returncode != 0:
        print('clang-format failed for ' + filename2)
        sys.exit(1)

    err = subprocess.run(['clang-format', '-i', filename3])
    if err.returncode != 0:
        print('clang-format failed for ' + filename3)
        sys.exit(1)


class arg_type():

    def __init__(
        self,
        target,
        arg,
    ):
        self.target = target
        self.type = arg[0].format(**CONVERT_LIST,
                                  target=target,
                                  Vec=TYPE_NAMES[target])
        self.name = arg[1].format(**CONVERT_LIST,
                                  target=target,
                                  Vec=TYPE_NAMES[target])
        self.pure_type = self.type.replace("const ", "")


class function_type():

    def __init__(self, name, group, ret, target, args):
        # parse_args
        self.arg_list = list()
        for arg in args:
            self.arg_list.append(arg_type(target=target, arg=arg))

        self.purename = name
        self.name = LIBNAME + "_" + group + "_" + "_".join(
            [arg.pure_type for arg in self.arg_list]) + "_" + name
        self.ret = ret
        self.declare = self.ret + " " + self.name + "(" + ", ".join(
            [arg.type + " " + arg.name for arg in self.arg_list]) + ")"
        self.prototype = self.declare + ";"


class code_type():

    def __init__(self, declare, operation, target):
        self.operation = operation
        self.code = declare + "{\n"

        self.op = operation.format(**CONVERT_LIST,
                                   target=target,
                                   Vec=TYPE_NAMES[target])

        self.code += self.op + "}\n"


def generate(name, group, targets, args, operation, src_file, test_file,
             header_file):
    main = str()
    for target, ret in targets:
        func = function_type(name=name,
                             group=group,
                             ret=ret,
                             target=target,
                             args=args)
        code = code_type(declare=func.declare,
                         operation=operation,
                         target=target)

        # write file
        header_file.writelines(func.prototype + "\n")
        src_file.writelines(code.code)
