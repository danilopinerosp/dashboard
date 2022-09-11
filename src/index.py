"""Dashboard app main index."""

from pages.app import app
from routes.routes import render_page_content  # noqa: F401

if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_props_check=True)
