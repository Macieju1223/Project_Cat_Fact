from dotenv import load_dotenv
import smtplib
import os
from .mongo_db import mydb
load_dotenv()

def send_email(title,content):

    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(os.getenv('MAIL_ADDR'),os.getenv('PASSWORD'))

        mail_content = f"Subject: {title}\n{content}"
        mails = list(mydb.mails.find({}))
        num = 1
        for mail in mails:
            try:
                smtp.sendmail(os.getenv('MAIL_ADDR'),mail[str(num)]['email'],mail_content)
            except OSError:
                print(f"{mail} error occured")
            num += 1
        smtp.quit()
        return {"Satus" : 200}
