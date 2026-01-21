#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

fake = Faker()

def create_restaurants():
    restaurants = []
    for i in range(5):
        r = Restaurant(
            name=fake.company(),
            address=fake.address(),
        )
        restaurants.append(r)

    return restaurants

def create_pizzas():
    pizzas = []
    ingredients = [
        "Dough, Tomato Sauce, Cheese",
        "Dough, Tomato Sauce, Cheese, Pepperoni",
        "Dough, Sauce, Ricotta, Red peppers, Mustard",
        "Dough, BBQ Sauce, Cheese, Chicken, Red Onion",
        "Dough, Tomato Sauce, Cheese, Mushrooms, Olives"
    ]
    
    names = ["Emma", "Geri", "Melanie", "BBQ Chicken", "Veggie Supreme"]
    
    for i in range(5):
        p = Pizza(
            name=names[i],
            ingredients=ingredients[i],
        )
        pizzas.append(p)

    return pizzas

def create_restaurant_pizzas(restaurants, pizzas):
    restaurant_pizzas = []
    for restaurant in restaurants:
        for i in range(randint(1, 3)):
            rp = RestaurantPizza(
                restaurant_id=restaurant.id,
                pizza_id=rc(pizzas).id,
                price=randint(1, 30),
            )
            restaurant_pizzas.append(rp)

    return restaurant_pizzas

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        
        # Clear existing data
        RestaurantPizza.query.delete()
        Restaurant.query.delete()
        Pizza.query.delete()
        
        print("Creating restaurants...")
        restaurants = create_restaurants()
        db.session.add_all(restaurants)
        db.session.commit()

        print("Creating pizzas...")
        pizzas = create_pizzas()
        db.session.add_all(pizzas)
        db.session.commit()

        print("Creating restaurant pizzas...")
        restaurant_pizzas = create_restaurant_pizzas(restaurants, pizzas)
        db.session.add_all(restaurant_pizzas)
        db.session.commit()

        print("Done seeding!")