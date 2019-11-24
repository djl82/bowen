#!/usr/bin/python
#-*-coding:utf8-*-
# #1.封装了smtp协议   导入相关的库和方法
# import smtplib
# #处理邮件中的组成部分  负责构建文本
# from email.mime.text import MIMEText
# # #负责构件图片
# # from email.mime.image import MIMEImage
# #处理邮件中的中文  负责将多个对象集合起来
# from email.mime.multipart import MIMEMultipart
#
# '''2.设置邮箱域名，发件人和收件人邮箱，发件人邮箱授权码'''
# #设置邮箱域名,smtp服务器，这里使用的163邮箱
# mail_host = 'smtp.163.com'
# #发件人邮箱
# mail_sender = '18738481350@163.com'
# #邮箱授权码，注意这里不是邮箱密码，licence:许可证
# mail_licence = '123djl'
# #收件人邮箱，可以为多个收件人
# mail_receivers = ['1179134482@qq.com',
#                   '826379642@qq.com'
#                   ]
#
# '''3.创建一个空邮件，这里面可以添加文本，图片，附件'''
# message = MIMEMultipart()
#
# '''4.设置邮件头部内容'''
# #设置邮件主题
# message['subject'] = '这是我测试的第一封邮件'
# #设置发送者
# message['from'] = mail_sender
# #设置邮件接收者
# message['to'] = str(mail_receivers)
#
# '''5.添加正文文本'''
# #邮件正文内容
# text = '这一个月，我给胖子过几个电话，对方提示暂停使用。胖子人在巴乃，冲电话费不方便，于是我往他卡里充了两百块钱，又打了几次，都是关机，于是只能打巴乃村里的电话，向阿贵询问胖子的情况。'
# #处理文本
# info_text = MIMEText(text)
# #向MIMEMultipart对象中添加文本对象
# message.attach(info_text)
#
# '''6.添加图片'''
# # #使用open读取图片
# # image_data = open('12.jpg', 'rb')
# # #处理图片
# # info_image = MIMEImage(image_data.read())
# # #关闭打开的图片文件
# # image_data.close()
# # #添加图片文件到邮件信息当中去
# # message.attach(info_image)
#
# #定义发送的附件的文件名，文件可以是任何格式的
# att1 =MIMEText(open('12.jpg', 'rb').read(), 'base64', 'utf-8')
# #附件携带的字段和值
# att1["Content-Type"] = 'application/octet-stream'
# #附件携带的字段和值   这里的filename可以任意写，写什么名字，邮件中就显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="aaa.jpg"'
# #将附件添加到邮件里
# message.attach(att1)
#
# '''7.发送邮件'''
# #创建smtp对象    设置发件人邮件的域名和端口，端口地址为465
# stp = smtplib.SMTP_SSL(mail_host, 465)
# #登录邮箱
# stp.login(mail_sender,mail_licence)
# #发送邮件
# stp.sendmail(mail_sender,mail_receivers,message.as_string())
# print('邮件发送成功')
# #关闭smtp对象
# stp.close()