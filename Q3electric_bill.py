def calculate_electricity_bill(units):
    total_bill = 0
    
    # For the first 100 units
    if units <= 100:
        total_bill = units * 4.5
    else:
        total_bill += 100 * 4.5
        units -= 100
        
        # For the next 100 units
        if units <= 100:
            total_bill += units * 6
        else:
            total_bill += 100 * 6
            units -= 100
            
            # For the next 100 units
            if units <= 100:
                total_bill += units * 10
            else:
                total_bill += 100 * 10
                units -= 100
                
                # For units above 300
                total_bill += units * 20
    
    return total_bill

# Example usage
units_consumed = int(input("Enter the number of units consumed: "))
bill_amount = calculate_electricity_bill(units_consumed)
print("Electricity bill: Rs.", bill_amount)

