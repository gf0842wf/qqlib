"""
QZone module
"""

from . import QQ
import time


class QZone(QQ):
    url_success = 'http://qzs.qq.com/qzone/v5/loginsucc.html?para=izone'
    url_feed = 'http://taotao.qzone.qq.com/cgi-bin/emotion_cgi_publish_v6'

    def g_tk(self):
        h = 5381
        cookies = self.session.cookies
        s = cookies.get('p_skey') or cookies.get('skey') or ''
        for c in s:
            h += (h << 5) + ord(c)
        return h & 0x7fffffff

    def feed(self, data):
        self.fetch(self.url_feed, params={
            'g_tk': self.g_tk(),
        }, data={
            'syn_tweet_verson': 1,
            'paramstr': 1,
            'pic_template': '',
            'richtype': '',
            'richval': '',
            'special_url': '',
            'subrichtype': '',
            'who': 1,
            'con': data,
            'feedversion': 1,
            'ver': 1,
            'ugc_right': 1,
            'to_tweet': 0,
            'to_sign': 0,
            'hostuin': self.user,
            'code_version': 1,
            'format': 'fs'
        })

    url_like_other = 'https://h5.qzone.qq.com/proxy/domain/w.qzone.qq.com/cgi-bin/likes/internal_dolike_app'  # ?g_tk={g_tk}&qzonetoken={qzonetoken}

    def like_other(self, other, unikey, curkey):
        self.fetch(self.url_like_other, params={'g_tk': self.g_tk()},
                   data={
                       'qzreferrer': 'http://user.qzone.qq.com/{user}'.format(user=other),
                       'opuin': self.user,
                       'unikey': unikey,
                       'curkey': curkey,
                       'from': '1',
                       'face': '0',
                       'query_count': '200',
                       'appid': '7030',
                       'fupdate': '1',
                       # 'zb_url': 'http://i.gtimg.cn/qzone/space_item/pre/3/72019_1.gif'
                   })


class MQZone(QZone):
    url_success = 'https://h5.qzone.qq.com/mqzone/index'
    url_feed = 'https://mobile.qzone.qq.com/mood/publish_mood'

    def feed(self, data):
        self.fetch(self.url_feed, params={
            'g_tk': self.g_tk(),
        }, data={
            'opr_type': 'publish_shuoshuo',
            'res_uin': self.user,
            'content': data,
            'richval': '',
            'lat': 0,
            'lon': 0,
            'lbsid': '',
            'issyncweibo': 0,
            'format': 'json',
        })
