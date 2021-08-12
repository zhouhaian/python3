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

    return accessToken


method = "POST"
path = "/v3/video/censor"
host = "ai.qiniuapi.com"
contentType = "application/json"
body = {
    "data": {
        "uri": 'https://'
        # 视频URL地址，目前支持http和https。
    },
    "params": {
        # 审核类型，必填字段，没有默认值，可选项：pulp/terror/politician。
        "scenes": ['pulp', 'terror', 'politician']
    }
}

print(AccessToken(method, path, host, contenttype=contentType, body=body))
