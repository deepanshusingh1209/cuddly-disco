weight=int(input("tell me your weight :--"))
unit=str(input("K for KG and L for LBS :--"))
K = "K"
if unit is K :
    weight_in_LBS=weight*2.20462262
    print("Your weight in LBS    is", weight_in_LBS)
else:
    weight_in_KG=weight/2.20462262
    print("Your weight in KG is", weight_in_KG)