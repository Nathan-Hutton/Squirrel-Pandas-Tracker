import pandas

data = pandas.read_csv('squirrel_data.csv')
gray_squirrels = data[data['Primary Fur Color'] == 'Gray']
black_squirrels = data[data['Primary Fur Color'] == "Black"]
cinnamon_squirrels = data[data['Primary Fur Color'] == 'Cinnamon']
print(len(gray_squirrels) + len(black_squirrels) + len(cinnamon_squirrels))

squirrel_dict = {
    'Fur Colors': ["Gray", "Black", "Cinnamon"],
    'Count': [len(gray_squirrels), len(black_squirrels), len(cinnamon_squirrels)]
}
squirrel_dataframe = pandas.DataFrame(squirrel_dict)
squirrel_dataframe.to_csv("squirrel_count.cvs")