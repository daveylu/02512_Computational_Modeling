import sys

# the following function is taken from:
# https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
# assists with opening files
def read_file(path):
    with open(path, "rt") as f:
        return f.read()

def model():
    return

def main():
    input_file = sys.argv[-1]
    input = read_file(input_file).splitlines()
    return