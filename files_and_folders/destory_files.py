from pathlib import Path

# method to delete files permanently and irreparably
root_dir = Path("to_delete")

# Adding the delete so we're very careful about what we're deleting
for path in root_dir.glob("*delete*.csv"):
    with open(path, "wb") as file:
        # obliterates them
        file.write(b"")
    # Deletes it
    path.unlink()