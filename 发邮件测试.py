#https://www.liaoxuefeng.com/wiki/1016959663602400/1017790702398272
#https://blog.csdn.net/MATLAB_matlab/article/details/106240424
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
#发送
fromAddr="405628079@qq.com"
password= "d"#"gydcnchvjdvybjfb"
toAddr=["sliz@qq.com","starlizhi@gmail.com"]

msg=MIMEMultipart();
msg.attach(MIMEText("str from py","plain","utf-8"))
msg["Subject"]="主题"
msg["From"]=fromAddr
msg["To"]=",".join(toAddr)

server=smtplib.SMTP_SSL("smtp.qq.com",465)
server.login(fromAddr,password)

server.set_debuglevel(1)
server.login(fromAddr,password)
server.sendmail(fromAddr,toAddr,msg.as_string())
server.quit()
