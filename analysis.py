import pandas as pd
import folium
from graph import bar_chart, line_chart
import matplotlib.pyplot as plt

# 1. Top 10 channels by subscribers
def plot_top_subscribers(df: pd.DataFrame):
    top = df.nlargest(10, 'subscribers')
    bar_chart(
        x=top['Youtuber'],
        y=top['subscribers'],
        title="Top 10 YouTube Channels by Subscribers",
        x_label="Channel",
        y_label="Subscribers",
        rotate_x=True
    )

# 2. Bottom 10 channels by subscribers
def plot_bottom_subscribers(df: pd.DataFrame):
    bottom = df.nsmallest(10, 'subscribers')
    bar_chart(
        x=bottom['Youtuber'],
        y=bottom['subscribers'],
        title="10 Least-Subscribed YouTube Channels",
        x_label="Channel",
        y_label="Subscribers",
        rotate_x=True
    )

# 3. Top 10 most-viewed channels
def plot_top_views(df: pd.DataFrame):
    top = df.nlargest(10, 'video views')
    bar_chart(
        x=top['Youtuber'],
        y=top['video views'],
        title="Top 10 YouTube Channels by Video Views",
        x_label="Channel",
        y_label="Video Views",
        rotate_x=True
    )

# 4. Channels per category
def plot_channels_by_category(df: pd.DataFrame):
    counts = df['category'].value_counts()
    bar_chart(
        x=counts.index,
        y=counts.values,
        title="YouTube Channels per Category",
        x_label="Category",
        y_label="Number of Channels",
        rotate_x=True
    )

# 5. Uploads vs Subscribers (line chart)
def plot_uploads_vs_subscribers(df: pd.DataFrame):
    top = df.nlargest(10, 'uploads')
    line_chart(
        x=top['Youtuber'],
        y1=top['uploads'],
        y2=top['subscribers'],
        title="Uploads vs Subscribers (Top 10 Uploaders)",
        x_label="Channel",
        y_label="Count"
    )

# 6. Channels per country
def plot_channels_by_country(df: pd.DataFrame):
    counts = df['Country'].value_counts().head(20)
    bar_chart(
        x=counts.index,
        y=counts.values,
        title="Number of Channels by Country (Top 20)",
        x_label="Country",
        y_label="Channels",
        rotate_x=True
    )

# 7. Channels created per year
def plot_channels_by_year(df: pd.DataFrame):
    df['created_year'] = pd.to_numeric(df['created_year'], errors='coerce')
    
 
    df_years = df[df['created_year'] >= 2005].copy()
    
    if df_years.empty:
        print("⚠️ No valid creation year data from 2005 onwards.")
        return

    counts = df_years['created_year'].value_counts().sort_index()

    years = counts.index.astype(int).tolist()
    totals = counts.values.tolist()

    plt.figure(figsize=(10, 6))
    plt.bar(years, totals, color='skyblue')
    plt.title("YouTube Channels Created per Year (2005+)")
    plt.xlabel("Year")
    plt.ylabel("Number of Channels")
    plt.xticks(years, rotation=45, ha='right')
    plt.xlim(min(years)-0.5, max(years)+0.5)
    plt.tight_layout()
    plt.show()


# 8. Earnings map (world)
def plot_earnings_map(df: pd.DataFrame):
    df_clean = df.dropna(subset=['Latitude', 'Longitude', 'highest_yearly_earnings']).copy()

    world_map = folium.Map(location=[20, 0], zoom_start=2)
    top = df_clean.nlargest(20, 'highest_yearly_earnings')

    for _, row in top.iterrows():
        lat, lon = row['Latitude'], row['Longitude']
        # Certifica que lat/lon são float
        lat, lon = float(lat), float(lon)
        earnings = row['highest_yearly_earnings']
        radius = max(3, earnings / 5_000_000)

        folium.CircleMarker(
            location=[lat, lon],
            radius=radius,
            popup=f"{row['Youtuber']}: ${int(earnings):,}",
            color='green',
            fill=True,
            fill_opacity=0.6
        ).add_to(world_map)

    return world_map

