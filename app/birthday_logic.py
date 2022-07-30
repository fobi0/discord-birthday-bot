from datetime import date
import csv
import logging

logging.basicConfig(level=logging.INFO)

def check_for_all_known_birthdays():
    current_date = date.today().strftime("%d.%m")

    with open('birthdays.csv') as inp:
        reader = csv.reader(inp)
        birthdays = {rows[0]:rows[1] for rows in reader}

    logging.info(f'Search birthday for todays date: {current_date}')
    birthday_users = []
    for name, birthday in birthdays.items():
        if birthday == current_date:
            birthday_users.append(name)
    logging.info(f'Found {len(birthday_users)} matches. Happy birthday to {str(birthday_users)}')
    return birthday_users

def generate_birthday_message(user):
    logging.debug(f"Generating awesome birthday message for user {user}")
    message = f'Happy Birthday {user}. :tada: :tada: :tada: All the best for your special day! :partying_face: :partying_face:  Great to have you here! :blush: @here Feel free to congratulate now!'
    return message

if __name__ == '__main__':
    users = check_for_all_known_birthdays()

    for user in users:
        logging.info(generate_birthday_message(user))
