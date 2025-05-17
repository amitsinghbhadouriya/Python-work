from city_function import get_formatted_name

def city_country_name():
    """Do name like 'Santiago, Chile'."""
    formatted_name = get_formatted_name('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'
