# 抓取动态网页+json解析
# Network-->XHR刷新(往下滑动,第二个开始)-->Response字典格式-->data-->0-->middleURL-->复制Headers的Request URL
import requests
import json


# 打开百度图片壁纸
# http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1567133149621_R&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E5%A3%81%E7%BA%B8

# 回调函数
def main():
    count = 1
    # 抓取三百张图片
    for i in range(0, 33, 3):
        try:
            # 抓取页面信息
            url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%A3%81%E7%BA%B8&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=0&ic=0&hd=0&latest=0&copyright=0&word=%E5%A3%81%E7%BA%B8&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=wallpaper&pn={}0&rn=30&gsm=&1570847806698='.format(
                i)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
            response = requests.get(url, headers=headers).content.decode('utf-8')
            # print(response)

            # 解析json格式(转化为Python能识别的类型-字典类型)
            js = json.loads(response)
            # print(type(js))   # <class 'dict'>字典类型

            # 获取图片url
            # print(js['data'])
            for i in js['data']:
                # print(i)
                # print(i['middleURL'])
                img_url = i['middleURL']
                data = requests.get(img_url).content  # 如果保存二进制格式,数据必须是字节流
                # print(data)
                with open('./百度图片壁纸/{}.png'.format(count), 'wb') as f:
                    f.write(data)
                    print('保存%d张图片完成' % count)
                    count += 1
        except:
            continue


# 主函数
if __name__ == '__main__':
    main()
