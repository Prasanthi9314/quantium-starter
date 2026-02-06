import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load cleaned data
df = pd.read_csv("output.csv")

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Convert Sales to numeric
df["Sales"] = pd.to_numeric(df["Sales"])

# Sort by Date
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"Date": "Date", "Sales": "Total Sales"}
)

# Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods - Pink Morsels Sales Visualiser", style={"textAlign": "center"}),

    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
