# 🧹 Desktop Cleaner

A Python-powered desktop organization tool that automatically sorts and cleans your desktop files into organized folders based on file types.

## 📋 Features

- **Automatic File Organization**: Sorts files into categorized folders
- **Smart Program Copy Detection**: Identifies and handles duplicate program files
- **Interactive User Control**: Asks for confirmation before moving files
- **Empty Folder Cleanup**: Removes empty directories with user consent
- **File Information Display**: Shows file sizes and modification dates
- **Safe Operation**: Never overwrites existing files or folders

## 📁 Supported File Categories

### 📋 Program Files
- **Extensions**: `.exe`, `.msi`, `.bat`, `.cmd`, `.com`, `.scr`, `.pif`, `.jar`
- **Examples**: Applications, installers, batch files, Java programs
- **Special Feature**: Detects and handles program copies (e.g., `chrome (1).exe`)

### 📄 Document Files  
- **Extensions**: `.pdf`, `.txt`, `.docx`, `.doc`, `.xls`, `.xlsx`, `.pptx`, `.ppt`, `.csv`, `.rtf`, `.odt`, `.ods`, `.odp`
- **Examples**: PDFs, Word docs, Excel sheets, PowerPoint presentations

### 🖼️ Image Files
- **Extensions**: `.png`, `.jpg`, `.jpeg`, `.gif`
- **Examples**: Photos, screenshots, graphics

### 🎬 Video Files
- **Extensions**: `.mp4`, `.mkv`, `.avi`, `.mov`
- **Examples**: Movies, recordings, video clips

### 🎵 Audio Files
- **Extensions**: `.mp3`, `.wav`, `.flac`
- **Examples**: Music, podcasts, sound clips

### 📦 Compressed Files
- **Extensions**: `.zip`, `.rar`, `.7z`
- **Examples**: Archives, compressed folders

### 💻 Code Files
- **Extensions**: `.html`, `.css`, `.js`, `.py`, `.java`, `.c`, `.cpp`
- **Examples**: Source code, web files, scripts

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Windows operating system (currently configured for Windows paths)

### Installation
1. Clone or download this repository
2. No additional dependencies required (uses Python standard library)

### Usage
1. **Update the desktop path** in `FullDesktopCleaner.py`:
   ```python
   desktop_path = 'C:\\Users\\YourUsername\\Desktop'
   ```

2. **Run the program**:
   ```bash
   python FullDesktopCleaner.py
   ```

3. **Follow the interactive prompts**:
   - View your desktop file listing
   - Confirm file movements
   - Handle program copies
   - Clean up empty folders

## 🔧 How It Works

1. **Scanning**: Lists all files on your desktop with details (size, modification date)
2. **Folder Creation**: Creates organized folders if they don't exist
3. **File Filtering**: Categorizes files by extension and prompts for movement
4. **Copy Detection**: Identifies program duplicates using pattern matching
5. **Cleanup**: Removes empty folders after organization

## 🛡️ Safety Features

- **User Confirmation**: Asks before moving each file
- **Non-Destructive**: Never deletes original files (only moves them)
- **Directory Preservation**: Leaves existing folders untouched
- **Selective Operation**: Skip files you want to keep in place

## 📊 Program Copy Detection

The tool automatically detects common copy patterns:
- `program (1).exe`, `program (2).exe`
- `program - Copy.exe`
- `Copy of program.exe`
- `program_copy.exe`

For detected copies, you can choose to:
- Move to a separate "Program Copies" folder
- Delete the duplicates
- Skip and leave them unchanged

## 🎯 Example Output

```
Scanning desktop files...
File: document.pdf, Size: 2048576 bytes, Last Modified: 15 Sep 2025
File: chrome.exe, Size: 1024000 bytes, Last Modified: 10 Sep 2025
Directory: Old Files

Creating necessary folders...
Created folder: Document Files
Created folder: Program Files

Filtering and moving files...
Are you sure you want to move the file(s): document.pdf? (yes/no): y
Moved file: document.pdf to Document Files

Desktop cleanup completed.
```

## 🔄 Customization

### Adding New File Types
Edit the `folders` dictionary in `create_folders()`:
```python
folders = {
    'Your Category': ['.ext1', '.ext2', '.ext3'],
    # ... existing categories
}
```

### Changing Desktop Path
Update the `desktop_path` variable:
```python
desktop_path = '/path/to/your/desktop'  # For macOS/Linux
```

### Modifying Copy Detection
Edit the `copy_patterns` list in `is_program_copy()` to add new patterns.

## 📝 Logging

The program provides console output for all actions:
- Files moved and their destinations
- Folders created
- User decisions (skip/move)
- Empty folder removals

## ⚠️ Important Notes

- **Backup First**: Consider backing up important files before running
- **Path Configuration**: Update the desktop path for your system
- **Permissions**: Ensure Python has read/write access to your desktop
- **Testing**: Try on a test folder first to familiarize yourself with the tool

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for improvements:
- Add support for more file types
- Improve copy detection patterns
- Add configuration file support
- Cross-platform path handling

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Organizing! 🎉**

> Keep your desktop clean and your files organized with Desktop Cleaner!
