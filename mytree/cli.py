import argparse
import pathlib
import sys

from tree_generator import TreeGenerator
from tree_output import TreeOutput

from . import __version__


def main():
    args = parse_cmd_args()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified directory doesn't exist")
        sys.exit()
    tree = TreeGenerator(root_dir)
    tree.generate()


def parse_cmd_args():
    parser = argparse.ArgumentParser(
        prog='mytree',
        description='improved version of Real Python tree generator',
        epilog='work on progress!'
    )
    parser.version = f'mytree version is {__version__}'
    parser.add_argument('-v', '--version', action='version')
    parser.add_argument(
        'root_dir',
        metavar='ROOT_DIR',
        nargs='?',
        default='.',
        help='Generated a full directory tree starting at ROOT_DIR'
    )
    return parser.parse_args()
