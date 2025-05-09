# -*- coding: utf-8 -*-
"""Copy of risk analysis code

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tE4EBNIKef8cMFuXlUPx_-LUn88CiLmE
"""



"""SVM"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Generate a synthetic dataset with supply chain risk factors
np.random.seed(42)

# Simulating 1000 data points
n_samples = 1000

# Features (risk factors)
data = pd.DataFrame({
    'defect_rate': np.random.uniform(0, 0.2, n_samples),   # Defect rate between 0 and 20%
    'lead_time': np.random.uniform(5, 30, n_samples),      # Lead time between 5 and 30 days
    'route_optimization': np.random.uniform(0.5, 1.0, n_samples),  # Route optimization (scale of 0.5 to 1.0)
    'demand_variation': np.random.uniform(0.1, 0.5, n_samples),   # Demand variation between 0.1 and 0.5
    'supplier_reliability': np.random.uniform(0.6, 1.0, n_samples),  # Supplier reliability between 0.6 and 1.0
    'inventory_levels': np.random.uniform(100, 1000, n_samples),  # Inventory levels
    'order_fulfillment_accuracy': np.random.uniform(0.7, 1.0, n_samples),  # Accuracy of fulfilled orders
    'production_downtime': np.random.uniform(0, 5, n_samples),   # Downtime in hours
    'financial_risk': np.random.uniform(0, 1, n_samples),   # Financial risk on a scale of 0 to 1
    'environmental_impact': np.random.uniform(0, 1, n_samples)   # Environmental impact risk factor
})

# Target (risk classification: 0 = Low, 1 = Medium, 2 = High)
# For simplicity, we'll create an artificial relationship between risk factors and risk level
conditions = [
    (data['defect_rate'] > 0.1) | (data['lead_time'] > 20) | (data['demand_variation'] > 0.4),
    (data['route_optimization'] < 0.6) | (data['supplier_reliability'] < 0.7),
    (data['financial_risk'] > 0.8) | (data['environmental_impact'] > 0.7)
]
choices = [2, 1, 0]  # High risk, Medium risk, Low risk
data['risk_level'] = np.select(conditions, choices, default=0)

# Step 2: Preprocess the data
X = data.drop(columns=['risk_level'])  # Features
y = data['risk_level']  # Target

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Step 3: Train the SVM model
svm_model = SVC(kernel='rbf', C=1, gamma='auto')
svm_model.fit(X_train, y_train)

# Step 4: Make predictions on the test set
y_pred = svm_model.predict(X_test)

# Step 5: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.show()

"""KNN

"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Generate a synthetic dataset with supply chain risk factors
np.random.seed(42)

n_samples = 1000

# Simulating risk factors
data = pd.DataFrame({
    'defect_rate': np.random.uniform(0, 0.2, n_samples),   # Defect rate between 0 and 20%
    'lead_time': np.random.uniform(5, 30, n_samples),      # Lead time between 5 and 30 days
    'route_optimization': np.random.uniform(0.5, 1.0, n_samples),  # Route optimization (scale of 0.5 to 1.0)
    'demand_variation': np.random.uniform(0.1, 0.5, n_samples),   # Demand variation between 0.1 and 0.5
    'supplier_reliability': np.random.uniform(0.6, 1.0, n_samples),  # Supplier reliability between 0.6 and 1.0
    'inventory_levels': np.random.uniform(100, 1000, n_samples),  # Inventory levels
    'order_fulfillment_accuracy': np.random.uniform(0.7, 1.0, n_samples),  # Accuracy of fulfilled orders
    'production_downtime': np.random.uniform(0, 5, n_samples),   # Downtime in hours
    'financial_risk': np.random.uniform(0, 1, n_samples),   # Financial risk on a scale of 0 to 1
    'environmental_impact': np.random.uniform(0, 1, n_samples)   # Environmental impact risk factor
})

# Target risk classification: 0 = Low, 1 = Medium, 2 = High
conditions = [
    (data['defect_rate'] > 0.1) | (data['lead_time'] > 20) | (data['demand_variation'] > 0.4),
    (data['route_optimization'] < 0.6) | (data['supplier_reliability'] < 0.7),
    (data['financial_risk'] > 0.8) | (data['environmental_impact'] > 0.7)
]
choices = [2, 1, 0]  # High risk, Medium risk, Low risk
data['risk_level'] = np.select(conditions, choices, default=0)

