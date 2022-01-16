"""
    1- first thing we must do is to import the smtp module which is smtplib
    2- then we can create an object from  the smtp class
    3- the assignment requires the name for the smtp server
         Gmail is : smtp.gmail.com
         hotmail :  smtp.live.com
         Yahoo   :  smtp.mail.yahoo.com
    4- connection.starttls() , this line will start the TLS (Transport layer security )  which is  is a cryptographic protocol designed to provide
        communications security over a computer network.
        The protocol is widely used in applications such as email but its use in securing HTTPS remains the most publicly visible.
        this protocol is designed to maximum privacy and Data integrity , so if someone intercept our connection using Wireshark or the Man in the middle
        he will see all the data encrypted
    5- to perfectly send the message your must disable some security features because recently all the email providers such us Gmail , Yahoo
    don't allow this type of connection
    6- Emails without subjects are considered as Spam , there is a way to add the subject
"""

import smtplib

my_email = ""  # create a variable and put your email right here
my_password = ""  # create a variable and put your password in it , don't worry the connection is secure using TLS

#creating the object :
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()  # securing our connections
connection.login(user=my_email , password=my_password) # this login method requires both login and password

# this sendmail method requires both the sender which is your address and the recipient
connection.sendmail(from_addr=my_email , to_addrs="recipient_address" , msg="subject: Email Subject \n\n put the message here")
connection.close() # we must close our connection

'''
there is a second method that we can do which is clean to send email and also you don't need to close it
 because it will be closed after the email been sent

'''
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email , password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="recipient address",
                        msg="subject: Email Subject \n\n this is the email message")
