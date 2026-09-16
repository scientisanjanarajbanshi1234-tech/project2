
from datetime import date, datetime

# Name input
name = input("Enter your name: ")

# Date of birth input
dob_input = input("Enter your date of birth (DD-MM-YYYY): ")

# Convert date of birth into date
dob = datetime.strptime(dob_input, "%d-%m-%Y").date()

# Today's date
today = date.today()

# Calculate age
age = today.year - dob.year

# Check if birthday has occurred this year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

# Display result
print("\n===== Personal Information =====")
print("Name:", name)
print("Date of Birth:", dob.strftime("%d-%m-%Y"))
print("Age:", age, "years")