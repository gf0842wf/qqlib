# -*- coding: UTF-8 -*-
from qqlib import qzone
import qqlib


def login(qq):
    exc = None
    # 自动重试登录
    while True:
        try:
            if exc is None:
                qq.login()
                break
            else:
                if exc.message:
                    print 'Error:', exc.message
                verifier = exc.verifier
                open('verify.jpg', 'wb').write(verifier.fetch_image())
                print '验证码已保存到verify.jpg'
                # 输入验证码
                vcode = raw_input('请输入验证码：')
                verifier.verify(vcode)
                exc = None
        except qqlib.NeedVerifyCode as e:
            exc = e


qq = qzone.QZone(980993313, 'flg829506--')
login(qq)
qq.feed('test feed')
