import random, smtplib

def GenerateOTP(email):
    receiver_email = email
    otp = random.randint(100000,999999)
    sender_email = "otpmail.noreply@gmail.com"
    app_password = "dxrrnmilxweeznoz"
    subject = "Your OTP for registration"
    message = f"""
    Hey,
    This is your otp : {otp} for registration.
    Thankyou for registering.
    From : Mail Bot Service, login.
    """
    text = f"Subject : {subject}\n\n{message}"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,app_password)
    server.sendmail(sender_email,receiver_email,text )
    server.quit()
    print("\nEmail has been successfully sent.")
    return otp