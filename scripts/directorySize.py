import os



def dirsize(dirpath):
    dir_sizes = {}
    for r, d, f in os.walk(dirpath, False):
        size = sum(os.path.getsize(os.path.join(r,f)) for f in f+d)
        size += sum(dir_sizes[os.path.join(r,d)] for d in d)
        dir_sizes[r] = size
        print("{} is {} MB".format(r, size/2**20))


print(dirsize('/home/kilo/repo/assignment_repos/assignment009'))