import contextlib

LIBNAME="IntegLA"
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
    "Val2": "gamma"
}


@contextlib.contextmanager
def read_and_formatting(filename1, filename2, filename3):
    file1 = open(filename1, 'a')
    file2 = open(filename2, 'a')
    file3 = open(filename3, 'a')
    yield file1, file2, file3
    #TODO clang-format
    file1.close()
    file2.close()
    file3.close()


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
    def __init__(
        self,
        func,
        group,
        ret,
        target,
        args
        ):
        # parse_args
        self.arg_list = list()
        for arg in args:
            arg_list.append(arg_type(target=target, arg=arg))

        self.purename=func
        self.name= LIBNAME + "_" + group + "_" + "_".join([arg.pure_type  for arg in arg_list]) + "_" + func
        self.ret=ret

def generate(func, group, targets, args, src_file, test_file, header_file):
    main = str()
    for target, ret in targets:
        function=function_type(func=func, group=group, ret=ret, target=target, args=args)

        main += ret + " " + func + "("
        main += ", ".join([arg.type + " " + arg.name
                           for arg in arg_list]) + ")"
        header_file.writelines(main + ";\n")
        main = ""
