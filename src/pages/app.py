"""Dashboard app page."""

import dash
import flask

from features.ui.layout.index import layout

server = flask.Flask(__name__)

app = dash.Dash(
    __name__,
    server=server,
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    title="Dashboard App",
)

app.layout = layout
