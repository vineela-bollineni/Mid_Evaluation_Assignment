import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
data = pd.read_csv("cleaned_books_data.csv")
print(data.head())
label_encoder = LabelEncoder()
data['Category'] = label_encoder.fit_transform(data['Category'])
data['Rating'] = label_encoder.fit_transform(data['Rating'])
data = data.dropna()
X = data[['Category', 'Price']]
y = data['Rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
gb_model = GradientBoostingClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
gb_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)
gb_predictions = gb_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_predictions)
gb_accuracy = accuracy_score(y_test, gb_predictions)
print(f"Random Forest Accuracy: {rf_accuracy:.4f}")
print(f"Gradient Boosting Accuracy: {gb_accuracy:.4f}")
print("\nRandom Forest Classification Report:")
print(classification_report(y_test, rf_predictions))
print("\nGradient Boosting Classification Report:")
print(classification_report(y_test, gb_predictions))
rf_cm = confusion_matrix(y_test, rf_predictions)
gb_cm = confusion_matrix(y_test, gb_predictions)
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
sns.heatmap(rf_cm, annot=True, fmt='d', cmap='Blues', ax=ax[0])
ax[0].set_title('Random Forest Confusion Matrix')
ax[0].set_xlabel('Predicted')
ax[0].set_ylabel('True')
sns.heatmap(gb_cm, annot=True, fmt='d', cmap='Blues', ax=ax[1])
ax[1].set_title('Gradient Boosting Confusion Matrix')
ax[1].set_xlabel('Predicted')
ax[1].set_ylabel('True')
plt.show()
rf_importance = rf_model.feature_importances_
plt.figure(figsize=(6, 4))
plt.barh(X.columns, rf_importance, color='green')
plt.title('Feature Importance - Random Forest')
plt.xlabel('Importance')
plt.ylabel('Features')
plt.show()
