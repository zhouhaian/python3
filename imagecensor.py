import requests
import json
from accesstoken import AccessToken


def ImageCensor(accessKey, secretKey, body):
    method = "POST"
    path = "/v3/image/censor"
    host = "ai.qiniuapi.com"
    contentType = "application/json"

    # 签算管理token以及将body从dict转成json格式
    accesstoken, body = AccessToken(accessKey, secretKey, method, path, host, contentType=contentType, body=body)
    # print(accesstoken)

    url = "http://" + host + path
    header = {
        'Host': host,
        'Content-Type': contentType,
        'Authorization': accesstoken
    }

    res = requests.post(url, headers=header, data=body)

    return res.content


if __name__ == '__main__':
    # 七牛账号AK/SK
    accessKey = ''
    secretKey = ''
    body = {
        "data": {
            # 图片URL地址，必传参数，目前支持http和https
            "uri": 'http://test.qiniu.com/test.png'
        },
        "params": {
            # 审核类型，必传参数，没有默认值，可选项：pulp/terror/politician。
            "scenes": ['pulp']
        }
    }

    print(ImageCensor(accessKey, secretKey, body))
