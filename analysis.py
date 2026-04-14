import pandas as pd
import matplotlib.pyplot as plt

print("DSA210 milestone 1 started")

# Load dataset (dosya adını kontrol et!)
df = pd.read_csv("dataset.csv")

print("Initial data analysis started")

# ======================
# DATA CLEANING
# ======================
df = df.dropna()

# ======================
# BASIC INFO
# ======================
print(df.head())
print(df.describe())

# ======================
# GRAPH 1 — DISTRIBUTION
# ======================
plt.figure()
df["popularity"].hist()
plt.title("Distribution of Track Popularity")
plt.xlabel("Popularity")
plt.ylabel("Frequency")
plt.show()

# ======================
# GRAPH 2 — ENERGY vs POPULARITY
# ======================
plt.figure()
plt.scatter(df["energy"], df["popularity"])
plt.xlabel("Energy")
plt.ylabel("Popularity")
plt.title("Energy vs Popularity")
plt.show()

# ======================
# GRAPH 3 — TEMPO vs POPULARITY
# ======================
plt.figure()
plt.scatter(df["tempo"], df["popularity"])
plt.xlabel("Tempo")
plt.ylabel("Popularity")
plt.title("Tempo vs Popularity")
plt.show()

# ======================
# BONUS — CORRELATION MATRIX
# ======================
corr = df.corr(numeric_only=True)

plt.figure()
plt.imshow(corr)
plt.title("Correlation Matrix")
plt.colorbar()
plt.show()
