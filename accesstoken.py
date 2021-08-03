import base64
import hmac


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
        EntryString = EntryString + body
    # print(EntryString)

    # 2)计算签名
    Signature = hmac.new(SecretKey.encode('utf-8'), EntryString.encode('utf-8'), digestmod='sha1').digest()
    encodedSignature = base64.urlsafe_b64encode(Signature)

    # 3)构建管理token
    # AccessToken = Qiniu AK:Signature
    accessToken = "Qiniu " + AccessKey + ':' + encodedSignature.decode('utf-8')

    return accessToken


method = "POST"
path = "/move/dGVzdDpoYWxvLmpwZw==/dGVzdDp0ZXN0LmpwZw=="
host = "rs.qbox.me"
contentType = "application/x-www-form-urlencoded"


print(AccessToken(method, path, host, contenttype=contentType))
