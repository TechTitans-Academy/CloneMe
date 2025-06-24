output = input("Are You RedHat Certified Engineer? (yes/no): ").strip().lower()

if output == "yes":
    print("Congratulations, You are one step ahead.")
elif output == "no":
    output2 = input("Would you like to register for RHCSA? (yes/no): ").strip().lower()
    if output2 == "yes":
        print("Please contact Tech Titans!!")
    elif output2 == "no":
        print("No problem. Keep learning!")
    else:
        print("Please enter yes/no only! Thank you.")
else:
    print("Please enter yes/no only! Thank you.")
