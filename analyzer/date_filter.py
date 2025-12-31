
def is_within_date_range(timestamp, start_date, end_date):
    if start_date and timestamp < start_date:
        return False
    if end_date and timestamp > end_date:
        return False
    return True
