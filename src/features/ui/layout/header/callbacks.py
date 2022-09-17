"""Dashboard App header callbacks."""
from dash.dependencies import Input, Output

from pages.app import app


@app.callback(Output("page-title", "children"), Input("url", "pathname"))
def update_page_title(pathname) -> str:
    """Update page title.

    Args:
        pathname: Pathname of the renderes page.

    Returns:
        str
    """
    pages = {
        "/finance": "Finance",
        "/": "Overview",
        "/human-resources": "Human Resources",
        "/information-technology": "Information Technology",
        "/operations": "Operations",
        "/production": "Production",
    }
    page_selected = pages.get(pathname, "")
    if page_selected[-1].lower() == "s":
        page_title = f"{page_selected}' Data Analysis"
    else:
        page_title = f"{page_selected}'s Data Analysis"
    return page_title
