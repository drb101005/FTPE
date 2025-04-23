import pandas as pd
import matplotlib.pyplot as plt

# Load and process Iris dataset
df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
print("First 8 rows:\n", df.head(8), "\n\nColumns:", df.columns.tolist())

# Handle missing data
df_filled, df_cleaned = df.fillna(df.mean(numeric_only=True)), df.dropna()
print("\nFilled data:\n", df_filled, "\n\nCleaned data:\n", df_cleaned)

# Group and analyze data
print("\nGrouped by species:")
for s, g in df_cleaned.groupby('species'):
    print(f"\n{s}:\n", g)

stats = df_cleaned['sepal_length'].agg(['mean', 'min', 'max'])
print("\nSepal length stats:\n", stats.round(2))

# Visualization
plt.hist(df_cleaned['sepal_length'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Length'); plt.xlabel('Sepal Length (cm)'); plt.ylabel('Frequency'); plt.grid(True)
plt.show()