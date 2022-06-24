import contextlib

TYPE_NAMES = {"double":"f64Vec", "float": "f32Vec", "int32_t": "i32Vec", "int64_t": "i64Vec"}
convert_list={"Vec0":"x", "Vec1":"y", "Vec2":"z",
              "Val0":"alpha", "Val1":"beta", "Val2":"gamma"}

@contextlib.contextmanager
def reading_incompletely(filename1, filename2, filename3):
  file1 = open(filename1, 'w')
  file2 = open(filename2, 'w')
  file3 = open(filename3, 'w')
  yield file1, file2, file3
  #TODO clang-format
  file1.close()
  file2.close()
  file3.close()

class arg_type():
    def __init__(self,
    target,
    ret,
    arg,
    ):
        self.target=target
        self.type = arg[0].format(**convert_list,target=target, Vec=TYPE_NAMES[target])
        self.name = arg[1].format(**convert_list,target=target, Vec=TYPE_NAMES[target])

def generate(
        func,
        targets,
        args
        ):
    main = "#include<stdio.h>\n"
    for target, ret in targets:

        # create prototype
        arg_list=list()
        for arg in args:
            arg_list.append(arg_type(target=target, arg=arg, ret=ret))

        main += ret + " " + func + "("
        main += ", ".join([arg.type + " " + arg.name for arg in arg_list]) + ")"
        print(main)
        main=""
