# Task 3: Linear Regression (Simple & Multiple)
# Easy version

# 1. Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 2. Load dataset
# You can download a simple House Price dataset or use any CSV
df = pd.read_csv(r"C:\Users\Admin\Desktop\del1\Housing.csv")  # replace with your dataset path

# Preview dataset
print(df.head())

# 3. Select features and target
# For simple linear regression, use one feature: "SqFt"
X = df[["area"]]  # independent variable
y = df["price"]   # dependent variable

# For multiple regression, you can use more features, e.g.,
# X = df[["SqFt", "Bedrooms", "Bathrooms"]]

# 4. Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Create and train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Predict on test data
y_pred = model.predict(X_test)

# 7. Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE:", mae)
print("MSE:", mse)
print("R² Score:", r2)

# 8. Coefficients
print("\nIntercept:", model.intercept_)
print("Coefficient(s):", model.coef_)

# 9. Plot regression line (for simple linear regression)
plt.scatter(X_test, y_test, color="blue", label="Actual")
plt.plot(X_test, y_pred, color="red", label="Regression Line")
plt.xlabel("Square Feet")
plt.ylabel("House price")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()