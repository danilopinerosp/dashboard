"""Page for 404 Error."""
from dash import html


def error_404():
    """Return page 404."""
    return html.Div([html.H1("Error 404")])
