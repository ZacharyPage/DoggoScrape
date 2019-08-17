import smtplib, ssl, requests, bs4, random

# Grabs the Shiba Image from google
website = requests.get('https://www.google.com/search?q=Cute+Shiba&rlz=1C1CHBF_en \
US822US822&soiurce=lnms&tbm=isch&sa=X&ved=0ahUKEwjVgJTBvJvjAhULbs0KHVmABbsQ_AUIECgB&biw=1920&bih=975')

shiba = bs4.BeautifulSoup(website.text, 'lxml')
images = shiba.find_all('img')
randomShiba = random.randint(0, len(images) - 1)
image = images[randomShiba]
image_link = image['src']

# Opens a SMTP connection and sends the picture via email
port = 465
sender_email = 'sender@email.com'
receiver_email = 'recieverl@email.com'
password = 'password'
message = """\
Subject: Hello!

Here are your links good sir:
https://image.shutterstock.com/image-vector/ace-spades-vintage-style-dirty-600w-126884831.jpg
"""

try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login('pagezacharyc@gmail.com', password)
        server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    print('An exception has ocurred')
print("Message Has Been Sent")


