"""Unit tests for Day 7."""
from day_7 import build_file_system, get_directories

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


def test_get_directories():
    """Test the max-size directory filter."""
    root = build_file_system(COMMANDS)
    assert set(x.name for x in get_directories(root)) == set(("a", "e"))
    assert sum(x.size for x in get_directories(root)) == 95437
