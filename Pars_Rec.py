import argparse
import shutil
from pathlib import Path


def copy_files(source_dir, dest_dir):
    try:
        for item in source_dir.iterdir():

            if item.is_dir():
                copy_files(item, dest_dir)

            elif item.is_file():
                extension = item.suffix[1:] if item.suffix else "no_extension"

                target_folder = dest_dir / extension
                target_folder.mkdir(parents=True, exist_ok=True)

                target_file = target_folder / item.name

                shutil.copy2(item, target_file)

                print(f"Copied: {item} -> {target_file}")

    except Exception as error:
        print(f"Error processing {source_dir}: {error}")


def main():
    parser = argparse.ArgumentParser(description="Recursive file sorter")

    parser.add_argument("source", help="Source directory")
    parser.add_argument(
        "destination",
        nargs="?",
        default="dist",
        help="Destination directory"
    )

    args = parser.parse_args()

    source_path = Path(args.source)
    destination_path = Path(args.destination)

    if not source_path.exists():
        print("Source directory does not exist")
        return

    destination_path.mkdir(parents=True, exist_ok=True)

    copy_files(source_path, destination_path)

    print("File sorting completed")


if __name__ == "__main__":
    main()
    