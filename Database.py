class Restaurant():
    def __init__(self, name, address, cuisine):
        self.name = name
        self.address = address
        self.cuisine = cuisine
    

dominoes = Restaurant("Dominoes", "www.dominoes.co.uk", "pizza")
yosushi = Restaurant("Yo Sushi!", "www.yosushi.co.uk", "sushi")
fiveguys = Restaurant("Five Guys", "www.fiveguys.co.uk" ,"burger")

restaurants = [dominoes.name, yosushi.name, fiveguys.name]
leave = False

while not leave:
    print("1. Display restaurant list")
    print("2. Add a restaurant")
    print("3. Exit")
    choice = int(input("Please enter you choice: "))

    if choice == 1:
        print(restaurants)

    elif choice == 2:
        name = input("Name: ")
        website = input("Website: ")
        cuisine = input("Cuisine: ")
        new_restaurant = Restaurant(name,website,cuisine)
        restaurants.append(new_restaurant.name)

    elif choice == 3:
        leave = True
    
    
        
    
    
