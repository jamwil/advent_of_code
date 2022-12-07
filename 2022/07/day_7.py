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


def get_directories(file_system: Directory) -> List[Directory | File]:
    """Walk a file system and return all directories that meet the threshold."""
    dirs = []
    if not hasattr(file_system, "children"):
        return dirs
    for child in file_system.children.values():
        if isinstance(child, Directory):
            if child.size < 100000:
                dirs.append(child)
            dirs.extend(get_directories(child))
    return dirs


if __name__ == "__main__":
    file_input = Path(__file__).parent / "input.txt"
    with open(file_input, "r", encoding="utf-8") as file:
        terminal_session = file.read().strip()
    root = build_file_system(terminal_session)
    valid_directories = get_directories(root)
    print(f"Total size of valid directories: {sum(x.size for x in valid_directories)}")
