import os
import sys
from datetime import datetime

def get_file_date(file_path):
    timestamp = os.path.getmtime(file_path)
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

def get_file_title(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]

def main(md_file):
    if not os.path.isfile(md_file):
        print(f"File {md_file} does not exist.")
        return

    date = get_file_date(md_file)
    title = get_file_title(md_file)
    
    # Output the Pandoc command
    pandoc_command = f"pandoc --standalone --metadata date-meta='{date}' --metadata title='{title}' --template template.html {md_file} -o {title}.html"
    # -o {title}.html
    print(pandoc_command)
    os.system(pandoc_command)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python preprocess.py <file.md>")
    else:
        main(sys.argv[1])

