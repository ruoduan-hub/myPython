from removebg import RemoveBg
import os

# 参数填入 api-key, 错误日志路径 
rmbg = RemoveBg("H11PQF7gGT97VxhJEhgcxNeP", "./error.log")

# 处理后的图片存放位置
path = os.path.join(os.getcwd(), "pic")

for pic in os.listdir(path):
    rmbg.remove_background_from_img_file(os.path.join(path, pic))