import os
import shutil
import sys
import zipfile

import requests

binary_files = {
    "darwin": ["adb"],
    "linux": ["adb"],
    "win32": ["adb.exe", "AdbWinApi.dll", "AdbWinUsbApi.dll"],
}

urls = {
    "darwin": "https://dl.google.com/android/repository/platform-tools-latest-darwin.zip",
    "linux": "https://dl.google.com/android/repository/platform-tools-latest-linux.zip",
    "win32": "https://dl.google.com/android/repository/platform-tools-latest-windows.zip"
}

target_dir = os.path.join('Contents', 'Libraries', 'Modules', 'adbutils', 'binaries')

platform = sys.platform


def copy_binaries():
    """download adb archives and copy binaries to the target directory"""
    assert os.path.isdir(target_dir)

    base_url = urls[platform]
    archive_name = os.path.join(target_dir, f'{platform}.zip')

    print("Downloading", base_url, "...", end=" ", flush=True)
    with open(archive_name, 'wb') as handle:
        response = requests.get(base_url, stream=True)
        if not response.ok:
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
    print("done")
    
    for binary in binary_files[sys.platform]:
        print("Extracting", binary, "...", end=" ")
        # extract the specified file from the archive
        member_name = f'platform-tools/{binary}'
        extract_archive_file(archive_file=archive_name, file=member_name, destination_folder=target_dir)
        shutil.move(src=os.path.join(target_dir, member_name), dst=os.path.join(target_dir, binary))

        # extracted files
        filename = os.path.join(target_dir, binary)
        if binary == "adb":
            os.chmod(filename, 0o755)
        print("done")

    os.rmdir(path=os.path.join(target_dir, 'platform-tools'))
    os.remove(path=archive_name)


def extract_archive_file(archive_file: str, file: str, destination_folder: str):
    """extracts specific file from archive file to destination folder"""
    extension = archive_file.rsplit('.', 1)[-1].lower()

    if extension == 'zip':
        with zipfile.ZipFile(archive_file, 'r') as archive:
            archive.extract(member=file, path=destination_folder)


if __name__ == '__main__':
    copy_binaries()
