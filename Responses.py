from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi"):
        return "Hey, how is going"

    if user_message in ("who are you",  "who are you?"):
        return "I'm bot Max"


    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H/%M/%S")

        return str(date_time)

    return "i don't understand you"