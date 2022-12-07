"""Day 7 of Advent of code 2022."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class File:
    """Represents a file object in a file system."""

    name: str
    size: int
    parent: Optional[Directory] = None


class Directory:
    """Represents a directory object in a file system."""

    def __init__(self, name: str, parent: Optional[Directory] = None):
        """Initialize a directory."""
        self.name = name
        self.parent = parent
        self.children: Dict[str, Directory | File] = {}

    def add_child(self, name: str) -> Directory:
        """Add a child to the directory."""
        self.children[name] = Directory(name, self)

    def add_file(self, name: str, size: int) -> File:
        """Add a file to the directory."""
        self.children[name] = File(name, size, self)

    @property
    def size(self) -> int:
        """Return the size of the directory."""
        return sum(child.size for child in self.children.values())


def build_file_system(commands: str) -> Directory:
    """Extract a file system from a terminal session."""
    cwd = Directory("/")
    for line in commands.splitlines():
        match line.split():
            case ["$", "cd", "/"]:
                continue
            case ["$", "cd", ".."]:
                cwd = cwd.parent
            case ["$", "cd", target]:
                if isinstance(cwd.children[target], Directory):
                    cwd = cwd.children[target]
            case ["$", "ls"]:
                continue
            case "dir", name:
                cwd.add_child(name)
            case size, name:
                cwd.add_file(name, int(size))
    while True:
        if cwd.parent is None:
            break
        cwd = cwd.parent
    return cwd


def get_directories(
    file_system: Directory, threshold: Optional[int] = None
) -> List[Directory | File]:
    """Walk a file system and return all directories that meet the threshold."""
    dirs = []
    if file_system.name == "/" and (not threshold or file_system.size <= threshold):
        dirs.append(file_system)
    if not hasattr(file_system, "children"):
        return dirs
    for child in file_system.children.values():
        if isinstance(child, Directory):
            if not threshold or child.size <= threshold:
                dirs.append(child)
            dirs.extend(get_directories(child, threshold))
    return dirs


def space_picker(file_system: Directory):
    """Find the smallest directory that exceeds the shortfall."""
    unused_space = 70000000 - file_system.size
    needed_space = 30000000
    shortfall = needed_space - unused_space
    directories = sorted(get_directories(file_system), key=lambda x: x.size)
    for directory in directories:
        if directory.size >= shortfall:
            return directory.size


if __name__ == "__main__":
    file_input = Path(__file__).parent / "input.txt"
    with open(file_input, "r", encoding="utf-8") as file:
        terminal_session = file.read().strip()
    root = build_file_system(terminal_session)
    directories_under_100k = get_directories(root, 100000)
    print(
        f"Total size of valid directories: {sum(x.size for x in directories_under_100k)}"
    )
    print("Size of directory that exceeds the shortfall:", space_picker(root))
