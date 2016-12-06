from tools import bucket
import sys

def main(im, size):
    lb = bucket.bt()
    return lb.resize("static/{0}".format(im), size)
im, size = sys.argv[1:]
print(main(im, int(size)))