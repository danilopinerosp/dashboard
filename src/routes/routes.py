"""Dashboard app routes."""

from dash import html


def render_page_content(pathname) -> html.Div:
    """Content to render in the dashboard app.

    Args:
        pathname: path of the page to render

    Returns:
        html.Div
    """
    return html.Div([html.H1("Title"), html.P(pathname)])
