sandwich_orders = ['bacon', 'baked bean', 'bagel toast', 'bauru', 'falafel']
finished_sandwichs = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Your sandwich: {current_sandwich.title()}")
    finished_sandwichs.append(current_sandwich)

print("\nI made your:")
for finished_sandwich in finished_sandwichs:
    print(f"{finished_sandwich.title()} sandwich.")