def city_country(city, country):
    formatted_string = f"{city.title()}, {country.title()}"
    return formatted_string

print(city_country("santiago", "chile"))
print(city_country("new york", "united states"))
print(city_country("tokyo", "japan"))
