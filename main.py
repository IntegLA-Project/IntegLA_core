import sys
import os
import shutil
from clib_gen import clib_gen, clib_gen_io

# setup dir
obj_dir = "./obj/"
if (os.path.isdir(obj_dir) == True):
    shutil.rmtree(obj_dir)
os.mkdir(obj_dir)

# BLAS Lv1 gen
with clib_gen_io.read_and_formatting(obj_dir + "axpy.c",
                                     obj_dir + "axpy_test.cpp",
                                     obj_dir + "blas.hpp") as (src, test,
                                                               header):
    clib_gen.generate(name="axpy",
                      group="blas",
                      targets=[("double", "void"), ("float", "void"),
                               ("int32_t", "void"), ("int64_t", "void")],
                      args=[("const {target}", "{Val0}"), ("const {Vec}&", "{Vec0}"),
                            ("{Vec}&", "{Vec1}")],
                      operation='''
                      {omp_directive}
                      for( {INT} i = 0; i < {Vec0}.size; i++){{
                          {Vec1}[i] += {Val0} * {Vec0}[i];
                      }}
                      ''',
                      src_file=src,
                      test_file=test,
                      header_file=header)

with clib_gen_io.read_and_formatting(obj_dir + "dot.c",
                                     obj_dir + "dot_test.cpp",
                                     obj_dir + "blas.hpp") as (src, test,
                                                               header):
    clib_gen.generate(name="dot",
                      group="blas",
                      targets=[("double", "double"), ("float", "float"),
                               ("int32_t", "int32_t"), ("int64_t", "int64_t")],
                      args=[("const {Vec}&", "{Vec0}"), ("const {Vec}&", "{Vec1}")],
                      omp_option="reduction(+:{RET})",
                      operation='''
                      {target_ret} {RET};

                      {omp_directive}
                      for( {INT} i = 0; i < {Vec0}.size; i++){{
                          {RET} += {Vec0}[i] * {Vec1}[i];
                      }}
                      ''',
                      src_file=src,
                      test_file=test,
                      header_file=header)