# Step 2: Preprocess the data
X = data.drop(columns=['risk_level'])  # Features
y = data['risk_level']  # Target

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Step 3: Train the KNN model
knn_model = KNeighborsClassifier(n_neighbors=5)  # Using 5 neighbors
knn_model.fit(X_train, y_train)

# Step 4: Make predictions on the test set
y_pred = knn_model.predict(X_test)

# Step 5: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.show()

"""ensemble learning model knn + svm

"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Generate a synthetic dataset with supply chain risk factors
np.random.seed(42)

n_samples = 1000

# Simulating risk factors
data = pd.DataFrame({
    'defect_rate': np.random.uniform(0, 0.2, n_samples),   # Defect rate between 0 and 20%
    'lead_time': np.random.uniform(5, 30, n_samples),      # Lead time between 5 and 30 days
    'route_optimization': np.random.uniform(0.5, 1.0, n_samples),  # Route optimization (scale of 0.5 to 1.0)
    'demand_variation': np.random.uniform(0.1, 0.5, n_samples),   # Demand variation between 0.1 and 0.5
    'supplier_reliability': np.random.uniform(0.6, 1.0, n_samples),  # Supplier reliability between 0.6 and 1.0
    'inventory_levels': np.random.uniform(100, 1000, n_samples),  # Inventory levels
    'order_fulfillment_accuracy': np.random.uniform(0.7, 1.0, n_samples),  # Accuracy of fulfilled orders
    'production_downtime': np.random.uniform(0, 5, n_samples),   # Downtime in hours
    'financial_risk': np.random.uniform(0, 1, n_samples),   # Financial risk on a scale of 0 to 1
    'environmental_impact': np.random.uniform(0, 1, n_samples)   # Environmental impact risk factor
})

# Target risk classification: 0 = Low, 1 = Medium, 2 = High
conditions = [
    (data['defect_rate'] > 0.1) | (data['lead_time'] > 20) | (data['demand_variation'] > 0.4),
    (data['route_optimization'] < 0.6) | (data['supplier_reliability'] < 0.7),
    (data['financial_risk'] > 0.8) | (data['environmental_impact'] > 0.7)
]
choices = [2, 1, 0]  # High risk, Medium risk, Low risk
data['risk_level'] = np.select(conditions, choices, default=0)

# Step 2: Preprocess the data
X = data.drop(columns=['risk_level'])  # Features
y = data['risk_level']  # Target

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Step 3: Define individual models (SVM and KNN)
svm_model = SVC(kernel='rbf', C=1, gamma='auto', probability=True)  # Enable probability estimates for voting
knn_model = KNeighborsClassifier(n_neighbors=5)

# Step 4: Create an ensemble model using VotingClassifier
# We use 'hard' voting for classification, meaning the models will vote based on their predicted classes.
ensemble_model = VotingClassifier(estimators=[
    ('svm', svm_model),
    ('knn', knn_model)
], voting='soft')  # Soft voting averages the predicted probabilities

# Train the ensemble model
ensemble_model.fit(X_train, y_train)

# Step 5: Make predictions on the test set
y_pred = ensemble_model.predict(X_test)

# Step 6: Evaluate the ensemble model
accuracy = accuracy_score(y_test, y_pred)
print(f"Ensemble Model Accuracy: {accuracy * 100:.2f}%")

# Classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.show()



"""ransdom forest

"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Generate a synthetic dataset with supply chain risk factors
np.random.seed(42)

n_samples = 1000

# Simulating risk factors
data = pd.DataFrame({
    'defect_rate': np.random.uniform(0, 0.2, n_samples),   # Defect rate between 0 and 20%
    'lead_time': np.random.uniform(5, 30, n_samples),      # Lead time between 5 and 30 days
    'route_optimization': np.random.uniform(0.5, 1.0, n_samples),  # Route optimization (scale of 0.5 to 1.0)
    'demand_variation': np.random.uniform(0.1, 0.5, n_samples),   # Demand variation between 0.1 and 0.5
    'supplier_reliability': np.random.uniform(0.6, 1.0, n_samples),  # Supplier reliability between 0.6 and 1.0
    'inventory_levels': np.random.uniform(100, 1000, n_samples),  # Inventory levels
    'order_fulfillment_accuracy': np.random.uniform(0.7, 1.0, n_samples),  # Accuracy of fulfilled orders
    'production_downtime': np.random.uniform(0, 5, n_samples),   # Downtime in hours
    'financial_risk': np.random.uniform(0, 1, n_samples),   # Financial risk on a scale of 0 to 1
    'environmental_impact': np.random.uniform(0, 1, n_samples)   # Environmental impact risk factor
})

