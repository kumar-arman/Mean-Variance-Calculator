from mean_var_std import calculate

# Valid input test
print("Valid Input Test:")
print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

# Invalid input test
print("\nInvalid Input Test:")
try:
    calculate([1, 2, 3])
except ValueError as e:
    print(e)
