from cat import Cats

cat_1 = Cats('Барон', 'мальчик', '2 года')
cat_2 = Cats('Сэм', 'мальчик', '2 года')

pets = [cat_1, cat_2]

for pet in pets:
    pet.print_list()
