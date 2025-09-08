dec = [165, 248, 94, 346, 299, 73, 198, 221, 313, 137, 205, 87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138]

decoded_string = ""
for d in dec:
    d_mod = d % 37
    if d_mod in range(0, 26):
        decoded_string += chr(d_mod + ord('A'))
    elif d_mod in range(26, 36):
        decoded_string += str(d_mod - 26)
    else:
        decoded_string += "_"

print(f"picoCTF{{{decoded_string}}}")
