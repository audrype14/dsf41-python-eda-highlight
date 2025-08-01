import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('sales_store_updated_allign_with_video.csv')
data.describe()

# Mengatasi missing value
for column in data.columns:
    if data[column].dtype == 'object':
        data[column].fillna(data[column].mode()[0], inplace=True)
    else:
        data[column].fillna(data[column].mean(), inplace=True)

data.isna().sum()
data.info()

print(data.isna().sum())
print(data.describe())

# Mengecek apakah ada duplicate di seluruh kolom
check_duplicate = data.duplicated().sum()

print(f"Jumlah data yang duplikat = {check_duplicate}")

data = data.drop_duplicates()

handle_duplicate = data.duplicated().sum()

print(f"Jumlah data yang duplikat = {handle_duplicate}")


sns.heatmap(data.corr(numeric_only = True), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

sns.pairplot(data[['customer_age', 'quantiy', 'prce']])
plt.suptitle('Pairplot: Age, Quantity, and Price', y=1.02)
plt.show()