import base64
import hmac
import json
import time


# 七牛账号AK/SK
AccessKey = ''
SecretKey = ''


def UploadToken(bucket, key = None, deadline = None, policy = None):
    # 1）构建上传策略
    if key is None:
        scope = bucket
    else:
        scope = bucket + ":" + key

    if deadline is None:
        deadline = int(time.time()) + 3600

    PutPolicyDict = {"scope": scope, "deadline": deadline}

    if policy is not None:
        # dict()将2个dict数据合并，形成完整的上传策略
        PutPolicyDict = dict(PutPolicyDict, **policy)

    # json.dumps()，将dict型数据转成string型
    PutPolicy = json.dumps(PutPolicyDict, separators=(',', ':'))

    # base64.urlsafe_b64encode()需要传入值为byte型
    # 得到base64url安全编码后的上传策略
    encodedPutPolicy = base64.urlsafe_b64encode(PutPolicy.encode('utf-8'))

    # 2）计算签名-Signature
    # 签名使用HMAC-SHA1算法
    # 签名结果要求进行base64url安全编码
    Signature = hmac.new(SecretKey.encode('utf-8'), encodedPutPolicy, digestmod='sha1').digest()
    encodedSignature = base64.urlsafe_b64encode(Signature)

    # 3）构建上传凭证-UploadToken
    # UploadToken = AK:Signature:PutPolicy
    UploadToken = AccessKey + ':' + encodedSignature.decode('utf-8') + ':' + encodedPutPolicy.decode('utf-8')

    return UploadToken


bucket = 'test'
key = 'test.jpg'
policy = {"isPrefixalScope": 1}
deadline = 1627965292

print(UploadToken(bucket=bucket, key=key, deadline=deadline, policy=policy))
