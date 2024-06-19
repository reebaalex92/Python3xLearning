def make_pizza(*toppings):
    for topin in toppings:
        print(topin, end="\n")


make_pizza("tomato")
make_pizza("tomato", "mushroom")
make_pizza("tomato", "olives", "sweetcorn", "mushroom")

# acts as tuples
# list and tuples are same but tuples are immutable.Its value can't be changed.
