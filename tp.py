from pathlib import Path

# Target the current directory (or use a specific path like Path('/path/to/dir'))
current_dir = Path('.')

# Loop through and print everything
for item in current_dir.iterdir():
    print(item.name)  # .name gives just the filename or folder name
