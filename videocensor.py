import requests
from accesstoken import AccessToken


def videocensor(accesskey, secretkey, body):
    method = "POST"
    path = "/v3/video/censor"
    host = "ai.qiniuapi.com"
    contentType = "application/json"

    # 签算管理token以及将body从dict转成json格式
    accesstoken, body = AccessToken(accesskey, secretkey, method, path, host, contenttype=contentType, body=body)
    
    url = "http://" + host + path
    header = {
        'Host': host,
        'Authorization': accesstoken,
        'Content-Type': contentType
    }

    res = requests.post(url, headers=header, data=body)

    return res.content


if __name__ == '__main__':
    # 七牛账号AK/SK
    AccessKey = ''
    SecretKey = ''
    body = {
        "data": {
            # 视频URL地址，必传参数，目前支持http和https
            "uri": ''
        },
        "params": {
            # 审核类型，必传参数，没有默认值，可选项：pulp/terror/politician。
            "scenes": ['pulp', 'terror', 'politician']
        }
    }
    
    print(videocensor(AccessKey, SecretKey, body))
