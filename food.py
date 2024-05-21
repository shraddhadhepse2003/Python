
type=input("which type of food are you looking for:")

if type=='veg':
    print("Paneer Tikka")
    print("Matar Paneer")
    print("Paneer Masala")

    food=input("which dish would you like:")
    if 'paneer Tikka' == food:
        print("\n Paneer Tikka \n price:300 \n butter roti:4")
    elif 'matar Paneer' == food:
        print("\n Matar Paneer \n price:200 \n butter roti:3")
    elif 'paneer masala' == food:
        print("\n paneer masala \n price:250 \n butter roti:3")

elif type=='nonveg':
    print("chicken Tikka")
    print("chicken 65")
    print("chicken biryani")

    food1=input("which dish would you like:")
    if 'chicken Tikka' == food1:
        print("\n chicken Tikka \n price:400 \n butter roti:4")
    elif 'chicken 65' == food1:
        print("\n chicken 65 \n price:350 \n butter roti:3")
    elif 'chicken biryani' == food1:
        print("\n chicken biryani \n price:350 \n butter roti:0")


    
