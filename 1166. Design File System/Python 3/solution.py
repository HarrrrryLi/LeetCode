class FileSystem:

    def __init__(self):
        self.fs = {}

    def create(self, path: str, value: int) -> bool:
        directories = path.split('/')
        size = len(directories)

        current = self.fs
        print(directories)
        for idx in range(1, size - 1):
            directory = directories[idx]
            if directory not in current:
                return False
            current = current[directory]

        current[directories[-1]] = {'/': value}
        return True

    def get(self, path: str) -> int:
        directories = path.strip('/').split('/')
        current = self.fs

        for directory in directories:
            if directory not in current:
                return -1
            current = current[directory]

        return current['/']


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.create(path,value)
# param_2 = obj.get(path)
