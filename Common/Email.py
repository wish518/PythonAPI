import SettingData
import email.message
import smtplib
class Email: 
    def SendGmail(self,To,Subject,body):
        try:
           EmailSetting=email.message.EmailMessage()
           EmailSetting["Form"]='Service@TrueEqual.one'
           EmailSetting["To"]=To
           EmailSetting["Subject"]=Subject
           EmailSetting.add_alternative(body,subtype="html") #HTML信件內容

           server=smtplib.SMTP_SSL("smtp.gmail.com",465) #建立gmail連驗
           server.login(SettingData.GmailAcc,SettingData.GmailPassWord)
           server.send_message(EmailSetting)
           server.close()
           return True
        except Exception as e:
           return False