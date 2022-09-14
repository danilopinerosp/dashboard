"""Dashboard App Leftbar."""
from dash import html


def leftbar():
    """Leftbar fot the dashboard app."""
    leftbar_header = html.Div(["Leftbar Header"])
    return html.Div(
        [leftbar_header, html.Div([html.H1("Leftbar")])],
        className="grid col-span-2 bg-sky-500/75",
    )
