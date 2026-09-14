phone_book = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077",
}

number = input("please check for a number: ")

if len(number) != 10 or not number.isdigit():
    print("Sorry, the number is invalid")

 
else:
 for name in phone_book:
    if phone_book[name] == number:
     print(name)
     break
 else:
    print("Sorry, the number is not found")
    

 
    