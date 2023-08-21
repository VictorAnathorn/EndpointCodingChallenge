from .directory import Directory

class FileSystem:
    def __init__(self) -> None:
        self.root = Directory("")

    def execute_command(self, cmd: str) -> None:
        parts = cmd.split()
        action = parts[0]
        if action == "CREATE":
            self._create(parts[1])
        elif action == "LIST":
            self._list()
        elif action == "DELETE":
            self._delete(parts[1])
        elif action == "MOVE":
            self._move(parts[1], parts[2])

    def _create(self, path: str) -> None:
        self.root.add(path.split("/"))
        print(f"CREATE {path}")

    def _list(self) -> None:
        print("LIST")
        self.root.list()

    def _delete(self, path: str) -> None:
        print(f"DELETE {path}")
        if not self.root.delete(path.split("/")):
            print(f"Cannot delete {path} - {path.split('/')[0]} does not exist")            

    def _move(self, src: str, dest: str) -> None:
        dest_dir = self.root.find(dest.split("/"))
        if not dest_dir or not self.root.move(src.split("/"), dest_dir):
            print(f"Cannot move {src} - {src.split('/')[0]} does not exist")
        else:
            print(f"MOVE {src} {dest}")