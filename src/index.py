from pages.app import app, server
from routes import render_page_content

if __name__ == "__main__":
    app.run_server(
        debug=True,
        dev_tool_props_check=True
    )