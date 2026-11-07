passanger_name = input ("what is your name ? :").title()
passanger_age = int(input("what is your age ? :"))
ticket = input("Do you have a ticket ? :").strip().upper()
ticket_cost = int(input(" input your Total ticket cost :"))
registered_passengers_total = 0

if passanger_age >=18 and ticket.upper() == "YES":
    print(f"Welcome {passanger_name}!")
    registered_passengers_total += 1

elif passanger_age <18:
    print (f"{passanger_name}, please visit customer care ")

elif ticket == "NO":
    print (f"{passanger_name}, please visit customer care ")


registered_passengers_total += 10 
passanger_remaining = 15 % 3

print (f"registered_passanger : {registered_passengers_total}")
print (f"total ticket amount : {ticket_cost}")
