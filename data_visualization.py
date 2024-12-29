import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
file_path = 'books_data.csv'
data = pd.read_csv(file_path)
if data.shape[1] == 1:
    data_split = data.iloc[:, 0].str.split(r"\t+", expand=True)
    data_split.columns = ['Category', 'Book Name', 'Rating', 'Price']
else:
    data_split = data

data_cleaned = data_split.apply(lambda x: x.str.strip())
data_cleaned['Price'] = data_cleaned['Price'].str.replace(r'[Â£$€]', '', regex=True).astype(float)
print("\nCleaned data preview:")
print(data_cleaned.head())
cleaned_file_path = 'cleaned_books_data.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)
print(f"Cleaned data saved to {cleaned_file_path}")
sns.countplot(x='Category', data=data_cleaned)
plt.title('Number of Books in Each Category')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
sns.histplot(data_cleaned['Price'], kde=True)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()
sns.countplot(x='Rating', data=data_cleaned)
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()
sns.scatterplot(x='Rating', y='Price', data=data_cleaned)
plt.title('Price vs. Rating')
plt.xlabel('Rating')
plt.ylabel('Price')
plt.show()
sns.boxplot(x='Category', y='Price', data=data_cleaned)
plt.title('Price Distribution by Category')
plt.xlabel('Category')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.show()
