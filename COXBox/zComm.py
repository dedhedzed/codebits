# zcomm beta 2023 zed industries - zed@zed.industries

import smtplib
import re
import random
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class CarrierGateway:
    def send(self, carrier, to, message):
        self.us_gateways = {
            "att": {"sms": "{number}@txt.att.net", "mms": "{number}@mms.att.net"},
            "tmobile": {"sms": "{number}@tmomail.net", "mms": "{number}@tmomail.net"},
            "verizon": {"sms": "{number}@vtext.com", "mms": "{number}@vzwpix.com"},
            "sprint": {"sms": "{number}@messaging.sprintpcs.com", "mms": "{number}@pm.sprint.com"},
            "boost": {"sms": "{number}@sms.myboostmobile.com", "mms": "{number}@myboostmobile.com"},
            "cricket": {"sms": "{number}@sms.cricketwireless.net", "mms": "{number}@mms.cricketwireless.net"},
            "googlefi": {"sms": "{number}@msg.fi.google.com", "mms": "{number}@msg.fi.google.com"},
            "republic": {"sms": "{number}@text.republicwireless.com", "mms": "none"},
            "straight": {"sms": "{number}@vtext.com", "mms": "{number}@mypixmessages.com"},
            "ting": {"sms": "{number}@message.ting.com", "mms": "none"},
            "tracfone": {"sms": "scout notice?", "mms": "{number}@mmst5.tracfone.com"},
            "uscellular": {"sms": "{number}@email.uscc.net", "mms": "{number}@mms.uscc.net"},
            "virginus": {"sms": "{number}@vmobl.com", "mms": "{number}@vmpix.com"},
        }
        self.canadian_gateways = {
            "rogers": {"sms": "{number}@pcs.rogers.com", "mms": "{number}@mms.rogers.com"},
            "bell": {"sms": "{number}@txt.bell.ca", "mms": "{number}@mms.bell.ca"},
            "telus": {"sms": "{number}@msg.telus.com", "mms": "{number}@mms.telus.com"},
            "fido": {"sms": "{number}@fido.ca", "mms": "{number}@mms.fido.ca"},
            "koodo": {"sms": "{number}@msg.koodomobile.com", "mms": "{number}@mms.koodomobile.com"},
            "virgin": {"sms": "{number}@vmobile.ca", "mms": "{number}@vmobile.ca"},
            "aliant": {"sms": "{number}@sms.wirefree.informe.ca", "mms": "none"},
            "pc": {"sms": "{number}@mobiletxt.ca", "mms": "none"},
            "sasktel": {"sms": "{number}@pcs.sasktelmobility.com", "mms": "none"},
            "freedom": {"sms": "{number}@txt.freedommobile.ca", "mms": "none"},           
        }

        if not re.match(r"^\d{10}$", to):
            print("Invalid phone number! Use a 10-digit North American phone number.")
            return

        region = input("Would you like to send to the US or Canada? ").lower()
        while region not in ["us", "canada"]:
            print("Invalid option. Try again.")
            region = input("Would you like to send to the US or Canada? ").lower()

        gateways = self.us_gateways if region == "us" else self.canadian_gateways
        if carrier not in gateways:
            return "Unrecognized carrier!"

        service = input("Would you like to send an SMS or MMS? ").lower()
        while service not in gateways[carrier].keys():
            print("Invalid option. Try again.")
            service = input("Would you like to send an SMS or MMS? ").lower()

        to = gateways[carrier][service].format(number=to)
        msg = MIMEMultipart() if service == "mms" else MIMEText(message)

if service == "mms":
    image_path = input("Enter the file path to the image: ")
    with open(image_path, "rb") as f:
        image = MIMEImage(f.read())
        msg.attach(image)

msg['Subject'] = random.choice([
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Vestibulum molestie facilisis velit vel laoreet.",
    "Nam posuere bibendum est, ac commodo sapien feugiat vel.",
    "Morbi porta risus vitae nulla malesuada bibendum.",
    "Fusce suscipit, velit vel congue placerat, quam velit vestibulum sem.",
])
msg = MIMEMultipart()
        msg["From"] = "your-email-address@example.com"
        msg["To"] = to
        msg["Subject"] = "Text message"

        msg.attach(MIMEText(message))

        try:
            smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login("your-email-address@example.com", "your-email-password")
            smtp_server.sendmail("your-email-address@example.com", [to], msg.as_string())
            smtp_server.close()
            print("Text message sent!")
        except Exception as e:
            print("Error: unable to send text message")
            print(e)

if service == "sms":
    return "SMS sent successfully!"

return "MMS sent successfully!"