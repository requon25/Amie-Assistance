from langchain_core.tools import tool

from datetime import datetime

@tool
def date_and_time() -> str:
    """Return date and time"""

    return datetime.now().strftime("Hoy es %A %d de %B de %Y, %H:%M")