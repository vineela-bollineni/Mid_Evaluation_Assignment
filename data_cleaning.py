import pandas as pd
file_path = 'books_data.csv'
data = pd.read_csv(file_path)
print("Raw data preview:")
print(data.head())
if data.shape[1] == 1:
    data_split = data.iloc[:, 0].str.split(r"\t+", expand=True)
else:
    data_split = data
print("\nAfter splitting columns:")
print(data_split.head())
if data_split.shape[1] >= 4:  #
    data_split.columns = ['Category', 'Book Name', 'Rating', 'Price']
else:
    raise ValueError("The dataset could not be split into the expected number of columns.")

data_cleaned = data_split.apply(lambda x: x.str.strip())
data_cleaned['Price'] = data_cleaned['Price'].str.replace('Â£', '').astype(float)
data_cleaned['Rating'] = data_cleaned['Rating'].astype(int)
data_cleaned = data_cleaned.dropna()
cleaned_file_path = 'cleaned_books_data.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)
print(f"Cleaned data saved to {cleaned_file_path}")
