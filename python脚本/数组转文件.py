import os
import re


# 创建文件夹 如果没有不会自动创建
def getFile(dir_name):
    if not os.path.exists(str(dir_name)):  # os模块判断并创建
        os.mkdir(dir_name)
    return dir_name

# 转换为md独立文件


def getMd():
    rstr = r"[\/\\\:\*\?\"\<\>\|\\\n\#\s]"  # '/ \ : * ? " < > |'  去除不合法文件名

    num = 1
    for md_name in http:
        md_name = re.sub(rstr, "_", md_name)  # 替换为下划线
        with open(dir_name+'/' + str(num)+'.' + md_name+'.md', 'a', encoding='UTF-8') as f:
            num += 1
            print('md_name')


if __name__ == "__main__":
    # 改变vue数组 和 文件名即可
    dir_name = '软技能'  # 文件名

    http = [
        "谈谈你对重构的理解",
        "什么样的前端代码是好的",
        "对前端⼯程师这个职位是怎么样理解的？它的前景会怎么样",
        "你觉得前端⼯程的价值体现在哪",
        "平时如何管理你的项⽬",
        "谈一谈组件封装",
        "前端⼀些常⻅问题",
    ]

    getFile(dir_name)
    getMd()
