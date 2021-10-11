import requests
from accesstoken import AccessToken


# ak、sk、bucket必需参数，limit范围1-1000
def Listv2(accessKey, secretKey, bucket, limit=1000, prefix=None, marker=None, delimiter=None):
    method = 'GET'
    path = "/v2/list?bucket=" + bucket + "&limit=" + str(limit)
    host = "rsf.qbox.me"
    contentType = "application/x-www-form-urlencoded"

    accessToken, body = AccessToken(accessKey, secretKey, method, path, host, contentType=contentType)
    # print("accessToken:", accessToken)
    url = "http://" + host + path
    header = {
        'Host': host,
        'Authorization': accessToken,
        'Content-Type': contentType
    }

    # headers传入值数据类型要求为dict
    res = requests.get(url, headers=header)
    # print("url:", url)
    return res.content


if __name__ == '__main__':
    accessKey = ''
    secretKey = ''
    bucket = 'theozhou'
    limit = 1
    prefix = None
    marker = None
    delimiter = None
    print(Listv2(accessKey, secretKey, bucket, limit=limit).decode('utf-8'))
