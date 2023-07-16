import pandas as pd
import os
import pathlib

filepath = pathlib.Path(__file__).parent.absolute()

# Read the data
df = pd.read_csv(os.path.join(filepath, "NYPL-menus", 'MenuItem.csv'))

print("Starting shape:", df.shape[0])

numeric_cols = ["id", "menu_page_id", "price",
                "high_price", "dish_id", "xpos", "ypos"]

# Convert to numeric
for col in numeric_cols:
    starting_shape = df.shape[0]
    df = df[pd.to_numeric(df[str(col)], errors="coerce").notnull() | df[str(col)].isnull()]
    print("Column:", col, "Number of rows affected:", starting_shape - df.shape[0], "Number of non-null:", df[col].notnull().sum())

# Drop duplicates and nulls
df = df.drop_duplicates()
print("After dropping duplicates:", df.shape[0])
# df = df.dropna()

print(df.head())
print("Ending shape:", df.shape[0])
# conversion need to apply to each column, print each column how many rows are affected.
# Save the data
df.to_csv(os.path.join(filepath, 'MenuItem_cleaned.csv'), index=False)
