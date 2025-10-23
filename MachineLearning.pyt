from sklearn.datasets import load_iris
iris = load_iris()
print(iris.feature_names)
print(iris.target_names)
print(iris.target[2]) 
for i in range(len(iris.target)):
  print(f"Ex {i} : Label {(iris.target[i])+1} : Feature {iris.data[i]}")