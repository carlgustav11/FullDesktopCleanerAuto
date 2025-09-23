# Read/List all files in desktop using scandir()
# Get the information about each file using stat()
# If the file ends with .exe, leave create a folder for program files
# If the file ends with .pdf, .txt, .docx, .doc, .xls, .xlsx, .pptx, .ppt, .csv, .rtf, .odt, .ods, .odp, create a folder for the all document files
# If the file ends with .png, .jpg, .jpeg, .gif, create a folder for the all image files
# If the file ends with .mp4, .mkv, .avi, .mov, create a folder for the all video files
# If the file ends with .mp3, .wav, .flac, create a folder for the all audio files
# If the file ends with .zip, .rar, .7z, create a folder for the all compressed files
# If the file ends with .html, .css, .js, .py, .java, .c, .cpp, create a folder for the all code files
# If the file ends with .lnk, create a folder for the all shortcut files
# Then move each file to the respective folder based on its type
# If the folder already exists, do not create it again
# If the file type is not recognized, leave it as it is
# If the file is a directory, leave it as it is
# Delete empty folders by checking if the folder is empty using os.listdir() by asking for user input
# Handle exceptions and errors gracefully
# Log actions taken (e.g., files moved, folders created, errors encountered)

import os
import shutil
from datetime import datetime
import re

# Define the desktop path

desktop_path = 'C:\\Users\\Carlg\\Desktop'

# Function to check if a file is a copy of a program
def is_program_copy(filename):
    """
    Detects if a file is a copy based on common copy patterns:
    - filename (1).exe, filename (2).exe, etc.
    - filename - Copy.exe
    - Copy of filename.exe
    - filename_copy.exe
    """
    copy_patterns = [
        r'.*\s\(\d+\)\.(exe|com|msi|bat|cmd|scr|pif)$',  # filename (1).exe
        r'.*\s-\sCopy\.(exe|com|msi|bat|cmd|scr|pif)$',   # filename - Copy.exe
        r'^Copy\sof\s.*\.(exe|com|msi|bat|cmd|scr|pif)$', # Copy of filename.exe
        r'.*_copy\.(exe|com|msi|bat|cmd|scr|pif)$',       # filename_copy.exe
        r'.*\.copy\.(exe|com|msi|bat|cmd|scr|pif)$'       # filename.copy.exe
    ]
    
    filename_lower = filename.lower()
    return any(re.match(pattern, filename_lower, re.IGNORECASE) for pattern in copy_patterns)

# Function to handle program copies (move or delete)
def handle_program_copy(f_path, f_name, desktop_path):
    """Handle program copies - user can choose to move, delete, or skip"""
    print(f'Found program copy: {f_name}')
    choice = input('Choose action: (m)ove to Program Copies, (d)elete, (s)kip: ').lower()
    
    if choice in ['m', 'move']:
        shutil.move(f_path, f'{desktop_path}/Program Copies')
        print(f'Moved program copy: {f_name} to Program Copies')
    elif choice in ['d', 'delete']:
        confirm = input(f'Are you sure you want to DELETE {f_name}? (yes/no): ')
        if confirm.lower() in ['y', 'yes']:
            os.remove(f_path)
            print(f'Deleted program copy: {f_name}')
        else:
            print(f'Cancelled deletion of: {f_name}')
    else:
        print(f'Skipped program copy: {f_name}')

# Function to convert timestamp to human-readable date
def convert_date(timestamp):
    d = datetime.fromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

# Function to Read/List all files in desktop using scandir()
def desktop_files(desktop_path):
    with os.scandir(desktop_path) as entries:
        for entry in entries:
            if entry.is_file():
                print(f'File: {entry.name}, Size: {entry.stat().st_size} bytes, Last Modified: {convert_date(entry.stat().st_mtime)}')
            elif entry.is_dir():
                print(f'Directory: {entry.name}')


# Create folders if they do not exist
def create_folders(desktop_path):
    folders = {
        'Program Files': ['.exe', '.lnk', '.msi', '.bat', '.cmd', '.com', '.scr', '.pif', '.cpl', '.msc', '.jar', 'program', '.app'],
        'Document Files': ['.pdf', '.txt', '.docx', '.doc', '.xls', '.xlsx', '.pptx', '.ppt', '.csv', '.rtf', '.odt', '.ods', '.odp', '.net'
        ],
        'Image Files': ['.png', '.jpg', '.jpeg', '.gif'],
        'Video Files': ['.mp4', '.mkv', '.avi', '.mov'],
        'Audio Files': ['.mp3', '.wav', '.flac'],
        'Compressed Files': ['.zip', '.rar', '.7z'],
        'Code Files': ['.html', '.css', '.js', '.py', '.java', '.c', '.cpp']
    }
    
    for folder in folders.keys():
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f'Created folder: {folder}')

