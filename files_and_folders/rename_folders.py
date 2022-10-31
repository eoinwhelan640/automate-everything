from pathlib import Path

root_dir = Path("sample_dir")

# Don't need to be doing nested loops
# file_paths = root_dir.iterdir()
# for path in file_paths:
#     for filepath in path.iterdir():
#         print(filepath)

file_paths = root_dir.glob("**/*")
for path in file_paths:
    if path.is_file():
        parent_folder = path.parts[-2] # use -2 for generic usage
        new_filename = parent_folder + "-" + path.name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)
