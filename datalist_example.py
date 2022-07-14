product=["television","fridge","oven","notebook"]
print(product)
#how many product
print(len(product))
# what are the first two name of the products
print(product[0:2])
#what are first and last name of products
print(product[0],product[-1])
#or
print(product[0],product[len(product)-1])
#rename the second product
product[1]="washing machine"
print(product)
#add to products
product=product+["air conditioning"]
print(product)
#reverse listing
print(product[::-1])
