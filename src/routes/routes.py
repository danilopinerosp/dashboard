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


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page_content(pathname) -> html.Div:
    """Content to render in the dashboard app.

    Args:
        pathname: path of the page to render

    Returns:
        html.Div
    """
    if pathname == "/finance":
        page = finance()
    elif pathname == "/human-resources":
        page = human_resources()
    elif pathname == "/information-technology":
        page = it()
    elif pathname == "/operations":
        page = operations()
    elif pathname == "/":
        page = overview()
    elif pathname == "/production":
        page = production()
    else:
        page = error_404()
    return page
