import os


class CountFile:
    """
    计算根并且列举所有文件名，
    放入list目录所有文件的数量
    """
    count = 0
    listWithPath = []
    list = []

    @staticmethod
    def switchParentDir():
        """
        切换到上一级目录（根目录）
        """
        parent_dir = os.path.dirname(os.getcwd())
        os.chdir(parent_dir)

    def counting(self, path: str):
        """
        开始统计根目录
        :return: int
        """
        sub_files = os.listdir(path)
        print(sub_files)
        for f in sub_files:
            cur_name = f'{path}/{f}'
            if os.path.isdir(f):
                self.counting(cur_name)
                continue

            self.count += 1
            self.listWithPath.append(cur_name)
            self.list.append(f)


countFile = CountFile()
countFile.switchParentDir()
countFile.counting(os.getcwd())
print(f"文件总数量： {countFile.count}")
print(f"所有文件List ： {countFile.list}")
