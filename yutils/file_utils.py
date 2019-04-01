import json
from .str_utils import str_to_list, list_to_str


#############################################################
###################
#   Read and write files
###################
# contents is a list of Strings
def write_list2file(contents, filename):
    s = ''
    for i in contents:
        s += (str(i) + "\n")
    with open(filename, 'wb') as f:
        f.write(s.encode())
    print("********** Write to %s Successfully" % filename)


def write_lol2file(contents, filename):
    s = ''
    for i in contents:
        s += (str(list_to_str(i)) + "\n")
    with open(filename, 'wb') as f:
        f.write(s.encode())
    print("********** Write to %s Successfully" % filename)


# read raw text into list (sentence in strings)
def read_file2list(filename):
    with open(filename, 'rb') as f:
        contents = [line.strip().decode() for line in f]
    print("The %s has lines: %d" % (filename, len(contents)))
    return contents


# read segmented corpus into list (sentence in list of words)
def read_file2lol(filename):
    with open(filename, 'rb') as f:
        contents = [str_to_list(line.strip().decode()) for line in f]
    print("The %s has lines: %d" % (filename, len(contents)))
    return contents


#############################################################

###################
#   Serialization to pickle
###################
def data_to_pickle(your_dict, out_file):
    try:
        import cPickle as pickle
    except ImportError:
        import pickle
    with open(out_file, 'wb') as f:
        pickle.dump(your_dict, f)


def pickle_to_data(in_file):
    try:
        import cPickle as pickle
    except ImportError:
        import pickle
    with open(in_file, 'rb') as f:
        your_dict = pickle.load(f)
        return your_dict


if __name__ == "__main__":
    print("------------This is for utility test--------------")

