scalar_name = ["alpha", "beta", "gamma"]
vector_name = ["x", "y", "z"]
matrix_name = ["A", "B", "C"]
type_names = {"double":"f64Vec", "float": "f32Vec", "int32_t": "i32Vec", "int64_t": "i64Vec"}

class function_def():
    def generate_arg_list(self, args):
        arg_names = list()
        vec_count = 0
        mat_count = 0
        val_count = 0
        for arg in args:
            if ("{target}" in arg):
                arg_names.append(val_names[val_count])
                val_count += 1
            elif ("Vec" in arg):
                arg_names.append(vec_names[vec_count])
                vec_count += 1
            elif ("Mat" in arg):
                arg_names.append(mat_names[mat_count])
                mat_count += 1
        return arg_names

    def __init__(self,
    target,
    func,
    args,
    ret
    ):
        self.type=target
        self.ret=ret
        self.arg_num=len(args)
        self.name=func
        self.prototype=ret + " " + self.name
    

class Generator():
    # create args -> ["alpha":"const double", "x": "coust f64Vec"...]

    def generate_arg_types(self, args, target):
        arg_types = list()
        vec_count = 0
        mat_count = 0
        val_count = 0
        for i in range(len(args)):
            arg_types.append(args[i].format(target=target, T=type_names[target]))
        print(arg_types)
        return arg_types

    def parse_func_def(self, target, ret, func, arg_types, arg_names):
        func = target + " " + func + "("
        for j in range(len(arg_types)):
            func += arg_types[j] + " " + arg_names[j]
            if(j == len(arg_types)-1):
                func += ")"
            else:
                func += ", "
        print(func)

    def __init__(self,
            targets,
            func,
            returns,
            args
            ):
        for i in range(len(targets)):
            function=function_def(target=targets[i],func=func, args=args, ret=returns[i])
            print(function.arg_num)
            print(function.type)
            print(function.name)
            print(function.prototype)
            
#             arg_types = self.generate_arg_types(args=args, target=target)
#             print(arg_types)
#             arg_names = self.generate_arg_list(args=args)
#             print(arg_names)
#             self.parse_func_def(ret=ret, target=target, func=func, arg_types=arg_types, arg_names=arg_names)
 
axpy = Generator(
        targets = ["double", "float", "int32_t", "int64_t"],
        func = "axpy",
        returns = ["void", "void", "void", "void"],
        args = ["const {target}", "const {T}Vec", "{T}Vec"],
        )
