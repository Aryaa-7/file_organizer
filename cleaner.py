import os
import shutil # Import the shutil module for moving files
import sys # Import the sys module to handle command-line arguments

# --- Custom file categories remain the same ---
File_Categories = {
    'Image_Files': ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    'Video_Files': ['.mp4', '.mkv', '.flv', '.mpeg'],
    'Document_Files': ['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Setup_Files': ['.exe', '.msi'],
    'Audio_Files': ['.mp3', '.wav', '.m4a'],
    'Compressed_Files': ['.zip', '.rar', '.7z'],
    'Programming_Files': ['.py', '.java', '.c', '.cpp', '.html', '.css', '.js'],
}

# Check if the user provided a directory path when running the script
if len(sys.argv) != 2:
    print("\nUsage: python cleaner.py <path_to_directory>")
    print("Example: python cleaner.py \"C:\\Users\\YourUser\\Downloads\"")
    sys.exit(1) # Exit the script if the path is missing

target_directory = sys.argv[1]

try:
    print(f"Scanning directory: {target_directory}")
    all_files = os.listdir(target_directory)

    for filename in all_files:
        # Create the full path for the source file
        source_path = os.path.join(target_directory, filename)

        # only  move files, skip over any folders.
        # Also, don't try to move the script itself!
        if os.path.isdir(source_path) or filename == os.path.basename(__file__): 
            continue

        # Get the file extension
        name, extension = os.path.splitext(filename)
        extension = extension.lower() # Standardize to lowercase

        # --- CORE LOGIC STARTS HERE ---

        # 1. Determine the destination folder name
        destination_folder_name = 'Other_Files' # Start with a default
        for category, extensions in File_Categories.items():
            if extension in extensions:
                destination_folder_name = category
                break # Found a match, no need to check further

        # 2. Create the full path for the destination folder
        destination_folder_path = os.path.join(target_directory, destination_folder_name)
        
        # 3. Create the destination folder if it doesn't exist
        os.makedirs(destination_folder_path, exist_ok=True)

        # 4. Move the file
        print(f"Moving '{filename}' to -> {destination_folder_name}")
        shutil.move(source_path, os.path.join(destination_folder_path, filename))
        
        # --- CORE LOGIC ENDS HERE ---

    print("\nDirectory cleanup complete!")

except FileNotFoundError:
    print(f"Error: The directory '{target_directory}' does not exist. Please check the path.")
except Exception as e:
    # Catch any other potential errors during file moving
    print(f"An unexpected error occurred: {e}")

