import pyotp


def generate_user_backup_codes():
    backup_set = [str(pyotp.random_base32())[:8] for i in range(10)]
    return backup_set

