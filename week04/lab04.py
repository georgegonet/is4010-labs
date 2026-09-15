def find_common_elements(list1, list2):
    """Return a list of values present in both input lists."""
    if not list1 or not list2:
        return []
    set2 = set(list2)
    return [item for item in list1 if item in set2]


def find_user_by_name(users, name):
    """Return the matching user dictionary, or None when no user matches."""
    if not users:
        return None
    for user in users:
        if user.get("name") == name:
            return user
    return None


def get_list_of_even_numbers(numbers):
    """Return the even integers in their original order."""
    if not numbers:
        return []
    return [n for n in numbers if n % 2 == 0]
