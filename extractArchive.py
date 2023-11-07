import zipfile

def extract_archive(filepath,dest_folder):
    with zipfile.ZipFile(file=filepath,mode='r') as archive:
        archive.extractall(dest_folder)

if __name__ == "__main__":
    extract_archive(filepath='',dest_folder='')
