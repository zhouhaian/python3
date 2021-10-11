import base64
import hmac
import time


# 生成私有空间文件下载url，url默认有效时间3600s
def DownloadURL(accessKey, secretKey, downloadUrl, expire=3600):
    deadline = int(time.time()) + expire
    downloadUrl = downloadUrl + '?e=' + str(deadline)

    # 签算结果需要base64url安全编码
    # hmac.new(key,data,算法)，key和data要求传入值为byte型
    Signature = hmac.new(secretKey.encode('utf-8'), downloadUrl.encode('utf-8'), digestmod='sha1')
    # base64.urlsafe_b64encode(data)，data要求传入值为byte型
    encodedSignature = base64.urlsafe_b64encode(Signature.digest())
    # print(encodedSignature)
    # DowanloadToken = AK:Signature
    Token = accessKey + ':' + encodedSignature.decode('utf-8')

    # 构建下载url
    pDownloadURL = downloadUrl + '&' + 'token=' + Token

    return pDownloadURL


if __name__ == '__main__':
    # 七牛账号AK/SK
    accessKey = ''
    secretKey = ''
    downloadUrl = 'http://kodo.qiniu.com/test.jpg'
    print(DownloadURL(accessKey, secretKey, downloadUrl))
