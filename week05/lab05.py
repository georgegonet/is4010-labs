def calculate_average_age(users):

    """Return the average numeric age from a list of users.
    Ignores missing ages and ages that are not numeric.
    Returns 0.0 when no valid ages exist."""

    valid_ages = []

    for user in users:
        age = user.get("age")

        if isinstance(age, (int, float)):
            valid_ages.append(age)

    if not valid_ages:
        return 0.0

    return sum(valid_ages) / len(valid_ages)

def get_active_user_emails(users):

    """
    Return email addresses belonging to active users.
    Includes an email only when is_active is truthy and the email key exists.
    """
    emails = []

    for user in users:
        if user.get("is_active") and "email" in user:
            emails.append(user["email"])

    return emails
