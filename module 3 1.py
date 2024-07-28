calls = 0
def caunt_calls():
    global calls
    calls += 1
def string_info(string):
    caunt_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    caunt_calls()
    if string.upper() in [s.upper() for s in list_to_search]:
        return ('True')
    else:
        return ('False')
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)