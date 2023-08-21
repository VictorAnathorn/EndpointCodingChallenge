from typing import List, Optional

class Directory:
    def __init__(self, name: str):
        self.name = name
        self.children: dict[str, 'Directory'] = {}

    def add(self, parts: List[str]) -> None:
        """
        Recursively add directories/subdirectories to the structure based on the given parts.
        """
        if not parts:
            return
        child_name = parts.pop(0)
        if child_name not in self.children:
            self.children[child_name] = Directory(child_name)
        self.children[child_name].add(parts)

    def find(self, parts: List[str]) -> Optional['Directory']:
        """
        Recursively find and return a directory based on the given parts. 
        Returns None if directory doesn't exist.
        """
        if not parts:
            return self
        child_name = parts.pop(0)
        return self.children.get(child_name, None) and self.children[child_name].find(parts)

    def delete(self, parts: List[str]) -> bool:
        """
        Recursively delete a directory based on the given parts. 
        Returns True if successful, False otherwise.
        """
        if len(parts) == 1:
            child_name = parts.pop(0)
            if child_name in self.children:
                del self.children[child_name]
                return True
            else:
                return False
        else:
            child_name = parts.pop(0)
            return child_name in self.children and self.children[child_name].delete(parts)

    def list(self, indent: int = -1) -> None:
        """
        Display the directory and its children recursively, with indentation for hierarchical structure.
        """
        if self.name:
            print("  " * indent + self.name)
        for child_name in sorted(self.children.keys()):
            self.children[child_name].list(indent + 1)

    def move(self, src_parts: List[str], dest_dir: 'Directory') -> bool:
        """
        Recursively move a directory (based on src_parts) to another directory (dest_dir).
        Returns True if successful, False otherwise.
        """
        if len(src_parts) == 1:
            child_name = src_parts.pop(0)
            if child_name in self.children:
                dest_dir.children[child_name] = self.children[child_name]
                del self.children[child_name]
                return True
            else:
                return False
        else:
            child_name = src_parts.pop(0)
            return child_name in self.children and self.children[child_name].move(src_parts, dest_dir)