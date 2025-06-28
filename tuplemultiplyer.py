tup1=(4,3,2,2,-1,18)
tup2=(2,4,8,8,3,2,9)
def product_of_tuple(numbers):
    product=1
    for num in numbers:
        product*=num
    return product
result1= product_of_tuple(tup1)
result2=product_of_tuple(tup2)
print("Product of tup1",result1)
print("Product of tup2",result2)