from faker import Faker

# 实例化并指定地区,不指定时默认 en_US (我需要中文的测试数据,所以选择zh_CN)
fake = Faker('zh_CN')

# 使用fake循环生成数据
data_total = [
    [
        x + 1,
        fake.name(),
        fake.random_int(0, 100),
        fake.job(),
        fake.phone_number(),
        fake.company(),
        fake.address(),
        fake.date_of_birth().strftime("%Y-%m-%d %H:%M:%S"),
        fake.ssn()
    ] for x in range(1000)
]


# 将数据写入文件
def write():
    # 首先打开文件 (file参数可以使用绝对路径或者相对路径; mode参数为w表示打开一个文件只用于写入.如果该文件已存在则打开文件,并从开头开始编辑,即原有内容会被删除.如果该文件不存在,创建新文件.)
    mock_file = open(file='C:/Users/chun/Desktop/mock_data.sql', mode='w', encoding='utf-8')
    for row in data_total:
        print(row)
        row_str = '{},{},{},{},{},{},{},{},{}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                                      row[8])
        mock_file.write(row_str)
        mock_file.write('\n')
    mock_file.close()
    print('文件写入结束')


write()
