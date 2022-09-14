"""Dashboard app page."""

import dash
import flask

from features.ui.layout.index import layout

server = flask.Flask(__name__)

external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

app = dash.Dash(
    __name__,
    server=server,
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    title="Dashboard App",
    external_scripts=external_script,
)

app.scripts.config.serve_locally = True
app.layout = layout()
