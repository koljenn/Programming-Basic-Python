price_mackerel_kg = float(input())
price_sprat_kg = float(input())
kg_bonito = float(input())
kg_safrid = float(input())
kg_mussels = int(input())

price_bonito_kg = price_mackerel_kg + price_mackerel_kg * 0.60
total_sum_bonito = kg_bonito * price_bonito_kg
price_safrid_kg = price_sprat_kg + price_sprat_kg * 0.80
total_sum_safrid = kg_safrid * price_safrid_kg
total_sum_mussels = kg_mussels * 7.50

total_bill = total_sum_bonito + total_sum_safrid + total_sum_mussels

print(f"{total_bill:.2f}")





