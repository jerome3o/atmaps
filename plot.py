import plotly.express as px
from constants import MAPBOX_TOKEN

def main():
    px.set_mapbox_access_token(MAPBOX_TOKEN)
    df = px.data.carshare()
    fig = px.scatter_mapbox(
        df,
        lat="centroid_lat",
        lon="centroid_lon",
        color="peak_hour",
        size="car_hours",
        color_continuous_scale=px.colors.cyclical.IceFire,
        size_max=15,
        zoom=10,
    )
    fig.update_layout(mapbox_style="carto-positron")
    with open("index.html", "w") as f:
        f.write(fig.to_html())


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
