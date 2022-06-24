import sys
import os
import shutil
from clib_gen import clib_gen

obj_dir="./obj/"
if(os.path.isdir(obj_dir) == True):
    shutil.rmtree(obj_dir)
os.mkdir(obj_dir)
# setup_dir(objdir)
 
with clib_gen.reading_incompletely(obj_dir+"axpy.c", obj_dir+"axpy_test.cpp", obj_dir+"blas.hpp" ) as f:
    clib_gen.generate(func = "axpy",
        targets = [("double", "void"), ("float", "void"), ("int32_t", "void"), ("int64_t", "void")],
        args = [("{target}", "{Val0}"), ("const {Vec}", "{Vec0}"), ("{Vec}", "{Vec1}")],
        ) # 追記でOK

# srcfp=fopen("axpy.c")
# testfp=fopen("axpy_test.c")
# hppfp=fopen("axpy.hpp")
#         src=fp_src,  # func or type
#         test=testfp, 
#         header=hppfp
#         header=fp
# 
#         code = '''
#                 for(Integer i=0; i<{Vec[0]}.size; i++){
#                     {Vec[0]}[i] += {Val[0]} * {Vec[0]};
#                 }
#             '''
#          src="src/{{func}}.c",  # func or type
#          test="test/test.c", 
#          header="include/blas.h" 
# Goal:
# '''
# 
# 
# @dataclass()
# class ARGS:
#     name: str
#     Ctype: str
#     const: True
#     number: 3
# 
# ARGS_list.append(ARGS(targets, args))
# 
# 
# S = ["alpha", "beta", "gamma"]
# Vec = ["x", "y", "z"]
# matrix_name = ["A", "B", "C"]
# type_names = {"double":"f64Vec", "float": "f32Vec", "int32_t": "i32Vec", "int64_t": "i64Vec"}
# 
# 
# 
# for goma in targets:
#     print(goma[0], goma[1])
# for goma,gomo in targets:
#     print(goma, gomo)
# 
# 
# class Generator():
#     # create args -> ["alpha":"const double", "x": "coust f64Vec"...]
# 
#     def generate_arg_types(self, args, target):
#         arg_types = list()
#         vec_count = 0
#         mat_count = 0
#         val_count = 0
#         for i in range(len(args)):
#             arg_types.append(args[i].format(target=target, T=type_names[target]))
#         print(arg_types)
#         return arg_types
# 
#     def parse_func_def(self, target, ret, func, arg_types, arg_names):
#         func = target + " " + func + "("
#         for j in range(len(arg_types)):
#             func += arg_types[j] + " " + arg_names[j]
#             if(j == len(arg_types)-1):
#                 func += ")"
#             else:
#                 func += ", "
#         print(func)
# 
#     def generate():
#         for i in range(len(targets)):
#             function=function_def(target=targets[i],func=func, args=args, ret=returns[i])
#             print(function.arg_num)
#             print(function.type)
#             print(function.name)
#             print(function.prototype)
# 
#     def generate_arg_list(self, args):
#         arg_names = list()
#         vec_count = 0
#         mat_count = 0
#         val_count = 0
#         for arg in args:
#             if ("{target}" in arg):
#                 arg_names.append(val_names[val_count])
#                 val_count += 1
#             elif ("Vec" in arg):
#                 arg_names.append(vec_names[vec_count])
#                 vec_count += 1
#             elif ("Mat" in arg):
#                 arg_names.append(mat_names[mat_count])
#                 mat_count += 1
#         return arg_names
