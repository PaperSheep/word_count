# @Date    : 2018-10-16 12:22:28
# @Author  : PaperSheep 
# @Version : $Id$

import os
import requests
import re

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


# 获取html的源码
def get_html(target_url):
    url = target_url
    response = requests.get(url, headers=HEADER)
    response.encoding = 'utf-8'
    text = response.text
    response.close()
    return text


# 主函数
def main():
    while True:
        raw_url = input(' \n 把需要下载的音效链接复制进来 \n ')
        raw_html = get_html(raw_url)
        try:
            raw_music_url = re.findall(r'<source src="//(.*?)"></audio>', raw_html)[0]
            music_url = 'https://' + raw_music_url
            music_name = re.findall(r'<h1 class="works-name">(.*?)</h1>', raw_html)[0]
            # 判断文目录是否存在并创建
            if os.path.exists('musics')==False:
                os.mkdir('musics')
            with open('musics/{}.mp3'.format(music_name), 'wb') as f:
                response = requests.get(url=music_url, headers=HEADER)
                f.write(response.content)
            print(' \n 下载成功o(*￣▽￣*)ブ \n ')
        except:
            print('下载失败, 去问子洋爸爸情况')



# 调用主函数
if __name__ == '__main__':
    main()
