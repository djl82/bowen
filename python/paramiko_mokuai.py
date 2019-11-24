#!/usr/bin/python
#-*-coding:utf8-*-
# import paramiko
# #创建一个远程连接的客户端
# ssh_client = paramiko.SSHClient()
# #跳过验证的,不到Know_host 文件中查找
# #远程连接的IP会让你选择yes/no，这个解决的问题是自动选择yes
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# #连接服务器
# ssh_client.connect(hostname='192.168.10.98',port=22,username='root',password='123456')
# #执行操作   (stdin:执行命令,只能执行有结果的命令   stdout:执行结果   stderr:执行错误)
# stdin,stdout,stderr=ssh_client.exec_command('ls')
# result = stdout.read().decode('utf-8')
# print(result)
# #断开连接
# ssh_client.close()
# import paramiko
# #获取传输通道,以一个元组的形式输入ip和端口号
# tran = paramiko.Transport(('192.168.10.98',22))
# #输入用户名，密码，连接服务器
# tran.connect(username='root',password='123456')
# #创建一个stfp客户端
# sftp = paramiko.SFTPClient.from_transport(tran)
# #设置上传的本地路径/远程文件路径
# localPath = r'D:\python\py_1906\b.txt'    #本地路径
# remotePath = '/root/b.txt'   #远程路径
# #执行上传动作
# # sftp.put(localPath,remotePath)
# #执行下载动作
# sftp.get(remotePath,localPath)
# tran .close()