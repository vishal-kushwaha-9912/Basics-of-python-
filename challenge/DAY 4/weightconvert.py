 
while True:
    print("Welcome to the Weight Converter 😊")

    user_weight = float(input("Enter your weight : "))
    unit = input("Choose the target unit (kg/lb): ").strip().lower()

    if unit == 'kg':
      convert = user_weight / 2.20462    # lb to Kg
      print (f"your weight in kilograms is  :{convert:.3f}")
    elif unit == 'lb':
      convert = user_weight * 2.20462    # kg to lb   converted = weight * 2.20462
      print(f"your weight in pounds is  : {convert:.3f}") 
    else :
        print(f"{unit} is invalid try again ! ")    

    choice = input("\nDo you want to perform another weight convert ? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you for using the Weight Converter. Goodbye! 👋")
        break        