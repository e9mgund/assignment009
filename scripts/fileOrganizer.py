import os


def fileOrganizer(dirpath):
    filetypes = []

    for path,dir,files in os.walk(dirpath):
        for file in files:
            type = os.path.abspath(file).split(".")[-1]
            if type not in filetypes and "/" not in type:
                filetypes.append(type)
                os.mkdir(os.path.join(os.path.abspath('results'),type))
            os.rename(os.path.abspath(file),os.path.abspath(type))
    print(os.walk(dirpath)) #to show directory structure





fileOrganizer('/home/kilo/repo/assignment_repos/assignment009') #As as an example

print(os.path.abspath('results'))