import numpy as np
from sklearn import preprocessing
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = load_breast_cancer()
print("\t".join(df.feature_names)+"\tmalignant")
for i in range(df.data.shape[0]):
    print("\t".join(["{0:10.6f}".format(x) for x in df.data[i]])+"\t"+str(df.target[i]))
