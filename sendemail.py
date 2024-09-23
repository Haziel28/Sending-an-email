import smtplib # This imports the module (send mail transport protocol library)


try: # we put this in a try block as its risky
    email = input("Your email") # terminal window asks you sender email then stores it in a variable called email
    receiver_email = input("Sending to: ") # same as up top but it's who your sending it to

    subject = input("SUBJECT: ") # same as up top just trying to be a little more organized
    message = input("MESSAGE: ")

    text = f"Subject: {subject}\n\n{message}" # we use an f string to send our subject and message down below with the new lines

    server = smtplib.SMTP("smtp.gmail.com", 587) # here we create a server object with 2 arguments the host and the default maill submission port
    server.starttls() # here we start our server with transport layer security

    server.login(email, "nsxjzfypctomvjqd") # here to use the login module we use our email variable and app password

    server.sendmail(email, receiver_email, text) # Now we use the sendmail module to send it with our 3 arguments

    print("email has been sent to " + receiver_email) # once all is done it will say email has been sent to "Whoever you send it to"

except smtplib.SMTPAuthenticationError: # This block of code is used to not show an error and instead print Unable to sign in
    print("Unable to sign in")





