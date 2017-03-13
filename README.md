qqlib
===

Python版QQ登录库，兼容Python2.x和Python3.x。

安装
---
``` sh
sudo pip install git+https://github.com/gf0842wf/qqlib.git -t .
```

高级用法
---
``` python
def login(qq):
    # 不考虑验证码的情况，直接登录
    qq.login()

import qqlib
qq = qqlib.QQ(12345678, 'password')
login(qq)
print('Hi, %s' % qq.nick)
```

登录时有可能出现需要验证码的情况，这时可以捕获`qqlib.NeedVerifyCode`错误并从中获取验证码图片（`exc.verifier.fetch_image()`）进行处理，验证（`exc.verifier.verify(code)`）之后再继续登录。下面是支持输入验证码的`login`方法：
``` python
# -*- coding: UTF-8 -*-

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
                    print('Error:', exc.message)
                verifier = exc.verifier
                open('verify.jpg', 'wb').write(verifier.fetch_image())
                print('验证码已保存到verify.jpg')
                # 输入验证码
                vcode = raw_input('请输入验证码：')
                verifier.verify(vcode)
                exc = None
        except qqlib.NeedVerifyCode as e:
            exc = e

import qqlib
qq = qqlib.QQ(123456, 'password.')
login(qq)
print('Hi, %s' % qq.nick)
```

QZone：
``` python
from qqlib import qzone
qq = qzone.QZone(12345678, 'password')
# 登录流程同上
login(qq)
qq.feed('发一条说说')
```
