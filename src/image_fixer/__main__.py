import os
import logging
import logging.config
from argparse import ArgumentParser

from PIL import Image
from tqdm import tqdm

logging.config.fileConfig('logging.conf')
LOG = logging.getLogger('Image Fixer')
ERR_ = '[\033[91mERRO\033[0m] '


def main():
    """Main function"""
    parser = ArgumentParser(prog="FixImg")
    parser.add_argument('source', type=str, help="Source file or directory.")
    parser.add_argument('target', type=str)
    args = parser.parse_args()

    source = args.source
    files = []
    folder = ''
    if os.path.isdir(source):
        files = os.listdir(source)
        folder = source
    elif os.path.isfile(source):
        file_name = os.path.basename(source)
        files.append(file_name)
        folder = os.path.join(source, os.pardir)
    else:
        print(ERR_ + f"No such file or directory at: {source}")
        exit(2)
    
    output_folder = args.target
    os.makedirs(output_folder, exist_ok=True)

    for file_name in tqdm(files, description="Processing..."):
        file_path = os.path.join(folder, file_name)
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            try:
                with Image.open(file_path) as img:
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    file_dest = os.path.join(output_folder, file_name)
                    img.save(file_dest, quality=95)
                tqdm.write(f"Processed: {file_name}")
            except Exception as e:
                tqdm.write(ERR_ + f"Error with {file_name}: {e}")


if __name__ == '__main__':
    main()
