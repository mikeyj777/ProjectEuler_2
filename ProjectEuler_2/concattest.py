import numpy as np

# lister = []
# lister.append([1, 2])
# nparr = np.array(lister)
# nparr = np.concatenate((nparr, [[3, 4]]), axis=0)
# print(nparr)


count = np.array([[1, 2], [3, 4]])
rownum = (count[:, 0] == [3]).nonzero()
row = count[rownum]
print(row)
