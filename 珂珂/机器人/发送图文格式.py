# 1.企业微信群->添加群机器人
# Webhook地址：https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=637d4b8d-9749-4ba4-bf85-df7956e72639

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

    # 发送图文
    def send_title(self, wx_title, wx_description, wx_url, wx_picurl):
        """
        企业微信发送图文
        :param wx_title:
        :param wx_description:
        :param wx_url:
        :param wx_picurl:
        :return:
        """
        # 要发送的内容
        send_title = wx_title
        send_description = wx_description
        send_url = wx_url
        send_picurl = wx_picurl

        headers = {'Content-Type': 'application/json'}

        # 图文类型
        string_news = {
            # 消息类型，此时固定为news
            "msgtype": "news",
            "news": {
                # 图文消息，一个图文消息支持1到8条图文
                "articles": [
                    {
                        # 标题，不超过128个字节，超过会自动截断
                        "title": send_title,
                        # 描述，不超过512个字节，超过会自动截断
                        "description": send_description,
                        # 点击后跳转的链接
                        "url": send_url,
                        # 图文消息的图片链接，支持JPG、PNG格式，较好的效果为大图 1068 * 455，小图150 * 150。
                        "picurl": send_picurl
                    }
                ]
            }
        }

        # 请求函数  format格式化
        res = requests.post(self.WX_URL.format(self.WX_TYPE, self.WX_KEY), json=string_news, headers=headers)
        response = res.json()['errmsg']
        # print(response)

        return '推送成功' if response == 'ok' else '推送失败'


if __name__ == '__main__':
    send = Send()
    title = "中秋节礼品领取"
    description = "今年中秋节公司有豪礼相送"
    url = "www.qq.com"
    picurl = "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
    massage_image = send.send_title(wx_title=title, wx_description=description, wx_url=url, wx_picurl=picurl)
    print(massage_image)
