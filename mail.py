import smtplib
from_="yourmail"
msg="helloo"
pwd="xyz"
to_="toaddress"
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(from_,pwd)

server.sendmail(from_,to_,msg)
server.quit()
