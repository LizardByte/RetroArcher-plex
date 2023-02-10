import os
import subprocess
import sys


def main():
    # update pip
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

    # install agent requirements
    shared_directory = os.path.join('Contents', 'Libraries', 'Shared')
    # this doesn't install dependencies of requirements...
    subprocess.check_call([
        sys.executable, '-m', 'pip', 'install', '--upgrade', f'--target={shared_directory}', '-r',
        os.path.join(shared_directory, 'requirements.txt'), '--no-warn-script-location', '--python-version', '2.7',
        '--no-deps', '--ignore-requires-python'
    ])

    # install retroarcher requirements
    modules_directory = os.path.join('Contents', 'Libraries', 'Modules')
    subprocess.check_call([
        sys.executable, '-m', 'pip', 'install', '--upgrade', f'--target={modules_directory}', '-r',
        os.path.join(modules_directory, 'requirements.txt'), '--no-warn-script-location'
    ])


if __name__ == '__main__':
    main()
