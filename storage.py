import datetime

def save_user_data(income, expenses, savings):
    with open("user_data.csv", "a") as f:
        line = f"{datetime.date.today()},{income},{expenses['Fixed']},{expenses['Food']},{expenses['Travel']},{expenses['Other']},{savings}\n"
        f.write(line)
