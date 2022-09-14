"""Dashboard App Header."""
from dash import html


def header():
    """Header for the dashboard app."""
    return html.Div([html.H1("Header")], className="col-span-12 bg-indigo-500")
