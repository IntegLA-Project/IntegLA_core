import sys
import os
import shutil
from clib_gen import clib_gen

# setup dir
obj_dir="./obj/"
if(os.path.isdir(obj_dir) == True):
    shutil.rmtree(obj_dir)
os.mkdir(obj_dir)
 
# BLAS Lv1 gen
with clib_gen.read_and_formatting(obj_dir+"axpy.c", obj_dir+"axpy_test.cpp", obj_dir+"blas.hpp" ) as (src,test,header):
    clib_gen.generate(func = "axpy",
        targets = [("double", "void"), ("float", "void"), ("int32_t", "void"), ("int64_t", "void")],
        args = [("{target}", "{Val0}"), ("const {Vec}", "{Vec0}"), ("{Vec}", "{Vec1}")],
        src_file=src,
        test_file=test,
        header_file=header
        )

with clib_gen.read_and_formatting(obj_dir+"dot.c", obj_dir+"dot_test.cpp", obj_dir+"blas.hpp" ) as (src,test,header):
    clib_gen.generate(func = "dot",
        targets = [("double", "double"), ("float", "float"), ("int32_t", "int32_t"), ("int64_t", "int64_t")],
        args = [("const {Vec}", "{Vec0}"), ("{Vec}", "{Vec1}")],
        src_file=src,
        test_file=test,
        header_file=header
        )
