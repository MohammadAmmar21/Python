##strings_n_numbers2
#h2e4r1
#hheeeer

string = input()

expanded = ''

for i in string:
    if i.isdigit():
        expanded += expanded[-1] * (int(character) - 1)
    else:
        expanded += character

print(expanded)
