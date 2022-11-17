#tried making a code for calculator for revising my youtube studies

first = input("first no.:")
second = input("input second no:")
operator = input("provide operators +,-,*,/")

f = float(first)
s = float(second)
if operator =="+":
    print(f+s)
elif operator== "-":
    print(f-s)
elif operator == "*":
    print(f*s)
elif operator == "/":
    print(f%s)
else:
     print("INVALID INPUT PLEASE TRY AGAIN")
