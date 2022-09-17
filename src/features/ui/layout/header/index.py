"""Dashboard App Header."""
from dash import html


def header() -> html.Div:
    """Header for the dashboard app."""
    return html.Div([html.H1(id="page-title")], className="col-span-12 bg-indigo-500")
