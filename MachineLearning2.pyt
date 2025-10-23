import numpy as np
from sklearn.datasets import load_iris
from sklearn  import tree
import matplotlib.pyplot as plt
iris = load_iris()
test_idx = [0,50,100]
train_target = np.delete(iris.target,test_idx)
train_data = np.delete(iris.data,test_idx,axis= 0)

test_target = iris.target[test_idx]
test_data = iris.target[test_idx]
clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)
tree.plot_tree(clf.fit(train_data,train_target))
plt.show()
