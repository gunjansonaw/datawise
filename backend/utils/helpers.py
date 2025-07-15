from datetime import datetime

def format_datetime(dt):
    """
    Formats a datetime object into a string.

    Args:
        dt (datetime): The datetime object to format.

    Returns:
        str: The formatted datetime string.
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def validate_tags(tags):
    """
    Validates a list of tags to ensure they meet certain criteria.

    Args:
        tags (list): The list of tags to validate.

    Returns:
        bool: True if the tags are valid, False otherwise.
    """
    if not isinstance(tags, list):
        return False
    return all(isinstance(tag, str) for tag in tags)

# Add more helper functions as needed
