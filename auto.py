import random
auto = ['Subaru', 'Priora', 'Omoda', 'Mclaren', 'VAZ', 'UAZ', 'KAMAZ', 'BMW']

san = random.choices(auto)
print(san)

print('Автомобили под санкциями') if (san == 'Mclaren' or san == 'BMW') else print('Автомобили не под санкциями')

ass = 'Есть автомобиль под санкциями' if (san == 'Mclaren' or san == 'BMW') else 'Автомобиль не под санкциями'
print(ass)

