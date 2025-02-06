def valida_email(email: str) -> bool:
    email = email.lower()
    if email.find('@') >= 0 and email.endswith('.com'):
        return True
    return False

print(valida_email('gui.com'))

print(valida_email('gui@'))

print(valida_email('gui@.com'))
