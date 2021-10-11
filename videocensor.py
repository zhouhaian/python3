import requests
from accesstoken import AccessToken


def VideoCensor(accessKey, secretKey, body):
    method = "POST"
    path = "/v3/video/censor"
    host = "ai.qiniuapi.com"
    contentType = "application/json"

    # 签算管理token以及将body从dict转成json格式
    accessToken, body = AccessToken(accessKey, secretKey, method, path, host, contentType=contentType, body=body)
    
    url = "http://" + host + path
    header = {
        'Host': host,
        'Authorization': accessToken,
        'Content-Type': contentType
    }

    res = requests.post(url, headers=header, data=body)

    return res.content


if __name__ == '__main__':
    # 七牛账号AK/SK
    accessKey = ''
    secretKey = ''
    body = {
        "data": {
            # 视频URL地址，必传参数，目前支持http和https
            "uri": 'https://test.kodo.com/test.mp4'
        },
        "params": {
            # 审核类型，必传参数，没有默认值，可选项：pulp/terror/politician。
            "scenes": ['pulp', 'terror', 'politician']
        }
    }

    print(VideoCensor(accessKey, secretKey, body))
