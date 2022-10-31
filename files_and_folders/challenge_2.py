from pathlib import Path


def search_files(term):
    return [path.absolute() for path in Path(".").glob("**/*") if path.is_file() and term in path.stem]


print(search_files("challenge"))
