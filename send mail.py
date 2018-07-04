# your Gmail account 
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("singh.santosh2702@gmail.com", "password")

# message to be sent
message = "Clash"

# sending the mail
s.sendmail("singh.santosh2702@gmail.com", "shwetanksp@gmail.com", message)

# terminating the session
s.quit()




