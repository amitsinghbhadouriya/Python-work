favorite_languages = {
    'jen': 'pyton',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'pyton',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")





favorite_languages = {
    'jen': 'pyton',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'pyton',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")






favorite_languages = {
    'jen': 'pyton',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'pyton',
}

for name in favorite_languages.keys():
    print(name.title())






favorite_languages = {
    'jen': 'pyton',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'pyton',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")






favorite_languages = {
    'jen': 'pyton',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'pyton',
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")






favorite_languages = {
    'jen': 'pyton',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'pyton',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")






favorite_languages = {
    'jen': 'pyton',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'pyton',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())





favorite_languages = {
    'jen': 'pyton',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'pyton',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())





favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languagesa are:")
    for language in languages:
        print(f"\t{language.title()}")