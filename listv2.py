import requests
from accesstoken import AccessToken


# ak、sk、bucket必需参数，limit范围1-1000
def listv2(accesskey, secretkey, bucket, limit=1000, prefix=None, marker=None, delimiter=None):
    method = 'GET'
    path = "/v2/list?bucket=" + bucket + "&limit=" + str(limit)
    host = "rsf.qbox.me"
    contentType = "application/x-www-form-urlencoded"

    accesstoken, body = AccessToken(accesskey, secretkey, method, path, host, contenttype=contentType)
    
    url = "http://" + host + path
    header = {
        'Host': host,
        'Authorization': accesstoken,
        'Content-Type': contentType
    }

    # headers传入值数据类型要求为dict
    res = requests.get(url, headers=header)
    # print("accesstoken:", accesstoken)
    # print("url:", url)
    return res.content


if __name__ == '__main__':
    access_key = ''
    secret_key = ''
    bucket_name = ''
    limit = 1
    prefix = None
    marker = None
    delimiter = None
    print(listv2(access_key, secret_key, bucket_name, limit=limit))
