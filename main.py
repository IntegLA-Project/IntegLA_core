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
with clib_gen.reading_incompletely(obj_dir+"axpy.c", obj_dir+"axpy_test.cpp", obj_dir+"blas.hpp" ) as f:
    clib_gen.generate(func = "axpy",
        targets = [("double", "void"), ("float", "void"), ("int32_t", "void"), ("int64_t", "void")],
        args = [("{target}", "{Val0}"), ("const {Vec}", "{Vec0}"), ("{Vec}", "{Vec1}")],
        )
