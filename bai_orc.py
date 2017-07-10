# 引入文字识别OCR SDK
from aip import AipOcr

# 定义常量
APP_ID = '9865717'
API_KEY = 'PGd4k97c2TZVIPc8uLo1M4o3'
SECRET_KEY = 'tutQkG0XvtTzFq3DEf6OOww7KGoMMTls'

# 初始化ApiOcr对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 初始化ApiOcr对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 定义参数变量
options = {
  'detect_direction': 'true',
  'language_type': 'CHN_ENG',
}

# 调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content('case_1.png'), options)
