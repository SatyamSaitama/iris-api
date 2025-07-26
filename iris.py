import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load the Iris dataset
iris = load_iris()
feature_names = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
X = pd.DataFrame(iris.data, columns=feature_names)
y = pd.Series(iris.target)

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the model to a file using joblib
joblib.dump(model, 'model.joblib')
print("Model saved to 'iris_model.joblib'")

