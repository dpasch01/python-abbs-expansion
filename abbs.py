import pickle

d = {}
with open("abbs.dic") as f:
    for line in f:
        line = line.rstrip()
        (key, val) = line.split(" ", 1)
        d[key] = val

with open('abbs.pickle', 'wb') as handle:
  pickle.dump(d, handle)
