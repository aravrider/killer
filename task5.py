import smtplib
import pywhatkit
from pytube import YouTube
from twilio.rest import Client

def send_email():
    my_mail = "aravrider@gmail.com"  # Replace with your email
    passcode = "hibjljyoybtatmuz"     # Replace with your app password or Gmail password

    # Set up the SMTP server
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_mail, password=passcode)

    mail_content = "Subject: Trip on This Weekend:\n\nHey, aao kbhi haweli pe"

    try:
        connection.sendmail(from_addr=my_mail, to_addrs="amanmahto669@gmail.com", msg=mail_content)
        print("Email sent successfully.")
    except Exception as e:
        print("Something went wrong while sending email:", e)
    finally:
        connection.close()

def send_sms():
    # Your Twilio Account SID and Auth Token
    account_sid = 'AC02f1ee4617c79b392003d119597755ad'  # Replace with your Twilio Account SID
    auth_token = '69aa4ee8e7a8e66ca855637c5bb2397a'      # Replace with your Twilio Auth Token

    # Create a Twilio client
    client = Client(account_sid, auth_token)

    # Send a message
    try:
        message = client.messages.create(
            to='+919709366634',           # Destination phone number
            from_='+15203895446',        # Your Twilio phone number
            body='Hello, this is a test message!'
        )
        print("SMS sent successfully:", message.sid)
    except Exception as e:
        print("Something went wrong while sending SMS:", e)

def send_whatsapp_message():
    try:
        pywhatkit.sendwhatmsg("+918235068566", "Geeks For Geeks!")  # Set time (hour, minutes)
        print("WhatsApp message scheduled successfully.")
    except Exception as e:
        print("Something went wrong while sending WhatsApp message:", e)

def download_video(video_url, output_path):
    try:
        # Create YouTube object
        yt = YouTube(video_url)
        
        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()
        
        if stream:
            print("Downloading video:", yt.title)
            stream.download(output_path)
            print("Video downloaded successfully to:", output_path)
        else:
            print("Error: No stream available for the given video URL.")
    except Exception as e:
        print("Error occurred while downloading video:", str(e))

if __name__ == "__main__":
    # Example usage for sending email, SMS, WhatsApp message, and downloading a video
    send_email()
    send_sms()
    send_whatsapp_message()

    # Download a video
    video_url = "https://youtube.com/shorts/EyD6UWIr6ko?si=oofXptnpqcXsXN7H"  # Replace with your video URL
    output_path = "/video"  # Replace with your desired output path
    download_video(video_url, output_path)
