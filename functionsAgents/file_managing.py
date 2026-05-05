from langchain_core.tools import tool

from pathlib import Path
from platformdirs import user_downloads_dir
import shutil
import subprocess
import platform
import os

@tool
def create_folder(name: str) -> str:
    """Creates a folder in Download directory"""
    download_path = Path(user_downloads_dir())
    path = download_path / name
    path.mkdir(parents=True, exist_ok=True)
    
    return f"Folder '{name}' created"

@tool
def open_file(location: str, name: str) -> str:
    """Opens a file"""
    path = Path.home() / location / name
    
    if not path.exists():
        return f"The file '{name}' does not exist."
    
    # Check the user's operating system
    system = platform.system()

    if system == "Windows":
        os.startfile(str(path)) 
    elif system == "Darwin":
        subprocess.run(["open", str(path)])
    else:
        subprocess.run(["xdg-open", str(path)])
    
    return f"File '{name}' opened."

@tool
def rename_item(location: str, old_name: str, new_name: str) -> str:
    """Renames a file or folder"""
    path = Path.home() / location / old_name
    new_path = path.parent / new_name

    if not path.exists():
        return f"'{old_name}' does not exist in {location}"

    path.rename(new_path)

    return f"Name successfully changed to '{new_name}'"

@tool
def delete_item(location: str, name: str) -> str:
    """Deletes a file or folder"""
    path = Path.home() / location / name

    if not path.exists():
        return "Does not exist"

    try:
        if path.is_file():
            path.unlink()
            return f"File '{name}' deleted"
        elif path.is_dir():
            shutil.rmtree(path)
            return f"Folder '{name}' deleted"
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def search_file(location: str, name: str) -> str:
    """Searches files by name"""

    base = Path.home() / location
    results = []

    for file in base.rglob("*"):
        if name.lower() in file.name.lower():
            results.append(str(file))

    if not results:
        return "No files found"

    return "\n".join(results[:5])  # limit results

@tool
def move_file(source: str, destination: str, file_name: str) -> str:
    """Moves a file from one location to another"""

    source_path = Path.home() / source / file_name
    destination_path = Path.home() / destination / file_name

    if not source_path.exists():
        return "Source file does not exist"

    try:
        shutil.move(source_path, destination_path)
        return f"File moved to {destination}"
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def copy_file(source: str, destination: str, file_name: str) -> str:
    """Copies a file from one location to another"""

    source_path = Path.home() / source / file_name
    destination_path = Path.home() / destination / file_name

    if not source_path.exists():
        return "Source file does not exist"

    try:
        shutil.copy(source_path, destination_path)
        return f"File copied to {destination}"
    except Exception as e:
        return f"Error: {str(e)}"