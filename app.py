import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load data
df = pd.read_csv("output.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Convert Sales to numeric
df["Sales"] = pd.to_numeric(df["Sales"])

# Sort by date
df = df.sort_values("Date")

# Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "backgroundColor": "#f4f6f9",
        "padding": "30px"
    },
    children=[

        html.H1(
            "Soul Foods - Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "10px"
            }
        ),

        html.P(
            "Use the filter below to view sales data by region.",
            style={
                "textAlign": "center",
                "color": "#555",
                "fontSize": "18px",
                "marginBottom": "30px"
            }
        ),

        html.Div(
            style={
                "display": "flex",
                "justifyContent": "center",
                "marginBottom": "25px"
            },
            children=[
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={
                        "fontSize": "18px",
                        "padding": "10px",
                        "backgroundColor": "white",
                        "borderRadius": "10px",
                        "boxShadow": "0px 2px 8px rgba(0,0,0,0.1)"
                    }
                )
            ]
        ),

        dcc.Graph(id="sales-graph")
    ]
)

# Callback to update graph based on region selection
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time ({selected_region.upper()})",
        labels={"Date": "Date", "Sales": "Total Sales"}
    )

    # Add price increase marker line
    fig.add_vline(
        x="2021-01-15",
        line_width=3,
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase (15 Jan 2021)",
        annotation_position="top left"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f4f6f9",
        font=dict(color="#2c3e50")
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
