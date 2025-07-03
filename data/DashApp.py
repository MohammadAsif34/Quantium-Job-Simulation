import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load data
file = './daily_sales_data_0.csv'
df = pd.read_csv(file)

df['date'] = pd.to_datetime(df['date'])
df['product'] = df['product'].str.strip()
df = df[df['product'].str.lower() == 'pink morsel']
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
df['sales'] = df['price'] * df['quantity']

# Initialize app
app = dash.Dash(__name__)
app.title = "Soul Foods Dashboard"

# App layout
app.layout = html.Div(
    style={
        'fontFamily': 'Segoe UI, sans-serif',
        'backgroundColor': '#f4f6f9',
        'minHeight': '100vh',
        'padding': '40px 20px'
    },
    children=[
        html.Div(
            children=html.H1("Soul Foods Sales Visualizer"),
            style={
                'textAlign': 'center',
                'color': '#2c3e50',
                'marginBottom': '40px',
                'fontSize': '2.5rem',
                'fontWeight': 'bold'
            }
        ),

        html.Div(
            children=[
                html.Div("Select a Region:", style={
                    'fontWeight': 'bold',
                    'marginBottom': '10px',
                    'color': '#34495e',
                    'fontSize': '1.1rem'
                }),

                dcc.RadioItems(
                    id='region-radio',
                    options=[
                        {'label': 'North', 'value': 'north'},
                        {'label': 'East', 'value': 'east'},
                        {'label': 'South', 'value': 'south'},
                        {'label': 'West', 'value': 'west'},
                        {'label': 'All Regions', 'value': 'all'}
                    ],
                    value='all',
                    labelStyle={
                        'display': 'inline-block',
                        'marginRight': '15px',
                        'padding': '10px 16px',
                        'borderRadius': '6px',
                        'cursor': 'pointer',
                        'backgroundColor': '#ecf0f1',
                        'border': '1px solid #bdc3c7',
                        'fontSize': '1rem'
                    },
                    inputStyle={
                        "marginRight": "6px"
                    },
                    style={'textAlign': 'center', 'marginBottom': '30px'}
                )
            ],
            style={
                'maxWidth': '700px',
                'margin': '0 auto',
                'backgroundColor': 'white',
                'padding': '25px',
                'borderRadius': '12px',
                'boxShadow': '0 4px 10px rgba(0, 0, 0, 0.06)',
                'marginBottom': '40px'
            }
        ),

        html.Div(
            children=dcc.Graph(id='sales-line-chart'),
            style={
                'backgroundColor': 'white',
                'padding': '20px',
                'borderRadius': '12px',
                'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.08)'
            }
        )
    ]
)

# Callback
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_chart(selected_region):
    filtered_df = df.copy()
    if selected_region != 'all':
        filtered_df = filtered_df[filtered_df['region'] == selected_region]

    grouped = filtered_df.groupby('date').sum(numeric_only=True).reset_index()

    fig = px.line(
        grouped,
        x='date',
        y='sales',
        title=f"Pink Morsel Sales - Region: {selected_region.title()}",
        labels={'date': 'Date', 'sales': 'Total Sales (AUD)'},
        template='plotly_white'
    )

    fig.update_layout(
        title=dict(
            x=0.5,
            xanchor='center',
            font=dict(size=20)
        ),
        margin=dict(l=40, r=20, t=60, b=40),
        height=500,
        shapes=[
            dict(
                type='line',
                x0='2021-01-15',
                x1='2021-01-15',
                y0=0,
                y1=1,
                xref='x',
                yref='paper',
                line=dict(color="red", width=2, dash="dash")
            )
        ],
        annotations=[
            dict(
                x='2021-01-15',
                y=1,
                xref='x',
                yref='paper',
                text='Price Increase',
                showarrow=False,
                xanchor='left',
                yanchor='bottom',
                font=dict(color='red')
            )
        ]
    )

    return fig

# Run
if __name__ == '__main__':
    print("🚀 Dash app running at: http://127.0.0.1:8050")
    app.run(debug=True, host='127.0.0.1', port=8050)
