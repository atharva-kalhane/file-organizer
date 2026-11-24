# Python File Organizer

A simple Python project that automatically organizes files into separate folders based on their file extensions.

The program asks the user for a folder path, previews the files that will be organized, and moves them into their respective category folders after confirmation.

## Features

- Automatically organizes files based on their extensions.
- Validates the folder path entered by the user.
- Displays a preview before moving files.
- Asks for user confirmation before organizing.
- Creates category folders automatically.
- Handles duplicate filenames by renaming them.
- Skips unsupported file types.
- Handles file-moving errors.
- Displays a summary of moved, renamed, and skipped files.

## Supported File Types

- **Documents:** `.pdf`, `.docx`
- **Images:** `.jpg`, `.png`
- **Videos:** `.mp4`
- **Audio:** `.mp3`

Unsupported file types are skipped.

## Requirements

- Python 3.x
- No external libraries required (uses Python's built-in modules).

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python main.py
```

5. Enter the folder path you want to organize.
6. Review the preview and enter `yes` to confirm the operation.

## Example Output

```text
========== FILE PREVIEW ==========
photo.jpg -> Images
report.pdf -> Documents
video.mp4 -> Videos
sample.xyz -> Unknown file type (Will be skipped)
===================================

Do you want to continue? (yes/no): yes

========== ORGANIZATION SUMMARY ==========
Files moved: 3
Files renamed: 0
Files skipped: 1
===========================================
Organization completed successfully!
```