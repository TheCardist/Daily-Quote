import random
import smtplib
from email.message import EmailMessage
from quote_list import get_quotes
from notes import read_note
import markdown


def get_contacts():
  """Parse contact list to retrieve the name and email address of each person that wants an email"""
    addresses = []

    with open('contacts.txt', 'r') as contacts:
        addresses = [contact.strip() for contact in contacts]

    contacts = [line.split(', ')[0] for line in addresses]
    emails = [line.split(', ')[1] for line in addresses]

    return contacts, emails


def send(contacts: list, emails: list):
  """Sending of the email to each user gathered from the contact list"""
    for c, e in zip(contacts, emails):
        contact = c.strip()
        email = e.strip()

        msg = EmailMessage()
        msg['Subject'] = "Random Quote and Note"
        msg['From'] = 'dailyquotegenerator@gmail.com'
        msg['To'] = email
        msg.set_content("Plain Text")
        msg.add_alternative(f"""\
            <!DOCTYPE html>
            <html>
                <body>
                    <p>Hi {contact}, Here is your quote and note of the day.</p>
                    <p>Quote by: <b>{quote['author']}</b></p>
                    <p><i>{quote['quote']}</i></p>
                    <br>
                    <p>{markdown_note}</p>
                </body>
            </html>
            """, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('email', 'password')
            smtp.send_message(msg)


if __name__ == '__main__':
    quote = random.choice(get_quotes())
    note = read_note()
    markdown_note = markdown.markdown(note)
    contacts, emails = get_contacts()
    send(contacts, emails)
