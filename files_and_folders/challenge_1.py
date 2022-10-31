from pathlib import Path
import datetime as dt

root_dir = Path("challenge_1_files")

file_paths = root_dir.glob("**/*")

if __name__ == "__main__":
    for path in file_paths:
        if path.is_file():
            # How to add created time
            stats = path.stat()
            created_time = stats.st_ctime
            print(dt.datetime.fromtimestamp(created_time).strftime("%Y-%m-%d_%H:%M:%S"))

            # How to rename based off folders
            new_name = "-".join(path.parts[-3:-1])
            new_filename = new_name + "-" + path.name
            new_path = path.with_name(new_filename)
            #new_path = path.with_name(new_filename[-5:]) # to undo name change and revert to start
            path.rename(new_path)

    # Convert files from txt to csv
    # if False:
    #     for path in root_dir.rglob("*.txt"):
    #         new_filepath = path.with_suffix(".txt")
    #         path.rename(new_filepath)