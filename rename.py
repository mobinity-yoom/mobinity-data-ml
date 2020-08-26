import os

def rename(path, name):
    idx = 0
    for filename in os.listdir(path):
        print(path + filename, '=>', path + str(name) + '_' + str(idx) + '.jpeg')
        os.rename(path + filename, path + str(name) + '_' + str(idx) + '.jpg')
        idx += 1

rename('./instrument/', 'instrument')