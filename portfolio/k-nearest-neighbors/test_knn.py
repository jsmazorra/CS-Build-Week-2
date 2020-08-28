from knn import Knn
from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Let's load the data, I will be using the wine quality dataset directly from sklearn.
wine = load_wine()
data = wine.data
target = wine.target

# In this test, I'll be comparing the performance of my knn algorithm with
# sklearn's own K-Neighbors Classifier.

# Split the data into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3)

# Sklearn-learn KNN Classifier
# Instantiate model
clf = KNeighborsClassifier(n_neighbors=10)

# Fit
clf.fit(X_train, y_train)

# Prediction
predict = clf.predict(X_test)
print("---SKLEARN---")
print("Prediction", predict)

# Accuracy Score
print(f"Sklearn's KNN classifier accuracy: {accuracy_score(y_test, predict)}")

# y_pred
y_pred = clf.predict([X_test[0]])
print("y_pred", y_pred)

# k_nearest_neighbors (build model)
# Instantiate model
classifier = Knn(n_neighbors=10)

# Fit
classifier.fit(X_train, y_train)

# Prediction
predict = classifier.predictor(X_test)
print("---BUILD MODEL---")
print("Prediction", predict)

# Accuracy Score
print(f"Build's k_nearest_neighbors model accuracy: {accuracy_score(y_test, predict)}")

# y_pred
y_pred = classifier.predictor([X_test[0]])
print("y_pred", y_pred)

# Neighbor index and euclidean distance
neighbors = classifier.dis_neighbors(X_test[0])
print("Neighbors and their corresponding euclidian distances", neighbors)