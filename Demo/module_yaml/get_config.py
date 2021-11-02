
# from ruamel.yaml import YAML
import yaml

# 第一步: 创建YAML对象
# yaml = YAML(typ='safe')

# typ: 选择解析yaml的方式
#  'rt'/None -> RoundTripLoader/RoundTripDumper(默认)
#  'safe'    -> SafeLoader/SafeDumper,
#  'unsafe'  -> normal/unsafe Loader/Dumper
#  'base'    -> baseloader

# 第二步: 读取yaml格式的文件
with open('user_info.yaml', encoding='utf-8') as file:
    data = yaml.load(file,Loader=yaml.FullLoader)  # 为列表类型

print(f"data:\n{data}")
# user_data = data['user']
