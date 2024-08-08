from faker import Faker
from faker.providers import BaseProvider

# 实例化并指定地区,不指定时默认 en_US (我需要中文的测试数据,所以选择zh_CN)
fake = Faker('zh_CN')


# 自定义provider
class CustomerProvider(BaseProvider):
    @staticmethod
    def gender():
        lists = ["男", "女"]
        index = fake.random_int(0, len(lists) - 1)
        return lists[index]

    @staticmethod
    def classIn():
        lists = ["17级测试1班", "17级测试2班", "17级测试3班", "17级测试4班", "17级测试5班"]
        index = fake.random_int(0, len(lists) - 1)
        return lists[index]

    @staticmethod
    def status():
        lists = ["正常", "停用"]
        index = fake.random_int(0, len(lists) - 1)
        return lists[index]


# 注册provider
fake.add_provider(CustomerProvider)

# 使用fake循环生成数据
data_total = [
    [
        fake.name(),
        fake.gender(),
        fake.classIn(),
        fake.random_number(10, 10),
        fake.phone_number(),
        fake.status()
    ] for x in range(30)
]


# 将数据写入文件
def write():
    # 首先打开文件 (file参数可以使用绝对路径或者相对路径; mode参数为w表示打开一个文件只用于写入.如果该文件已存在则打开文件,并从开头开始编辑,即原有内容会被删除.如果该文件不存在,创建新文件.)
    mock_file = open(file='C:/Users/chun/Desktop/mock_data.txt', mode='w', encoding='utf-8')
    for row in data_total:
        print(row)
        row_str = '{},{},{},{},{},{}'.format(row[0], row[1], row[2], row[3], row[4], row[5])
        mock_file.write(row_str)
        mock_file.write('\n')
    mock_file.close()
    print('文件写入结束')


write()
