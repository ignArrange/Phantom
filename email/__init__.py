import random
import names


def gen(y):
    return ''.join(random.choice(str(random.randint(0, 9))) for x in range(y))


def generateEmail(amt, domain=None):
    domains = ["gmail", "yahoo", "mail", "hotmail", "live", "protonmail"]
    emails = []
    for x in range(amt):
        if domain is None:
            email = names.get_full_name().replace(' ', '') + str(gen(random.randint(3, 6))) + "@" + random.choice(
                domains) + ".com"
            emails.append(email)
        else:
            email = names.get_full_name().replace(' ', '') + str(gen(random.randint(3, 6))) + "@" + domain
            emails.append(email)

    return emails
