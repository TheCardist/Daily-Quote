import os
import smtplib
from email.message import EmailMessage
from file_locator import FileLocator
import keyring
from datetime import date

os.chdir('/home/chris/Desktop/DailyQuotes')


def get_contacts() -> list[str]:
    addresses = []

    with open(r'/home/chris/Desktop/DailyQuotes/contacts.txt', 'r') as contacts:
        addresses = [contact.strip() for contact in contacts]

    contacts = [line.split(', ')[0] for line in addresses]
    emails = [line.split(', ')[1] for line in addresses]

    return contacts, emails


def send(contacts: list, emails: list, note: str, quote: dict):
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
                    <p>Hi {contact}, Here is your quote and note of the day.</p></br>
                    <p>Quote by: <b>{quote['author']}</b></p>
                    <p><i>{quote['quote']}</i></p>
                    <br>
                    <p>{note}</p>
                </body>
            </html>
            """, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(keyring.get_password('gmail', 'email'),
                       keyring.get_password('gmail', 'password'))
            smtp.send_message(msg)


if __name__ == '__main__':
    today = date.today()
    locator = FileLocator()
    note = locator.get_content(path='200 - Citadel', quote=False)
    quote = locator.get_content(
        path='400 - Archive/300 - Literature Notes', quote=True)
    contacts, emails = get_contacts()
    send(contacts, emails, note, quote)
    with open('log_file.txt', 'w+') as f:
        for line in note.splitlines():
            f.write(f'Sent on {today} - {line}')
            break
