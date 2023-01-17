month_mappings = [ "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC" ]

def get_month(month_index):
    return month_mappings[month_index]

def get_month_index(month):
    return month_mappings.index(month)
