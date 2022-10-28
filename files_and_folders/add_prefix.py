from pathlib import Path

root_dir = Path("files")
file_paths = root_dir.iterdir()
print(list(file_paths))

for path in file_paths:
    new_filename = "new-" + path.stem + path.suffix
    # This would cause problems - not preserving the directory
    #new_filepath = Path(new_filename)
    new_filepath = Path.with_name(new_filename)
    path.rename(new_filepath)
