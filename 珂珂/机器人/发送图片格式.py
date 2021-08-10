# 1.企业微信群->添加群机器人
# Webhook地址：https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=637d4b8d-9749-4ba4-bf85-df7956e72639

import base64
import hashlib
import requests


class Send:
    def __init__(self, wx_key=None):
        """
        :param wx_key: 企业微信机器人秘钥
        """
        if wx_key is None:
            wx_key = '637d4b8d-9749-4ba4-bf85-df7956e72639'

        self.WX_TYPE = 'send'

        # 机器人唯一标识
        self.WX_KEY = wx_key

        # 机器人url,需要传参
        self.WX_URL = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/{0}?key={1}'

    # 发送图片
    def send_image(self, wx_image):
        """
        企业微信发送图片
        :param wx_image:
        :return:
        """
        # 要发送的图片
        send_image = wx_image

        # 图片base64码
        with open(send_image, "rb") as f:
            base64_data = base64.b64encode(f.read())
            data = base64_data.decode()
        # print(data)

        # 图片的md5值
        file = open(send_image, "rb")
        md = hashlib.md5()
        md.update(file.read())
        res1 = md.hexdigest()
        # print(res1)

        # 图片类型  图片（base64编码前）最大不能超过2M，支持JPG,PNG格式
        string_image = {
            # 消息类型，此时固定为image
            "msgtype": "image",
            "image": {
                # 图片内容的base64编码
                "base64": data,
                # 图片内容（base64编码前）的md5值
                "md5": res1
            }
        }

        # 请求函数  format格式化
        res = requests.post(self.WX_URL.format(self.WX_TYPE, self.WX_KEY), json=string_image)
        response = res.json()['errmsg']
        # print(response)

        return '推送成功' if response == 'ok' else '推送失败'


if __name__ == '__main__':
    send = Send()
    massage_image = send.send_image(wx_image=r"D:\其它\桌面壁纸.jpg")
    print(massage_image)
