#!/usr/bin/env python
# _*_ coding: utf-8 _*_

################################################
# python 3.7
################################################

import smtplib
from email.mime.text import MIMEText


# SMTP Server/HOST
SMTPServer = "smtp.163.com"
# SMTP port, mail port, generally 25.
SMTPPort = 25
# Sender mail address
SenderAddr = "xxxxxxxxxxxxxxxxxx"
# mail box SMTP authority password
SenderPwd = "xxxxxxxxxxxx"

rawMessage = "Tom is a good man, this mail was sent by Python!"
message = MIMEText(rawMessage)
message["Subject"] = "FYI"
message["From"] = SenderAddr

if __name__ == "__main__":
    mailReceiver = "yyyyyyyyyyyyy@163.com"
    # create SMTP Server
    try:
        mailServer = smtplib.SMTP(SMTPServer, SMTPPort)
        # login
        mailServer.login(SenderAddr, SenderPwd)
        # Send mail
        mailServer.sendmail(SenderAddr, [mailReceiver, SenderAddr], message.as_string())
        # logout
        mailServer.quit()
    except Exception as e:
        print(e)
    pass
