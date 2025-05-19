# # The shutil module in Python is part of the standard library and is used for high-level file operations,
# #  such as copying, moving, and removing files and directories. It’s especially helpful for scripting and
# #  automation tasks involving file system manipulation.

# ✅ Common Functions in shutil
# 1. Copying Files

# import shutil

# Copy file with metadata (permissions, timestamps, etc.)
# shutil.copy2('source.txt', 'destination.txt')

# Copy file without metadata
# shutil.copy('source.txt', 'destination.txt')


# 2. Copying Entire Directory

# shutil.copytree('source_folder', 'destination_folder')


# 3. Moving Files or Directories

# shutil.move('file_or_folder', 'new_location/')


# 4. Removing Directory (recursively)

# shutil.rmtree('folder_name')


# 5. Archiving (zip, tar, etc.)

# shutil.make_archive('backup', 'zip', 'folder_to_compress')


# 6. Extracting Disk Usage Info

# usage = shutil.disk_usage('/')
# print(f"Total: {usage.total}, Used: {usage.used}, Free: {usage.free}")


# 7. Which Executable

# shutil.which('python')  # Returns path to python executable



# 🔧 Challenge: Folder Backup Utility
# Write a Python script that:

# Takes a folder path as input

# Copies the entire folder to a backup directory

# Compresses the backup folder into a ZIP archive

# Prints the size of the original and compressed folders

# Deletes the copied backup folder (leaves only the .zip)

# ✅ Requirements:
# Use shutil.copytree(), shutil.make_archive(), shutil.rmtree(), and os.path.getsize()

# Accept folder path using input() or argparse (bonus)


import shutil
import argparse
from pathlib import Path

# path = Path("F:/Python Code With Harry")


# Taking folder path from user

parser = argparse.ArgumentParser(description="Backup mentioned Folder Data into compressed file command line utility")

parser.add_argument('path',type=str,help='Enter the path of the directory to be backed up')

args = parser.parse_args()

folder_dir = Path(args.path)

# Define the path
copyfolder_dir = Path(r"F:\BackupFolderCodeWithHarry")

if folder_dir.exists() and folder_dir.is_dir():

    # Remove old backup folder if it exists
    if copyfolder_dir.exists() and copyfolder_dir.is_dir():
        shutil.rmtree(copyfolder_dir)
    # Copies the entire folder to a backup directory

    shutil.copytree(folder_dir, copyfolder_dir)
    print("Folder copy to backup Location")

    # Compresses the backup folder into a ZIP archive

    zip_path = shutil.make_archive('code_with_harrybackup', 'zip', copyfolder_dir)
    print("Zip file created of Backup Folder")

     # Prints the size of the original and compressed folders

    # incorrect implementation by me 

    # usage = shutil.disk_usage(folder_path)
    # compressed_usage = shutil.disk_usage(Path('code_with_harrybackup'))
    # print(f"OriginalFileSize: {usage.used}, CompressedFileSize:{compressed_usage.used}")

    original_size = sum(f.stat().st_size for f in folder_dir.glob('**/*') if f.is_file())

    compressed_size = Path(zip_path).stat().st_size

    print(f"Original_fileSize: {original_size/ 1024:.2f} KB , CompressedFileSize: {compressed_size/ 1024:.2f}KB")
    print(f"Path of the created zip folder: ",Path(zip_path))



    # Deletes the copied backup folder (leaves only the .zip)

    shutil.rmtree(copyfolder_dir)
    print("Backup Folder Removed")


    # print("Path exists:", path)

else:
    print("Mentioned DIrectory do not exists",folder_dir)

