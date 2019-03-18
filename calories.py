#Po-I Wu
#program calories_counter
#This program calculate calories from fat and carbs

def fat_calories(fat):
    fatty = fat * 9
    return fatty

def carb_calories(carbs):
    carbohydrates = carbs * 4
    return carbohydrates

def main():
    fat_grams = float(input("How many grams of fat did you consume yesterday?"))
    carb_grams = float(input("How many grams of carbs did you consume yesterday?"))

    total_fat = fat_calories(fat_grams)
    total_carbs = carb_calories(carb_grams)

    print("The total amount of calories from fat is:", total_fat)
    print("The total amount of calories from carbs is:", total_carbs)

    print("The total amount of calories from both are:", total_fat+total_carbs)

main()
