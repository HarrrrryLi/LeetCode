class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        record = {'end': False}

        for directory in folder:
            subdirs = directory.split('/')
            if not subdirs:
                return ['/']

            cur = record
            idx = 0
            size = len(subdirs)

            while idx < size:
                subdir = subdirs[idx]
                if not subdir:
                    idx += 1
                    continue
                if subdir not in cur:
                    result.append('/'.join(subdirs))
                    while idx < size:
                        subdir = subdirs[idx]
                        if subdir:
                            cur[subdir] = {'end': False}
                            cur = cur[subdir]
                        idx += 1
                    cur['end'] = True
                else:
                    cur = cur[subdir]
                    if cur['end']:
                        break

                    idx += 1
        return result
