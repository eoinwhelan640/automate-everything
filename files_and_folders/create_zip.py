from pathlib import Path
import zipfile

root_dir = Path("empties")
zip_path = root_dir / Path("zipper.zip")

with zipfile.ZipFile(zip_path, "w") as writefile:
    for path in root_dir.rglob("*.txt"):
        writefile.write(path)

## To extract the zipfiles
unzip_path = Path("unzip_folder")

for path in root_dir.glob("*.zip"):
    with zipfile.ZipFile(path, "r") as readfile:
        readfile.extractall(path=unzip_path)