age = int(input("enter the age of the person->"))
gender = input("enter the gender->")

if gender=="m":
    if age>21:
        print("the person is male and can marry")
    else:
        print("Kiddo U need more years")
else:
    if age>18:
        print("the person is female and can marry")
    else:
        print("the person cannot marry ")