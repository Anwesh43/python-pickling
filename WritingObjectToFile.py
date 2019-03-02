from constants import FILE_NAME
import pickle
data = {"a" : 1, "b" : 2, "c" : 3}
with open(FILE_NAME, "wb") as f:
    pickle.dump(data, f)
print("written to file")
