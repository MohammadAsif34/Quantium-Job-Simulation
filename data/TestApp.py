import pytest
from dash import Dash
from DashApp import app as dash_app  # Assuming your app file is named DashApp.py

@pytest.fixture
def app():
    return dash_app

def test_header_present(dash_duo, app):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "Soul Foods Sales Visualizer"

def test_graph_present(dash_duo, app):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)
    region_picker = dash_duo.find_element("#region-radio")
    assert region_picker is not None
