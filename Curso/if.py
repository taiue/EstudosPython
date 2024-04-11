is_male = False
is_tall = False

if is_male or is_tall:
    print("Tu e macho e grande, ou so macho, ou so grande, acontece...")
else:
    print("Femea baixa")


is_strong = False
is_elderly = True

if is_elderly and is_strong:
    print("Velho e forte")
elif is_strong and not (is_elderly):
    print("Novo e forte")
elif not(is_strong) and is_elderly:
    print("Velho fraco")
else:
    print("Novo e fraco...")