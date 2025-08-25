def savings(gross_pay, tax_rate, expenses):
    after_tax_pay = int(gross_pay * (1 - tax_rate))
    remaining_money = after_tax_pay - expenses
    return remaining_money

def material_waste(total_material, material_units, num_jobs, job_consumption):
    consumed_material = num_jobs * job_consumption
    remaining_material = total_material - consumed_material
    return str(remaining_material) + material_units

def interest(principal, rate, periods):
    simple_interest = principal * rate * periods
    final_value = principal + simple_interest
    return int(final_value)