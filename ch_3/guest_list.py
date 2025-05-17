guest = ['aman', 'jeet', 'abhishek', 'anmol']
print(f"I am inviting you for a dinner party {guest[0].title()}")
print(f"I am inviting you for a dinner party {guest[1].title()}")
print(f"I am inviting you for a dinner party {guest[2].title()}")
print(f"I am inviting you for a dinner party {guest[3].title()}")


# insert
guest = ['aman', 'jeet', 'abhishek', 'anmol']
guest.insert(0, 'narendra')
print(guest)

guest.insert(3, 'naitik')
print(guest)


# append
guest.append('dev')
print(guest)

print(f"I am inviting you for a dinner party {guest[0].title()}")
print(f"I am inviting you for a dinner party {guest[1].title()}")
print(f"I am inviting you for a dinner party {guest[2].title()}")
print(f"I am inviting you for a dinner party {guest[3].title()}")
print(f"I am inviting you for a dinner party {guest[4].title()}")
print(f"I am inviting you for a dinner party {guest[5].title()}")
print(f"I am inviting you for a dinner party {guest[6].title()}")



message = '''sorry for the inconvience but now I am able to invite only two people 
beacause the table does not arive at the correct time '''
print(message)


# pop
guest = ['narendra', 'aman', 'jeet', 'naitik', 'abhishek', 'anmol', 'dev']
popped_guest  = guest.pop()
print(popped_guest)


# remove
guest = ['dev', 'aman']
guest.remove('dev')
guest.remove('aman')
print(guest)