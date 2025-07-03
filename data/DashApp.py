import datetime
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

file = './daily_sales_data_0.csv'

# Load and clean data
df = pd.read_csv(file)
df['date'] = pd.to_datetime(df['date'])
df['product'] = df['product'].str.strip()

df_pm = df[df['product'].str.lower() == 'pink morsel'].copy()
df_pm = df_pm.sort_values('date')

df_pm['price'] = df_pm['price'].replace('[\$,]', '', regex=True).astype(float)
df_pm['sales'] = df_pm['price'] * df_pm['quantity']

fig = px.line(
    df_pm,
    x='date',
    y='sales',
    title="Pink Morsel Sales Over Time",
    labels={'date': 'Date', 'sales': 'Total Sales (AUD)'}
)

fig.update_layout(
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

app = dash.Dash(__name__)
app.title = "Soul Foods Sales Visualizer"

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualizer", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

# Run app
if __name__ == '__main__':
    print("🚀 Dash app running at: http://127.0.0.1:8050")
    app.run(debug=True, host='127.0.0.1', port=8050)
