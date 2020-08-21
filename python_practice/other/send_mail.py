#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'

import smtplib
from email.mime.text import MIMEText

# msg = MIMEText('send by python...', 'plain', 'utf-8')
msg = MIMEText('<html><body><h1>Hello</h1>' + '<p>send by <a href="http://www.xuegod-for.cn/yum">python</a></body></html>', 'html', 'utf-8')
msg['From'] = "xiaoxin@qq.com"
msg["To"] = "xinlei@126.com"
msg["Subject"] = "python test"

server = smtplib.SMTP_SSL('smtp.qq.com', 465)
server.set_debuglevel(1)
server.login("xiaoxin@qq.com", "xxxxxx")
server.sendmail("xiaoxin@qq.com",["xinlei@126.com"],msg.as_string())
server.quit()
