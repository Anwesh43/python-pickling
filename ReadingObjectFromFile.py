import pickle
from constants import FILE_NAME
with open(FILE_NAME, "rb") as f:
    data = pickle.load(f)
    print(type(data))
    for k,v in data.items():
        print("{0}:{1}".format(k, v))
