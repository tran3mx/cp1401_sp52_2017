def main():
    print("Calculate the Bonus: ")
    sales = float(input("Enter sales: $"))
    while sales >=0:
            if sales < 1000:
                bonus = sales * 0.1
                print("Bonus: $", bonus)
                sales = float(input("Enter sale: $"))
            elif sales >= 1000:
                bonus = sales * 0.15
                print("Bonus : $", bonus)
                sales = float(input("Enter sale: $"))
            else:
                pass
main()