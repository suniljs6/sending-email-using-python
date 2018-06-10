smtplib Overview:-
--
  The smtplib module defines an SMTP client session object that can be used to send
  mail to any Internet machine with an SMTP or ESMTP listener daemon. 

  SMTP stands for Simple Mail Transfer Protocol. 

  The smtplib modules is useful for communicating with mail servers to send mail.

  Sending mail is done with Python's smtplib using an SMTP server. 

  Actual usage varies depending on complexity of the email and settings of the
  email server, the instructions here are based on sending email through Gmail.


Working:-
--
  Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.

  Here is a simple syntax to create one SMTP object, which can later be used to send an e-mail −

  import smtplib

  smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )

  Here is the detail of the parameters −

      host − This is the host running your SMTP server. You can specify IP address of the host or a domain name like tutorialspoint.com. This is optional argument.

      port − If you are providing host argument, then you need to specify a port, where SMTP server is listening. Usually this port would be 25.

      local_hostname − If your SMTP server is running on your local machine, then you can specify just localhost as of this option.

  An SMTP object has an instance method called sendmail, which is typically used to do the work of mailing a message. It takes three parameters −

      The sender − A string with the address of the sender.

      The receivers − A list of strings, one for each recipient.

      The message − A message as a string formatted as specified in the various RFCs.
