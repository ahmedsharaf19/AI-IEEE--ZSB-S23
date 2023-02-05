dict1 = {
    "A":[20,30,100,49],
    "B":[00,199,201,29],
    "C":[40,90,69,18]
}
maxRange = -10e20
key = None
for main_key in dict1:
    rang = max(dict1[main_key]) - min(dict1[main_key])
    if rang > maxRange :
            maxRange = rang
            key = main_key

print(key)
