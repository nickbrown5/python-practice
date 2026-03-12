import os
import zipfile

# function to build a zip archive
def zip_all(dir, fileExts, outputFile):
    zip = zipfile.ZipFile(outputFile, "w")
    for root, dirs, files in os.walk(dir):
        for file in files:
            ext = file.split('.')[1]
            if ext in fileExts:
                print(f'Adding {os.path.join(root, file)}')
                zip.write(os.path.join(root, file))

if __name__ == '__main__':
    zip_all('./my_stuff', ['jpg','txt'], 'output.zip')