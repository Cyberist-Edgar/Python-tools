from zipfile import ZipFile
import os 


def get_all_path(directory):
    file_path = []
    for root, directories, files in os.walk(directory):
        for file_name in files:
            path = os.path.join(root, file_name)
            file_path.append(path)
    return file_path

if __name__ == "__main__":
    directory = "./"
    file_paths = get_all_path(directory)
    
    with ZipFile("file.zip", "w") as zip:
        for file in file_paths:
            zip.write(file)