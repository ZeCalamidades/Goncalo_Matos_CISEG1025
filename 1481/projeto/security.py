import re

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
phone_pattern = r"\b(\+?\d{1,3})?[\s\-]?\d{9,}\b"

def detect_personal_data(message):

    if re.search(email_pattern, message):
        return "email"

    if re.search(phone_pattern, message):
        return "telefone"

    return None