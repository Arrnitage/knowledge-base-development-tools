import os


def get_directory_file(filelist: list, directory: str):
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".ttp"):
                filelist.append(os.path.join(root, f))
        for sub_directory in dirs:
            get_directory_file(filelist, sub_directory)


def check_file_exist(file_path: str):
    if os.path.exists(file_path):
        return True
    else:
        return False


def write_file(file_path: str, content: str):
    with open(file_path, "w") as f:
        f.write(content)
