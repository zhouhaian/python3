import base64
import hmac
import json


# 生成管理token
def AccessToken(accessKey, secretKey, method, path, host, contentType=None, body=None):
    # 1)构建待签名参数
    """
        <Method> <Path>
        Host: <Host>
        Content-Type: <ContentType>
        [<Body>]
    """
    EntryString = method + ' ' + path + '\n' + 'Host: ' + host
    if contentType is not None:
        EntryString = EntryString + '\n' + 'Content-Type: ' + contentType
    EntryString = EntryString + '\n\n'
    # <Body> 只有在 <ContentType> 存在且不为 application/octet-stream 时才签进去。
    if contentType is not None and contentType != "application/octet-stream":
        body = json.dumps(body, separators=(',', ':'), ensure_ascii=False)
        EntryString = EntryString + body
    # print(body)

    # 2)计算签名
    Signature = hmac.new(secretKey.encode('utf-8'), EntryString.encode('utf-8'), digestmod='sha1').digest()
    encodedSignature = base64.urlsafe_b64encode(Signature)

    # 3)构建管理token
    # AccessToken = Qiniu AK:Signature
    accessToken = "Qiniu " + accessKey + ':' + encodedSignature.decode('utf-8')

    return accessToken, body


if __name__ == '__main__':
    # 七牛账号AK/SK
    accessKey = ''
    secretKey = ''
    method = "POST"
    path = "/v1/namespaces"
    host = "qvs.qiniuapi.com"
    contentType = "application/json"
    body = {
    }

    print(AccessToken(accessKey, secretKey, method, path, host, contentType=contentType, body=body))
