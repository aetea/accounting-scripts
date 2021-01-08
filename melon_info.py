"""Print out all the melons in our inventory."""

from melons import melons

# print the nested dictionary, but with 
# each key-value pair (item) on a separate line

for melon_name, melon_info in melons.items(): 
    
    print(melon_name.upper())
    for key, value in melon_info.items():
        print(f"    {key}: {value}")
    print()




### ---------------- OLD CODE --------------- ###
# from melons import melon_names, melon_seedlessness, melon_prices


# def print_melon(name, seedless, price):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