# Target risk classification: 0 = Low, 1 = Medium, 2 = High
conditions = [
    (data['defect_rate'] > 0.1) | (data['lead_time'] > 20) | (data['demand_variation'] > 0.4),
    (data['route_optimization'] < 0.6) | (data['supplier_reliability'] < 0.7),
    (data['financial_risk'] > 0.8) | (data['environmental_impact'] > 0.7)
]
choices = [2, 1, 0]  # High risk, Medium risk, Low risk
data['risk_level'] = np.select(conditions, choices, default=0)

# Step 2: Preprocess the data
X = data.drop(columns=['risk_level'])  # Features
y = data['risk_level']  # Target

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Step 3: Train the Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Step 4: Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Step 5: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Random Forest Model Accuracy: {accuracy * 100:.2f}%")

# Classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Step 1: Load historical delay data (generate synthetic data for example)
# Replace this with your actual delay data
date_rng = pd.date_range(start='2015-01-01', end='2023-01-01', freq='MS')
np.random.seed(42)
delays_data = np.random.poisson(lam=4, size=(len(date_rng))) + np.random.binomial(10, 0.1, size=(len(date_rng)))  # Simulate delays data
df = pd.DataFrame(date_rng, columns=['Date'])
df['Delays'] = delays_data
df.set_index('Date', inplace=True)

# Step 2: Split the data into training and test sets
train_size = int(len(df) * 0.8)  # Use 80% for training and 20% for testing
train, test = df[:train_size], df[train_size:]

# Step 3: Fit an ARIMA model on the training data
p, d, q = 1, 1, 1  # ARIMA model parameters, typically determined by prior analysis
model = ARIMA(train['Delays'], order=(p, d, q))
fitted_model = model.fit()

# Step 4: Make predictions on the test set
start = test.index[0]
end = test.index[-1]
predictions = fitted_model.predict(start=start, end=end, typ='levels')

# Step 5: Calculate Mean Squared Error for evaluation
mse = mean_squared_error(test['Delays'], predictions)
print(f'Mean Squared Error on Test Set: {mse}')

# Step 6: Visualize the actual vs predicted delays
plt.figure(figsize=(10, 6))
plt.plot(train['Delays'], label='Training Data', color='blue')
plt.plot(test['Delays'], label='Actual Delays', color='orange')
plt.plot(predictions, label='Predicted Delays', color='green', linestyle='--')
plt.title('ARIMA Model - Actual vs Predicted Shipment Delays')
plt.xlabel('Date')
plt.ylabel('Number of Delays')
plt.legend()
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import cross_val_score, KFold
from sklearn.svm import SVC

# Step 1: Load a dataset (e.g., Iris dataset)
# Replace this with your actual data
data = datasets.load_iris()
X = data.data
y = data.target

# Step 2: Initialize the SVM model
svm_model = SVC(kernel='linear')

# Step 3: Perform cross-validation
# Using K-Fold Cross-Validation with 5 folds
kf = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(svm_model, X, y, cv=kf, scoring='accuracy')

# Step 4: Plot the cross-validation scores
plt.figure(figsize=(8, 6))
plt.bar(range(1, len(cv_scores) + 1), cv_scores, color='steelblue')
plt.title('Cross-Validation Scores for SVM Model')
plt.xlabel('Cross-Validation Folds')
plt.ylabel('Accuracy')
plt.ylim(0.90, 1.00)  # Set y-axis limits based on typical accuracy range for better visualization
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from sklearn.metrics import RocCurveDisplay

# Step 1: Load and preprocess data
# Using Iris dataset, but only two classes for binary classification
data = datasets.load_iris()
X = data.data
y = data.target
# Binarize the target variable to make it binary (e.g., classify between class 0 and class 1)
y = label_binarize(y, classes=[0, 1, 2])[:, 0]

# Step 2: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Train an SVM model
svm_model = SVC(kernel='linear', probability=True)
svm_model.fit(X_train, y_train)

# Step 4: Predict probabilities on the test set
y_proba = svm_model.predict_proba(X_test)[:, 1]

# Step 5: Compute ROC curve and AUC score
fpr, tpr, _ = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)

# Step 6: Plot ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='black', linestyle='--')  # Diagonal line
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc='lower right')
plt.show()