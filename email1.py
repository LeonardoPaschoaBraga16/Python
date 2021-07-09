import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("leopasbraga@gmail.com", "Black Knight")
server.sendmail(
  "leopasbraga@gmail.com",
  "leopasbraga@gmail.com",
  "Macaco Roxo")
server.quit()
