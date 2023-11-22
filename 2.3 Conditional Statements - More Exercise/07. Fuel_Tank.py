fuel_type = input()
liters_fuel = float(input())

if liters_fuel >= 25:
    if fuel_type == 'Diesel':
        fuel_type = fuel_type.lower()
        print(f'You have enough {fuel_type}.')
    elif fuel_type == 'Gasoline':
        fuel_type = fuel_type.lower()
        print(f'You have enough {fuel_type}.')
    elif fuel_type == 'Gas':
        fuel_type = fuel_type.lower()
        print(f'You have enough {fuel_type}.')
    else:
        print('Invalid fuel!')

else:
    if fuel_type == 'Diesel':
        fuel_type = fuel_type.lower()
        print(f'Fill your tank with {fuel_type}!')
    elif fuel_type == 'Gasoline':
        fuel_type = fuel_type.lower()
        print(f'Fill your tank with {fuel_type}!')
    elif fuel_type == 'Gas':
        fuel_type = fuel_type.lower()
        print(f'Fill your tank with {fuel_type}!')
    else:
        print('Invalid fuel!')
