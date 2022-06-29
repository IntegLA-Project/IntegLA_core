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
    "INT": "size_t",
    "RET": "ret"
}

class code_omp_section():

    def __init__(self, declare, operation, target, ret, omp_option):
        self.code="#pragma omp parallel for"
        if omp_option != None:
            self.option = omp_option.format(**CONVERT_LIST,
                                   target=target,
                                   Vec=TYPE_NAMES[target],
                                   target_ret=ret,
                                   )
            self.code += " " + self.option

class code_operation_section():

    def __init__(self, declare, operation, target, ret, omp_section):
        self.code = operation.format(**CONVERT_LIST,
                                   target=target,
                                   Vec=TYPE_NAMES[target],
                                   target_ret=ret,
                                   omp_directive=omp_section
                                   )

class code_section():

    def __init__(self, declare, operation, target, ret, omp_option):
        self.operation = operation
        self.code = declare + "{\n"


        self.omp = code_omp_section(declare=declare,
                              operation=operation,
                              target=target,
                              ret=ret,
                              omp_option=omp_option)

        self.op = code_operation_section(declare=declare,
                              operation=operation,
                              target=target,
                              ret=ret,
                              omp_section=self.omp.code)

        self.code += self.op.code + "}\n"

class arg_type():

    def __init__(
        self,
        target,
        arg,
    ):
        self.target = target
        self.type = arg[0].format(
            **CONVERT_LIST,
            target=target,
            Vec=TYPE_NAMES[target],
        )
        self.name = arg[1].format(
            **CONVERT_LIST,
            target=target,
            Vec=TYPE_NAMES[target],
        )
        self.pure_type = self.type.replace("const ", "")


class function_type():

    def __init__(self, name, group, ret, target, args, operation, omp_option):
        # parse args
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


        # create code
        self.code = code_section(declare=self.declare,
                              operation=operation,
                              target=target,
                              ret=ret,
                              omp_option=omp_option)


def generate(name, group, targets, args, operation, src_file, test_file,
             header_file, omp_option=None):
    main = str()
    for target, ret in targets:
        func = function_type(name=name,
                             group=group,
                             ret=ret,
                             target=target,
                             args=args,
                             operation=operation,
                             omp_option=omp_option)

        # write file
        header_file.writelines(func.prototype + "\n")
        src_file.writelines(func.code.code)
