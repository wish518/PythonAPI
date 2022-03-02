import SettingData
import email.message
import smtplib
class Email: 
    def SendGmail(self,To,Subject,body):
        try:
           EmailSetting=email.message.EmailMessage()
           EmailSetting["From"]='Service@TrueEqual.one'
           EmailSetting["To"]=To
           EmailSetting["Subject"]=Subject
           EmailSetting.add_alternative(body,subtype="html") #HTML信件內容

           server=smtplib.SMTP_SSL("smtp.gmail.com",465) #建立gmail連驗
           server.login(SettingData.GmailAcc,SettingData.GmailPassWord)
           server.send_message(EmailSetting)
           server.close()
           return {"Code":"000"}
        except Exception as e:
           return {"Code":"800","Msg":e.args[0]}