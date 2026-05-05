from langchain_core.tools import tool

import webbrowser

@tool
def open_url(url: str) -> str:
    """open url on a web browser"""
    if not url.startswith("http"):
        url = "https://" + url
    webbrowser.open(url)
    return f"The {url} is opened."