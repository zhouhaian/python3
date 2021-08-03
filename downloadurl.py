import base64
import hmac
import time

# 七牛账号AK/SK
AccessKey = ''
SecretKey = ''


# 生成私有空间文件下载url，url默认有效时间3600s
def DownloadURL(DownloadUrl, expire=3600):
    deadline = int(time.time()) + expire
    DownloadUrl = DownloadUrl + '?e=' + str(deadline)

    # 签算结果需要base64url安全编码
    # hmac.new(key,data,算法)，key和data要求传入值为byte型
    Signature = hmac.new(SecretKey.encode('utf-8'), DownloadUrl.encode('utf-8'), digestmod='sha1')
    # base64.urlsafe_b64encode(data)，data要求传入值为byte型
    encodedSignature = base64.urlsafe_b64encode(Signature.digest())
    # print(encodedSignature)
    # 构建下载凭证AK:Signature
    Token = AccessKey + ':' + encodedSignature.decode('utf-8')

    # 构建下载url
    PDownloadURL = DownloadUrl + '&' + 'token=' + Token

    return PDownloadURL


DownloadUrl = 'http://kodo.qiniu.com/test.jpg'
print(DownloadURL(DownloadUrl, expire=3600))
