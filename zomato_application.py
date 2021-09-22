# In this code first of all u have to fill enter a user name''''''
def dish(dishes,dict1):
    if dishes in dict1:
        if dishes=="momos":
            print("\n1.parallax \n2 momos \n==>these are available--->")
        elif dishes=="finger chips" or dishes=="idly dosa":
            print("\n1.Dine Dime  \n2 finger chips \n3 idly dosa \n ==> these all  available in  this restuarant.")
        elif dishes=='gulab jamun' or dishes=="omlet":
            print("\n1 mirchi house in this\n2 gulab jamunn 3\ omlet is available")
        elif dishes=="coldrink" or dishes=="salad":
            print("\n1 coldrink \n2 salad mirchi house mirchi house  restorant  is available-")
        elif dishes=="aalu pratha" or dishes=="ice cream" or dishes=="orange juice":
            print("\n1 taaj restuarunat \n2 aalu paratha \3 ice craem is available")
        
        print(dishes +' added to cart')
        return dishes
	
def cat(b):
    if b=="Healthy food":
        print("1 (🍩)omlet\n2 salad\n3 orange juice-")
    elif b=="Sweet food":
        print("1 (🍦)ice cream\n2  gulab jamun\n3  coldrink ")
    elif b=="Fast food":
        print("1.(🍲)momos\n2 finger chips\n3 idly dosa\n4 🥘aalu paratha🥘")
        print()

def order(dict1):
	b=input("enter whish catagery u want\n1 Healthy food\n2 Sweet food\n3 Fast food---")
	cat(b)
	a=input("enter whish dish u want ---")
	x=dish(a,dict1)
	return x

def order2(dict1):
    # Here u have to choise what u want restaruant ya dish
    # if you choise restaruant so what ever we have restaraunt and in this restaruant what what things 
    # is aviable so print ''''''''''
	b=input("enter restorent--")

	restorants(b)
	a=input("enter which dish u want ---")
    # here if you choise dish.....
    # so all dishes it will print 
    # what ever dish you want you can choise .........
	x=dish(a,dict1)
	return x


def restorants(res):
	if res=="parallax":
        # Here i  put all restaruant means which which restraunt what what things is 
        # aviable ..........
		print("1.(🍩)omlet\n2 salad\n3 orange juice")
	elif res=="dine dime":
		print("1.(🍲)momos\n2 finger chips\n3 idly dosa\n4 🥘aalu paratha🥘")
	elif res=="mirchi house":
		print("1.(🍲)momos \n2 gulab jamun\n3 coldrink")
	elif res=="taaj":
		print("1.(🍦)ice cream\n2 gulab jamun \n3 idly dosa\n4 🥘aalu paratha🥘")



print("(🛵)welcome ZOMATO (🛵)")
name=input("enter your name(🥰)-")
password=input("enter password--")
# Here you have to enter password ....

password1=input("enter same password--")

if password==password1:
    # if password your same then your login is succesfully ''''''
    print("you login successfully")
    location=input("enter your location--")
    # Here you have to enter location ''''

    location1=input("enter same location--")
    print()
    if location==location1:
        # if location your same then your location is creect.....
        print()
        print("we will deliver on this "+location+" location")

        search=input("(😍)what you want restruant or dish(😍)--")
        print()
        dict1={'omlet':20, 'salad':30, 'orange juice':20, 'ice cream':50, 'gulab jamun':100, 'coldrink':40, 'momos':60, 'finger chips':60, 'idly dosa':60, 'aalu paratha':40}
        l2=[]
        if search=="dish":
            t=True
            while t:
                c=order(dict1)
                
                l2.append(c)
                d=input('(👍)want to add another dish \n1 yes\n2  no(👍)')
                if d=='no':
                    break
        elif search=="restruant":
            t=True
            while t:

                print("\n1 parallax \n2 dine dime\ n3 taaj \n4 mirchi house ")
                c=order2(dict1)
                l2.append(c)
                d=input('(👍)want to add another dish \n1 yes\n2  no(👍)')
                if d=='no':
                    break
        print('Your cart')
        for i in l2:
            print(i)

        usercard1=input(" Do you want to place order\n1 .yes\n2.no-->")
        if usercard1=="yes":
            count=0
            for i in l2:
                if i in dict1:
                    count+=dict1[i]

            payment=input("enter a payment \n1.online \n2.cash on deliver-----")
            if payment=="online":
                pay1=input("there is two method of online paymen \n1. phone pay \n2. google pay enter this--")
                if pay1=="phone pay" or pay1=="google pay":
                    # Here you have to choise google pay and phone pay;;;;;
                    no=input("enter your 10 digit no.")

                    if len(no)==10:
                        print("your order is successfully and total amount is-"+str(count))
                        # Here you have to enter  atleast 10 digit number;;;;;;1,,google pay 2,phone pay...
                    else:
                        print("check your no.")

            elif payment=="cash on deliver" or payment=="2":
                
                print("your order is successfully and total amount is-"+str(count))

            import random
            m=[20,25,23,22,21,26,30,28]
            m=random.choice(m)
            # Here i total timeing means how much time it will take dilvire......
            print('your order is placed it will be delivered in '+str(m)+'min(⏰')