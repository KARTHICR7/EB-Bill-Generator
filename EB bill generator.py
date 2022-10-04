def domestic():
    amt=int(5);
    if(units<=100):
        print("Your total bill amount is free")
    elif((units>100) and (units<=200)):
        print("Your total bill amount is",units*amt);
    elif((units>200) and (units<=300)):
        print("Your total bill amount is",units*amt);
    elif((units>300) and (units<=400)):
        print("Your total bill amount is",units*amt);
    elif((units>400) and (units<=500)):
        print("Your total bill amount is",units*amt);
    elif(units>500):
        print("Your total bill amount is",units*amt*amt);
    
def commercial():
    amt=int(10);
    if(units<=100):
        print("Your total bill amount is free")
    elif((units>100) and (units<=200)):
        print("Your total bill amount is",units*amt);
    elif((units>200) and (units<=300)):
        print("Your total bill amount is",units*amt);
    elif((units>300) and (units<=400)):
        print("Your total bill amount is",units*amt);
    elif((units>400) and (units<=500)):
        print("Your total bill amount is",units*amt);
    elif(units>500):
        print("Your total bill amount is",units*amt*amt);
    
print("....ELECTRICITY BILL GENERATOR....");
print("----------------------------------")
bn=int(input("Enter bill No.:"))
name=input("Enter Name:")
units=int(input("Enter the unit:"));
print("1.Domestic , 2.Commercial");
billType=int(input("Enter the electricity bill type(1or2):"));
if billType==1:
    print("Bill no.:",bn);
    print("Name:",name);
    print("Your electricity bill is Domestic");
    domestic()
else:
    print(bn);
    print(name);
    print("Your electricity bill is Commercial");
    commercial()