# Filter the files based on their extensions and move them to respective folders
def filter_files(desktop_path):
    for f_name in os.listdir(desktop_path):
        f_path = os.path.join(desktop_path, f_name)
        if os.path.isfile(f_path):
            # Check if it's a program copy first
            if is_program_copy(f_name):
                handle_program_copy(f_path, f_name, desktop_path)
            # Check for regular program files
            elif f_name.endswith(('.exe', '.lnk', '.msi', '.bat', '.cmd', '.com', '.scr', '.pif', '.cpl', '.msc', '.jar', 'program', '.app')):
                yes = input(f'Are you sure you want to move the file(s): {f_name}? (yes/no): ')
                if yes.lower() in ['y', 'yes']:
                    shutil.move(f_path, f'{desktop_path}/Program Files')
                    print(f'Moved file: {f_name} to Program Files')
                else:
                    print(f'Skipped moving file(s): {f_name}')
            elif f_name.endswith(('.pdf', '.txt', '.docx', '.doc', '.xls', '.xlsx', '.pptx', '.ppt', '.csv', '.rtf', '.odt', '.ods', '.odp')):
                yes = input(f'Are you sure you want to move the file(s): {f_name}? (yes/no): ')
                if yes.lower() in ['y', 'yes']:
                    shutil.move(f_path, f'{desktop_path}/Document Files')
                    print(f'Moved file: {f_name} to Document Files')
                else:
                    print(f'Skipped moving file(s): {f_name}')
            elif f_name.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                yes = input(f'Are you sure you want to move the file(s): {f_name}? (yes/no): ')
                if yes.lower() in ['y', 'yes']:
                    shutil.move(f_path, f'{desktop_path}/Image Files')
                    print(f'Moved file: {f_name} to Image Files')
                else:
                    print(f'Skipped moving file(s): {f_name}')
            elif f_name.endswith(('.mp4', '.mkv', '.avi', '.mov')):
                yes = input(f'Are you sure you want to move the file(s): {f_name}? (yes/no): ')
                if yes.lower() in ['y', 'yes']:
                    shutil.move(f_path, f'{desktop_path}/Video Files')
                    print(f'Moved file: {f_name} to Video Files')
                else:
                    print(f'Skipped moving file(s): {f_name}')
            elif f_name.endswith(('.mp3', '.wav', '.flac')):
                yes = input(f'Are you sure you want to move the file(s): {f_name}? (yes/no): ')
                if yes.lower() in ['y', 'yes']:
                    shutil.move(f_path, f'{desktop_path}/Audio Files')
                    print(f'Moved file: {f_name} to Audio Files')
                else:
                    print(f'Skipped moving file(s): {f_name}')
            elif f_name.endswith(('.zip', '.rar', '.7z')):
                yes = input(f'Are you sure you want to move the file(s): {f_name}? (yes/no): ')
                if yes.lower() in ['y', 'yes']:
                    shutil.move(f_path, f'{desktop_path}/Compressed Files')
                    print(f'Moved file: {f_name} to Compressed Files')
                else:
                    print(f'Skipped moving file(s): {f_name}')
            elif f_name.endswith(('.html', '.css', '.js', '.py', '.java', '.c', '.cpp')):
                yes = input(f'Are you sure you want to move the file(s): {f_name}? (yes/no): ')
                if yes.lower() in ['y', 'yes']:
                    shutil.move(f_path, f'{desktop_path}/Code Files')
                    print(f'Moved file: {f_name} to Code Files')
                else:
                    print(f'Skipped moving file(s): {f_name}')
            else:
                f_name.startswith('Genvej', 'genvej', 'Shortcut', 'shortcut')
                yes = input(f'Are you sure you want to move the file(s): {f_name}? (yes/no): ')
                if yes.lower() in ['y', 'yes']:
                    shutil.move(f_path, f'{desktop_path}/Program Files')
                    print(f'Moved file: {f_name} to Program Files')
                else:
                    print(f'Skipped moving file(s): {f_name}')


# Function to delete empty folders
def delete_empty_folders(desktop_path):
    with os.scandir(desktop_path) as entries:
        for entry in entries:
            if entry.is_dir():
                if not os.listdir(entry.path):
                    yes = input(f'Are you sure you want to delete the empty folder(s): {entry.name}? (yes/no): ')
                    if yes.lower() in ['y', 'yes']:
                        os.rmdir(entry.path)
                        print(f'Deleted empty folder: {entry.name}')
                    else:
                        print(f'Skipped deletion of folder: {entry.name}')
                else:
                    print(f'Folder not empty, not deleted: {entry.name}')

# Main execution
if __name__ == '__main__':
    print("Scanning desktop files...")
    desktop_files(desktop_path)
    print("\nCreating necessary folders...")
    create_folders(desktop_path)
    print("\nFiltering and moving files...")
    filter_files(desktop_path)
    print("\nDeleting empty folders...")
    delete_empty_folders(desktop_path)
    print("\nDesktop cleanup completed.")
