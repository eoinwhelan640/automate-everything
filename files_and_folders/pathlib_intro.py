from pathlib import Path

# Path itself is a class object.
# benefit of path class is more visible with complicated frameworks
# Has a lot of associated methods with it that make for useful utilities
pl = Path("files/sample_1.txt")
print(type(pl))

# Offers some neat utilities
print(pl.name)
print(pl.stem)
print(pl.suffix)


# Can also use it for dirs
pl_dir = Path("files")

# To print the elements use the iterdir method
# Will see that the files are themselves Path classes
for file in pl_dir.iterdir():
    print(f"file is {file}, type is {type(file)}")


