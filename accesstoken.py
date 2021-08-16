import base64
import hmac
import json


# 七牛账号AK/SK
AccessKey = ''
SecretKey = ''


# 生成管理token
def AccessToken(method, path, host, query=None, contenttype=None, body=None):
    # 1)构建待签名参数
    EntryString = method + ' ' + path + '\n' + 'Host: ' + host
    if contenttype is not None:
        EntryString = EntryString + '\n' + 'Content-Type: ' + contenttype
    EntryString = EntryString + '\n\n'
    if body is not None:
        body = json.dumps(body, separators=(',', ':'))
        EntryString = EntryString + body
    # print(EntryString)
    # print(body)

    # 2)计算签名
    Signature = hmac.new(SecretKey.encode('utf-8'), EntryString.encode('utf-8'), digestmod='sha1').digest()
    encodedSignature = base64.urlsafe_b64encode(Signature)

    # 3)构建管理token
    # AccessToken = Qiniu AK:Signature
    accessToken = "Qiniu " + AccessKey + ':' + encodedSignature.decode('utf-8')

    return accessToken, body


if __name__ == '__main__':
    # 七牛账号AK/SK
    AccessKey = ''
    SecretKey = ''
    method = "POST"
    path = "/facecompare"
    host = "face-compare.qiniuapi.com"
    contentType = "application/json"
    body = {
        "data_uri_a": "",
        "data_uri_b": ""
    }

    print(AccessToken(AccessKey, SecretKey, method, path, host, contenttype=contentType, body=body))

