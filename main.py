
import os
import shutil
from pathlib import Path

# Step 1: Ask user to enter folder path
target_folder = input("Enter folder path: ").strip()

print("Target folder:", target_folder)

# Step 2: Check whether folder exists
folder_status = os.path.exists(target_folder)
print("Folder exists:", folder_status)

if not folder_status:
    print("Folder does not exist!")
    exit()

# Step 3: Check whether it is a directory
if not os.path.isdir(target_folder):
    print("The given path is not a folder!")
    exit()

# Step 4: Get all items inside the selected folder
files = os.listdir(target_folder)

# Step 5: Define file categories
file_categories = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".jpg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".mp3": "Audio"
}

# Step 6: Initialize preview list and counters
preview_list = []

files_moved = 0
files_renamed = 0
files_skipped = 0

# Step 7: Prepare preview
print("\n========== FILE PREVIEW ==========")

for i in files:
    file_path = os.path.join(target_folder, i)

    if os.path.isfile(file_path):
        extension = Path(i).suffix.lower()
        category = file_categories.get(extension)

        if category:
            destination_folder = os.path.join(target_folder, category)
            destination_path = os.path.join(destination_folder, i)

            # Handle duplicate filenames
            if os.path.exists(destination_path):
                file_name = Path(i).stem
                extension = Path(i).suffix

                count = 1

                while os.path.exists(destination_path):
                    new_name = f"{file_name}_{count}{extension}"
                    destination_path = os.path.join(
                        destination_folder, new_name
                    )
                    count += 1

            # Store preview information
            preview_list.append(
                (i, destination_folder, destination_path)
            )

            # Display preview
            destination_name = os.path.basename(destination_path)

            if destination_name != i:
                print(f"{i} -> {category}/{destination_name}")
            else:
                print(f"{i} -> {category}")

        else:
            print(i, "-> Unknown file type (Will be skipped)")
            files_skipped += 1

if not preview_list:
    print("No supported files found to organize.")

print("===================================")

# Step 8: Ask user confirmation after preview
confirmation = input(
    "\nDo you want to continue? (yes/no): "
).strip().lower()

if confirmation != "yes":
    print("Operation cancelled!")
    exit()

# Step 9: Move files after confirmation
for file_name, destination_folder, destination_path in preview_list:

    file_path = os.path.join(target_folder, file_name)

    # Create category folder if needed
    os.makedirs(destination_folder, exist_ok=True)

    # Move file with error handling
    try:
        shutil.move(file_path, destination_path)
        files_moved += 1

        if destination_path != os.path.join(destination_folder, file_name):
            files_renamed += 1

    except OSError as e:
        print(f"Could not move {file_name}: {e}")
        files_skipped += 1

# Step 10: Organization summary
print("\n========== ORGANIZATION SUMMARY ==========")
print("Files moved:", files_moved)
print("Files renamed:", files_renamed)
print("Files skipped:", files_skipped)
print("===========================================")
print("Organization completed successfully!")
