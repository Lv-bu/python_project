#-*-coding:utf-8-*-
""" Photo Sketching Using Python """
import cv2
img = cv2.imread("D:\girl.jpg")
## Image to Gray Image
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
## Gray Image to Inverted Gray Image
inverted_gray_image = 255-gray_image
## Blurring The Inverted Gray Image
blurred_inverted_gray_image = cv2.GaussianBlur(inverted_gray_image, (19,19),0)
## Inverting the blurred image
inverted_blurred_image = 255-blurred_inverted_gray_image
### Preparing Photo sketching
sketck = cv2.divide(gray_image, inverted_blurred_image,scale= 256.0)
cv2.imshow("Original Image",img)
cv2.imshow("Pencil Sketch", sketck)
cv2.waitKey(0)

"""
# 自动发送多封邮件
# 　　这个脚本可以帮助我们批量定时发送邮件，邮件内容、附件也可以自定义调整，非常的实用。
# 　　相比较邮件客户端，Python脚本的优点在于可以智能、批量、高定制化地部署邮件服务。
# 　　需要的第三方库：
# 　　· Email - 用于管理电子邮件消息
# 　　· Smtlib - 向SMTP服务器发送电子邮件，它定义了一个 SMTP 客户端会话对象，该对象可将邮件发送到互联网上任何带有 SMTP 或 ESMTP 监听程序的计算机
# 　　· Pandas - 用于数据分析清洗地工具

import smtplib  
from email.message import EmailMessage
import pandas as pd
def send_email(remail, rsubject, rcontent):
	email = EmailMessage()                          ## Creating a object for EmailMessage
	email['from'] = 'The Pythoneer Here'            ## Person who is sending
	email['to'] = remail                            ## Whom we are sending
	email['subject'] = rsubject                     ## Subject of email
	email.set_content(rcontent)                     ## content of email
	with smtplib.SMTP(host='smtp.gmail.com',port=587)as smtp:      
		smtp.ehlo()                                 ## server object
		smtp.starttls()                             ## used to send data between server and client
		smtp.login("deltadelta371@gmail.com","delta@371") ## login id and password of gmail
		smtp.send_message(email)                    ## Sending email
		print("email send to ",remail)              ## Printing success message
if __name__ == '__main__':
	df = pd.read_excel('list.xlsx')
	length = len(df)+1
	for index, item in df.iterrows():
		email = item[0]
		subject = item[1]
		content = item[2]
		send_email(email,subject,content)
"""



