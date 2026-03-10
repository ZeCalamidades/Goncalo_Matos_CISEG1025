import re

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
phone_pattern = r"\b(\+?\d{1,3})?[\s\-]?\d{9,}\b"
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
birthday_pattern = r"\b\d{2}[/-]\d{2}[/-]\d{4}\b"
credit_pattern = r"\b(?:\d[ -]*?){13,16}\b"
name_pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

def detect_personal_data(message):

    if re.search(email_pattern, message):
        return ("block","Email")

    if re.search(phone_pattern, message):
        return ("block","Telefone")
    
    if re.search(ip_pattern, message):
        return ("block","Endereço IP")

    if re.search(birthday_pattern, message):
        return ("block","Data de Nascimento")
    
    if re.search(credit_pattern, message):
        return ("block","Cartão de Crédito")
    
    if re.search(name_pattern, message):
        return ("warn","Nome Completo")
    
    
    return None

