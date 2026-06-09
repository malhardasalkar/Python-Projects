print("===== ELECTRICAL CALCULATOR =====")

while True:
    print("\n1. Calculate Power (P = V x I)")
    print("2. Calculate Current (I = V / R)")
    print("3. Calculate Voltage (V = I x R)")
    print("4. Calculate Resistance (R = V / I)")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        V = float(input("Enter Voltage (V): "))
        I = float(input("Enter Current (A): "))
        P = V * I
        print("Power =", P, "Watts")

    elif choice == "2":
        V = float(input("Enter Voltage (V): "))
        R = float(input("Enter Resistance (Ohms): "))
        I = V / R
        print("Current =", I, "Amperes")

    elif choice == "3":
        I = float(input("Enter Current (A): "))
        R = float(input("Enter Resistance (Ohms): "))
        V = I * R
        print("Voltage =", V, "Volts")

    elif choice == "4":
        V = float(input("Enter Voltage (V): "))
        I = float(input("Enter Current (A): "))
        R = V / I
        print("Resistance =", R, "Ohms")

    elif choice == "5":
        print("Thank you for using Electrical Calculator!")
        break

    else:
        print("Invalid Choice! Please try again.")