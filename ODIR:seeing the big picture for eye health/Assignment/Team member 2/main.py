import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np



data = pd.read_csv("House Price India.csv")

#univariate analysis on price 
variable = "Price"
mean = data[variable].mean()
median = data[variable].median()
mode = data[variable].mode().iloc[0]
std_dev = data[variable].std()
variance = data[variable].var()


plt.hist(data[variable], bins=50, alpha=0.5)
plt.axvline(x=mean, color='r', linestyle='--', label='Mean')
plt.axvline(x=median, color='g', linestyle='--', label='Median')
plt.axvline(x=mode, color='b', linestyle='--', label='Mode')
plt.xlabel(variable)
plt.ylabel("Frequency")
plt.legend()
plt.show()

#descriptive statistics
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard deviation:", std_dev)
print("Variance:", variance)

# bivariate analysis on Price and Living Area columns
x = data['living area']
y = data['Price']


plt.scatter(x, y)
plt.title('Living Area vs. Price')
plt.xlabel('Living Area')
plt.ylabel('Price')
plt.show()


corr = x.corr(y)
print('Correlation coefficient:', corr)

z = data['number of bedrooms']

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=z, cmap='cool')
ax.set_xlabel('Living Area')
ax.set_ylabel('Price')
ax.set_zlabel('Number of Bedrooms')
plt.show()

#missing values
data_subset = pd.concat([x, y, z], axis=1)
data_subset = data_subset.dropna()

#descriptive statistics 
print(data_subset.describe())


#missing values
data = data.apply(lambda col: np.where(np.random.rand(len(col)) < 0.1, np.nan, col))

report = pd.DataFrame({
    'Column name': data.columns,
    'Number of missing values': data.isnull().sum(),
    'Percentage of missing values (%)': round(data.isnull().sum() / len(data) * 100, 2)
})
print("\nReport for the dataset with missing values\n------------------")
print(report)



