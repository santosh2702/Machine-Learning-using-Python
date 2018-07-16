# your Gmail account 
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("singh.santosh2702@gmail.com", "poiu@12345")

# message to be sent
message = "hello what the hell"

# sending the mail
s.sendmail("singh.santosh2702@gmail.com", "nitishchauhan9900@gmail.com", message)

# terminating the session
s.quit()




