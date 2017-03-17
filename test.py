# -*- coding: UTF-8 -*-
from qqlib import qzone
import qqlib


def login(qq, retry=3):
    exc = None
    # 自动重试登录
    for _ in xrange(retry):
        try:
            if exc is None:
                qq.login()
                return True
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
    if exc:
        return False
    else:
        return True


user = 100000
password = 'password'
qq = qzone.QZone(user, password)
# qq.attempt_cookie()
is_login = login(qq)
if is_login:
    qq.persist_cookie()
    # qq.feed('ai')
    # TODO: 检测空间是否能访问
    qq.like_other('otherqq',
                  'http://user.qzone.qq.com/otherqq',
                  'http://user.qzone.qq.com/otherqq')
else:
    print 'login failed'
