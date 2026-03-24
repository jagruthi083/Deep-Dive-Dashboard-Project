import pandas as pd
import numpy as np
import os

# Set seed for reproducibility
np.random.seed(42)

# Number of records
n = 1000

# Generate dataset
data = pd.DataFrame({
    "customer_id": np.arange(1, n + 1),
    
    "signup_date": pd.date_range(
        start="2023-01-01",
        periods=n,
        freq="D"
    ),
    
    "region": np.random.choice(
        ["North", "South", "East", "West"], n
    ),
    
    "product_category": np.random.choice(
        ["Electronics", "Clothing", "Home", "Beauty"], n
    ),
    
    "orders": np.random.randint(1, 10, n),
    
    "revenue": np.random.randint(100, 5000, n),
    
    "churned": np.random.choice(
        [0, 1], n, p=[0.7, 0.3]
    )
})

# Create folder if not exists
os.makedirs("../data", exist_ok=True)

# Save CSV
data.to_csv("../data/data.csv", index=False)

print("data.csv file created successfully!")
