principal =int(input("How much money?: "))
Time_years=int(input("how long has the money been deposited?: "))
rate=int(input("intrest rate?: "))
Amount=principal*(1+rate/100)**Time_years
print("Amount Of money in your account is {}".format(Amount))1