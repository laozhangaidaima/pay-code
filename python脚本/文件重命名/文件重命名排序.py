import os
import re


# 获取该目录下所有文件，存入列表中
def getFile(dir_name):
    if not os.path.exists(str(dir_name)):  # os模块判断并创建
        os.mkdir(dir_name)
    return dir_name


path = './list/'
newPath = './newList/'

getFile(newPath)


fileList = os.listdir(path)
n = 0
for i in fileList:

    # 设置旧文件名（就是路径+文件名）
    oldname = path + os.sep + fileList[n]   # os.sep添加系统分隔符

    # 设置新文件名
    # newname = path + os.sep + 'a'+str(n+1)+'.JPG'
    rstr = r"[\d+\.?\d*.md]"  # 去除数字
    fileList[n] = re.sub(rstr, "", fileList[n])  # 替换为下划线
    print('fileList[n]', fileList[n])

    newname = newPath + str(n+1)+str('.') + fileList[n]+str('.md')

    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名

    n += 1
