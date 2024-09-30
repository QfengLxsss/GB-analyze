import re

# 读取文件内容
with open('sequence.gb', 'r') as file:
    content = file.read()

# 使用正则表达式查找并删除 translation 部分
content = re.sub(r'translation\s*=\s*".*?"', '', content, flags=re.DOTALL)

# 将修改后的内容写回文件
with open('sequence.gb', 'w') as file:
    file.write(content)