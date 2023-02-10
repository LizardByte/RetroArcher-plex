#!/usr/bin/env python2.7
import os
import subprocess
import sys


def main():
    # update pip
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

    # install agent requirements
    shared_directory = os.path.join('Contents', 'Libraries', 'Shared')

    subprocess.check_call([
        sys.executable, '-m', 'pip', 'install', '--upgrade', '--target=%s' % shared_directory, '-r',
        os.path.join(shared_directory, 'requirements.txt'), '--no-warn-script-location'
    ])


if __name__ == '__main__':
    main()
