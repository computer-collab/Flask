import random, smtplib


def GenerateOTP(email,Name=None):
    if not Name:
        Name = "**Name not defined**\n"
    receiver_email = email
    otp = random.randint(100000,999999)
    sender_email = "otpmail.noreply@gmail.com"
    app_password = "dxrrnmilxweeznoz"
    subject = "Your OTP for registration"
    message = f"""
    Hey Ms./Mr.{Name},
    This is your otp : {otp} for registration.
    Thankyou for registering.
    From : Mail Bot Service, login.
    """
    text = f"Subject : {subject}\n\n{message}"
    try :
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender_email,app_password)
        server.sendmail(sender_email,receiver_email,text )
        server.quit()
        print("Email has been successfully sent.\n")
        return otp
    
    except Exception as e :
        print(f"\n\033[31mError:\033[0m {e}\n")
        return "Error_exception"
    


