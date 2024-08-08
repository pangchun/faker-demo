from faker import Faker
from faker.providers import BaseProvider

# 实例化并指定地区,不指定时默认 en_US (我需要中文的测试数据,所以选择zh_CN)
fake = Faker('zh_CN')


# 自定义provider【通过继承BaseProvider】
class CustomerProvider(BaseProvider):

    @staticmethod
    def faculty():
        lists = ["计算机系", "软件系", "数学系", "物理系", "化学系", "生物系", "经济系", "法学系", "历史系", "政治系"]
        index = fake.random_int(0, len(lists) - 1)
        return lists[index]


# 注册provider
fake.add_provider(CustomerProvider)

# 使用fake循环生成数据
data_total = [
    [
        fake.faculty(),
        '大一' + str(x+1) + '班'
    ] for x in range(4)
]


# 将数据写入文件
def write():
    # 首先打开文件 (file参数可以使用绝对路径或者相对路径; mode参数为w表示打开一个文件只用于写入.如果该文件已存在则打开文件,并从开头开始编辑,即原有内容会被删除.如果该文件不存在,创建新文件.)
    mock_file = open(file='C:/Users/chun/Desktop/mock_data.txt', mode='w', encoding='utf-8')
    print('文件写入开始')
    for row in data_total:
        print(row)
        row_str = '{},{}'.format(row[0], row[1])
        mock_file.write(row_str)
        mock_file.write('\n')
    mock_file.close()
    print('文件写入结束')


write()
