__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from pathlib import Path
from zipfile import ZipFile

folder_name = Path.cwd() / "files" / "cache"


def clean_cache():
    try:
        folder_name.mkdir(exist_ok=False)
    except FileExistsError:
        for child in folder_name.iterdir():
            child.unlink()
        print("Empty folder created.")
    else:
        print("New folder created.")


def cache_zip(zip_file, folder):
    zip_file = Path(zip_file)
    folder = Path(folder)
    with ZipFile(zip_file, "r") as zip:
        zip.extractall(folder)
    return print(f"Extracted {zip_file.stem}.zip to {folder.stem} folder.")


def cached_files():
    return [str(file) for file in folder_name.iterdir() if file.is_file()]


def find_password(file_with_pathnames):
    for path in file_with_pathnames:
        with open(path) as file:
            if "password" in file.read():
                target_file = path
                break

    with open(target_file) as file2:
        for line in file2:
            if "password" in line:
                target_line = line
                break
    return target_line.split()[1]
