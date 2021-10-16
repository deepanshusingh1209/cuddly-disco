number_of_items=int(input("Tell me how much product you purchased :--"))
cost= 100
if number_of_items>1000:
    original_cost=number_of_items*cost
    new_cost= original_cost-(original_cost*10/100)
    print("Total cost for your ",number_of_items,"products is", new_cost)
else :
    original_cost=number_of_items*cost
    print("Total cost for your ",number_of_items,"products is",original_cost)
