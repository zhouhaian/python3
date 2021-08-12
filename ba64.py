import optparse
import base64


# urlsafe base64 编码
def base64en(data):
    # base64输入输出数据均为byte类型
    endata = base64.urlsafe_b64encode(data.encode('utf-8'))
    return endata.decode()


# urlsafe base64 解码
def base64de(data):
    dedata = base64.urlsafe_b64decode(data.encode('utf-8'))
    return dedata.decode()


# 命令行直接获取输入
# -e 表示编码，-d 表示解码
use = "python3 %prog -d <decode> -e <encode> target"
parser = optparse.OptionParser(use)
# python3 ba64.py -d xxxx
parser.add_option('-d', dest='decode', type='string', help='decode string')
# python3 ba64.py -e xxxx
parser.add_option('-e', dest='encode', type='string', help='encode string')
options, args = parser.parse_args()
# 输出结果转成dict，以便进行判断选择是编码还是解码操作
opt = eval(str(options))


# 判断选择编码还是解码操作
if opt["encode"] is None:
    # 解码
    print("")
    print("解码结果：")
    print(base64de(opt["decode"]))
    print("")
else:
    # 编码
    print("")
    print("编码结果：")
    print(base64en(opt["encode"]))
    print("")
