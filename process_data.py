import pandas as pd

# 1. Load the data file

print("Loading dataset...")
df = pd.read_csv("Nassau Candy Distributor.csv")

factory_mapping = {
    "Wonka Bar - Nutty Crunch Surprise": {"Factory": "Lot's O' Nuts", "Lat": 32.881893, "Lon": -111.768036},
    "Wonka Bar - Fudge Mallows": {"Factory": "Lot's O' Nuts", "Lat": 32.881893, "Lon": -111.768036},
    "Wonka Bar -Scrumdiddlyumptious": {"Factory": "Lot's O' Nuts", "Lat": 32.881893, "Lon": -111.768036},
    "Wonka Bar - Milk Chocolate": {"Factory": "Wicked Choccy's", "Lat": 32.076176, "Lon": -81.088371},
    "Wonka Bar - Triple Dazzle Caramel": {"Factory": "Wicked Choccy's", "Lat": 32.076176, "Lon": -81.088371},
    "Laffy Taffy": {"Factory": "Sugar Shack", "Lat": 48.11914, "Lon": -96.18115},
    "SweeTARTS": {"Factory": "Sugar Shack", "Lat": 48.11914, "Lon": -96.18115},
    "Nerds": {"Factory": "Sugar Shack", "Lat": 48.11914, "Lon": -96.18115},
    "Fun Dip": {"Factory": "Sugar Shack", "Lat": 48.11914, "Lon": -96.18115},
    "Fizzy Lifting Drinks": {"Factory": "Sugar Shack", "Lat": 48.11914, "Lon": -96.18115},
    "Everlasting Gobstopper": {"Factory": "Secret Factory", "Lat": 41.446333, "Lon": -90.565487},
    "Lickable Wallpaper": {"Factory": "Secret Factory", "Lat": 41.446333, "Lon": -90.565487},
    "Wonka Gum": {"Factory": "Secret Factory", "Lat": 41.446333, "Lon": -90.565487},
    "Hair Toffee": {"Factory": "The Other Factory", "Lat": 35.1175, "Lon": -89.971107},
    "Kazookles": {"Factory": "The Other Factory", "Lat": 35.1175, "Lon": -89.971107}
}

print(" Mapping products to factories...")
df['Factory'] = df['Product Name'].map(lambda x: factory_mapping.get(x, {}).get('Factory', 'Unknown'))
df['Factory_Latitude'] = df['Product Name'].map(lambda x: factory_mapping.get(x, {}).get('Lat', None))
df['Factory_Longitude'] = df['Product Name'].map(lambda x: factory_mapping.get(x, {}).get('Lon', None))

df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y', errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d-%m-%Y', errors='coerce')


print(" Calculating shipping lead times...")
df['Shipping Lead Time'] = (df['Ship Date'] - df['Order Date']).dt.days


df = df[df['Shipping Lead Time'] >= 0]


df.to_csv("Cleaned_Nassau_Candy_Data.csv", index=False)
print("Done! Your new cleaned file 'Cleaned_Nassau_Candy_Data.csv' has been created successfully.")


# # 8. DATA ANALYSIS & INSIGHTS

print("\n=== GENERATING BUSINESS INSIGHTS ===")

# Insight A: Average Shipping Lead Time by Factory
print("\n1. Average Shipping Lead Time (Days) by Factory:")
avg_lead_time = df.groupby('Factory')['Shipping Lead Time'].mean().reset_index()
print(avg_lead_time)

# Insight B: Total Sales and Gross Profit by Factory
print("\n2. Total Sales and Gross Profit by Factory Location:")
factory_perf = df.groupby('Factory')[['Sales', 'Gross Profit']].sum().reset_index()
print(factory_perf)

# Insight C: Top 5 Highest Grossing Products
print("\n3. Top 5 Products by Total Gross Profit:")
top_products = df.groupby('Product Name')['Gross Profit'].sum().nlargest(5).reset_index()
print(top_products)

# # 9. VISUALIZATION

import matplotlib.pyplot as plt

print("\nGenerating bar chart for Top 5 Products...")

# Create the bar chart
plt.figure(figsize=(10, 5))
plt.barh(top_products['Product Name'], top_products['Gross Profit'], color='skyblue')
plt.xlabel('Gross Profit ($)')
plt.title('Top 5 Most Profitable Candy Products')
plt.gca().invert_yaxis()  # Put the highest profit at the top
plt.tight_layout()

# Save the chart as an image 
plt.savefig('top_products_profit.png')
print("Chart saved successfully as 'top_products_profit.png'!")