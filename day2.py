def max(num1,num2):
    if(num1>num2):
        result=num1
    else:
        result=num2
    return result
def main():
    i=5
    j=10
    k=max(i,j)
    print("The larger number betwwem {} and {} is {}".format(i,j,k))   
    main()         