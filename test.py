import pandas as pd
from sklearn.model_selection import GroupKFold
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib
import pickle

# Load data
data = pd.read_csv("template/features/features_training.csv")

# Create binary label indicating cancerous or not
data["cancerous"] = data["diagnostic"].isin(["MEL", "SCC", "BCC"])
# Remove unnecessary colum
features = data.drop(columns=["patient_id", "diagnostic", "cancerous"])
target = data["cancerous"]


# Define cross-validation strategy based on patient_id
group_kfold = GroupKFold(n_splits=5)

# Initialize logistic regression model
model = LogisticRegression(max_iter=1000000)

# Perform cross-validation
accuracies = []
for train_index, test_index in group_kfold.split(features, target, data["patient_id"]):
    X_train, X_test = features.iloc[train_index], features.iloc[test_index]
    y_train, y_test = target.iloc[train_index], target.iloc[test_index]

    # Train the model
    model.fit(X_train, y_train)

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

# Calculate average accuracy
average_accuracy = sum(accuracies) / len(accuracies)
print("Average Accuracy:", average_accuracy)

# Save the trained classifier using pickle with .sav file extension
with open("logistic_regression_classifier.sav", "wb") as file:
    pickle.dump(model, file)
