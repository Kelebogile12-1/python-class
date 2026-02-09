import pandas as pd

# Read the file line by line
with open("mytelevision.csv", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

df = pd.DataFrame(lines, columns=["raw"])

# Extract the price at the end of the line
df["price"] = df["raw"].str.extract(r"-R\s*([\d,]+)$")

# Remove rows where price extraction failed
df = df.dropna(subset=["price"])

# Clean price (remove commas and convert to int)
df["price"] = df["price"].str.replace(",", "").astype(int)

# Extract product name (everything before '-R <price>')
df["product"] = df["raw"].str.replace(r"-R\s*[\d,]+$", "", regex=True).str.strip()

# Reorder columns
df = df[["product", "price"]]

# Save back to CSV with semicolon delimiter
df.to_csv("mytelevision.csv", index=False, sep=";")

print("✔ File cleaned and saved with semicolon delimiter!")








