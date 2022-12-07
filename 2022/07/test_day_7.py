"""Unit tests for Day 7."""
from day_7 import build_file_system, get_directories, space_picker

COMMANDS = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".strip()


def test_build_file_system():
    """Test build_file_system."""
    root = build_file_system(COMMANDS)
    assert root.size == 48381165


def test_get_directories_under_100k():
    """Test the max-size directory filter."""
    root = build_file_system(COMMANDS)
    assert set(x.name for x in get_directories(root, 100000)) == set(("a", "e"))
    assert sum(x.size for x in get_directories(root, 100000)) == 95437


def test_space_picker():
    """Test the space picker."""
    root = build_file_system(COMMANDS)
    assert space_picker(root) == 24933642
