import pandas as pd
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
csv_input_path = os.path.join(current_folder, "Nassau Candy Distributor.csv")
csv_output_path = os.path.join(current_folder, "Cleaned_Nassau_Candy_Data.csv")

print(f"🔄 Looking for data at: {csv_input_path}")
df = pd.read_csv(csv_input_path)


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

print("🏭 Mapping products to factories...")
df['Factory'] = df['Product Name'].map(lambda x: factory_mapping.get(x, {}).get('Factory', 'Unknown'))
df['Factory_Latitude'] = df['Product Name'].map(lambda x: factory_mapping.get(x, {}).get('Lat', None))
df['Factory_Longitude'] = df['Product Name'].map(lambda x: factory_mapping.get(x, {}).get('Lon', None))

df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d-%m-%Y')

print("⏳ Calculating shipping lead times...")
df['Shipping Lead Time'] = (df['Ship Date'] - df['Order Date']).dt.days

df = df[df['Shipping Lead Time'] >= 0]

df.to_csv(csv_output_path, index=False)
print(f"✅ Success! File saved directly to: {csv_output_path}")