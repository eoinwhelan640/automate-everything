from pathlib import Path

root_dir = Path("empties")

for i in range(10,21):
    filename = f"{i}.txt"
    filepath = root_dir / Path(filename)
    print(filepath)
    filepath.touch()