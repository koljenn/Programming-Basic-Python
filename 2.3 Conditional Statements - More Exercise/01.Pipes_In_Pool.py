volume_of_the_pool = int(input())
p1 = int(input())
p2 = int(input())
hours_worker_missing = float(input())

debit_of_p1 = p1 * hours_worker_missing
debit_of_p2 = p2 * hours_worker_missing
field = debit_of_p1 + debit_of_p2

if field <= volume_of_the_pool:
    p1_field = debit_of_p1 / field * 100
    p2_field = debit_of_p2 / field * 100
    pool_field = field / volume_of_the_pool * 100
    print(f"The pool is {pool_field:.2f}% full. Pipe 1: {p1_field:.2f}%. Pipe 2: {p2_field:.2f}%.")
else:
    print(f"For {hours_worker_missing} hours the pool overflows with {(field - volume_of_the_pool):.2f} liters.")


