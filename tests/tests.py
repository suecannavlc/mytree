import pytest

from mytree import DirectoryTree


def test_full_path():
    tree = DirectoryTree('test_data')
    tree.generator.generate()


def test_only_file():
    assert True


def test_only_subdir():
    assert True
