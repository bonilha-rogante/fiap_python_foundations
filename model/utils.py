def valida_email(email: str) -> str:
    email = email.lower()
    if email.find('@') >= 0 and email.endswith('.com'):
        return True
    return False