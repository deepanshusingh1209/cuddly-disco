weight=int(input("tell me your weight!!"))
unit=int(input("that was in LBS OR KG--1 for the LBS and 2 for the KG :--"))
if unit == 2:
    weight_in_LBS=weight*2.20462262
    print("Your weight in LBS    is", weight_in_LBS)
else:
    weight_in_KG=weight/2.20462262
    print("Your weight in KG is", weight_in_KG)

