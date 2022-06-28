import contextlib
import subprocess, sys, shutil


@contextlib.contextmanager
def read_and_formatting(filename1, filename2, filename3):
    file1 = open(filename1, 'a')
    file2 = open(filename2, 'a')
    file3 = open(filename3, 'a')
    yield file1, file2, file3

    # check clang-format command is installed?
    if shutil.which('clang-format') == None:
        print('clang-format is not found.')
        sys.exit(1)

    # file close and formatting.
    file1.close()
    err = subprocess.run(['clang-format', '-i', filename1])
    if err.returncode != 0:
        print('clang-format failed for ' + filename1)
        sys.exit(1)

    file2.close()
    err = subprocess.run(['clang-format', '-i', filename2])
    if err.returncode != 0:
        print('clang-format failed for ' + filename2)
        sys.exit(1)

    file3.close()
    err = subprocess.run(['clang-format', '-i', filename3])
    if err.returncode != 0:
        print('clang-format failed for ' + filename3)
        sys.exit(1)
