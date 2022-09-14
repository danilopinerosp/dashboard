"""Dashboard app routes."""

from dash import html
from dash.dependencies import Input, Output
from pages.app import app

from pages.error_404 import error_404
from pages.finance import finance
from pages.human_resources import human_resources
from pages.it import it
from pages.operations import operations
from pages.overview import overview
from pages.production import production

from features.finance.callbacks.index import *
from features.human_resources.callbacks.index import *
from features.it.callbacks.index import *
from features.operations.callbacks.index import *
from features.overview.callbacks.index import *
from features.production.callbacks.index import *

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def render_page_content(pathname) -> html.Div:
    """Content to render in the dashboard app.

    Args:
        pathname: path of the page to render

    Returns:
        html.Div
    """
    if pathname == "/finance":
        return finance()
    elif pathname == "/human-resources":
        return human_resources()
    elif pathname == "/information-technology":
        return it()
    elif pathname == "/operations":
        return operations()
    elif pathname == "/":
        return overview()
    elif pathname == "/production":
        return production()
    else:
        return error_404()
