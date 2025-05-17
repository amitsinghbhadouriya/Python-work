poll_results = {}

def take_poll():
    while True:
        name = input("Enter your name (or 'quit' to exit): ")
        if name.lower() == 'quit':
            break
        destination = input("If you could visit one place in the world, where would you go? ")
        
        if destination in poll_results:
            poll_results[destination] += 1
        else:
            poll_results[destination] = 1

take_poll()

print("\nPoll Results:")
for destination, count in poll_results.items():
    print(f"{destination}: {count} vote(s)")
