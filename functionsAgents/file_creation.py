from langchain_core.tools import tool

from pathlib import Path
from platformdirs import user_downloads_dir

@tool
def txt_creation(name: str, contenido: str) -> str:
    """Create .txt file on Downloads file"""

    dir_path = Path(user_downloads_dir())

    if dir_path is None:
        return "Could not find the directory"

    if not name.endswith(".txt"):
        name += ".txt"

    file_path = dir_path / name

    try:
        file_path.write_text(contenido)
        return f"File '{name}' created in {dir_path}"
    except Exception as e:
        return f"Error: {str(e)}"


# FUTURE FEATURES: DOCX, EXCEL, PPT, CSV