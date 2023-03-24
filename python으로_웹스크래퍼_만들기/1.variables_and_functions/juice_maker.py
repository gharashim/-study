def makeP_juice(fruit):
    return f"{fruit} "

def add_ice(juice):
    return f"{juice} + ice "

def add_surgar(iced_juice):
    return f"{iced_juice} + sugar "

juice = makeP_juice("apple")
cold_juice = add_ice(juice)
sugar_juice = add_surgar(cold_juice)

print(sugar_juice + 'juice')
