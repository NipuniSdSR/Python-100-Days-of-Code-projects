##################### Extra Hard Starting Project ######################

# Todo: 1. Update the birthdays.csv

# Todo: 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
month = now.month
day = now.day

# Reading letters---------------------------#
import os

letters = []
path = "./letter_templates/"
os.chdir(path)
# listdir :Return a list containing the names of the files in the directory.
for file in os.listdir():
    with open(file) as letter:
        letters.append(letter.read())

# Changing directory to original path---------#
path = "../"
os.chdir(path)

# Reading CSV file ----------------------------#
import pandas

dataframe = pandas.read_csv("birthdays.csv")
print(dataframe)

# getting rows related to both month and day -----#
dataframe = dataframe.loc[(dataframe["month"] == month) & (dataframe["day"] == day)]

# If today has a birthday send an email------------#
if not dataframe.empty:
    print(dataframe)

    # Todo: 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
    #  actual name from birthdays.csv
    names = dataframe.name.values
    letter = random.choice(letters)

    for index in range(len(names)):
        letter = letter.replace("[NAME]", names[index])

        # Todo: 4. Send the letter generated in step 3 to that person's email address.
        my_email = "beecharm.g@gmail.com"
        password_g = "frgvefrsveqvcmsf"
        receiver_mail = dataframe.email.values[index]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password_g)
            connection.sendmail(from_addr=my_email,
                                to_addrs=receiver_mail,
                                msg=f"Subject: Happy Birthday!\n\n"
                                    f"{letter}")

else:
    print("No birthday today")
