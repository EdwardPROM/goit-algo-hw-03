import shutil
import argparse
from pathlib import Path

def copy_files(source_dir: Path, dest_dir: Path):
    for item in source_dir.iterdir():
        if item.is_dir():
            copy_files(item, dest_dir)
        else:
            file_extension = item.suffix[1:]
            dest_subdir = dest_dir / file_extension
            dest_subdir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, dest_subdir)

def main():
    parser = argparse.ArgumentParser(description="Рекурсивно копіює файли та сортує їх за розширенням у вихідній директорії.")
    parser.add_argument("source_dir", help="Шлях до вихідної директорії")
    parser.add_argument("-d", "--destination_dir", help="Шлях до директорії призначення", default="dist")
    args = parser.parse_args()
    
    source_dir = Path(args.source_dir)
    dest_dir = Path(args.destination_dir)
    
    try:
        copy_files(source_dir, dest_dir)
        print("Files are copied")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
