def dynamic_programming(products: dict, cash: int):
    def get_calories(products):
        calories = {}
        sorted_by_calories = {}
        for item in products.items():
            calories[item[1]['cost']] = item[1]['calories']

        sorted_by_calories = sorted(
            calories.items(), key=lambda item: item[1], reverse=True)

        # print("sorted by max calories:", sorted_by_calories)
        return sorted_by_calories

    def get_basket_by_cost(sorted_by_calories, cash):
        basket_by_cost = {}
        temp = cash
        for cost, calories in sorted_by_calories:
            if temp - cost >= 0:
                temp -= cost
                basket_by_cost[cost] = calories

        # print("basket_by_cost:",basket_by_cost)
        return basket_by_cost

    def get_basket_by_cost_calories(basket_by_cost):
        cost_calories = []
        [cost_calories.append({"cost": key, "calories": value})
         for key, value in basket_by_cost.items()]

        # print("cost_calories",cost_calories)
        return cost_calories

    def get_basket_by_product(cost_calories):
        basket = []
        for key, values in products.items():
            for item in cost_calories:
                if item == values:
                    basket.append(key)

        # print("Items of basket",basket)
        return basket

    var1 = get_calories(products)
    var2 = get_basket_by_cost(var1, cash)
    var3 = get_basket_by_cost_calories(var2)
    basket = get_basket_by_product(var3)

    return basket


def greedy_algorithm(products, cash):
    def get_cost_unit(products):
        basket_cost_unit = {}
        for item in products.values():
            basket_cost_unit[item["cost"]] = item["calories"]/item["cost"]

        sorted_by_max = sorted(
            basket_cost_unit.items(), key=lambda item: item[1], reverse=True)

        # print("sorted_by_max:", sorted_by_max)
        return sorted_by_max

    def get_by_cost(costs, cash):
        temp = cash
        basket_by_cost = {}
        for cost, calories in costs:
            if temp - cost >= 0:
                temp -= cost
                basket_by_cost[cost] = calories

        # print("basket_by_cost:",basket_by_cost)
        return basket_by_cost

    def get_cost_calories(costs):
        cost_calories = []
        for items in products.values():
            for cost in costs:
                if items['cost'] == cost:
                    cost_calories.append(items)

        # print("cost_calories:", cost_calories)
        return cost_calories

    def get_basket(cost_calories):
        basket = []
        for key, items in products.items():
            for item in cost_calories:
                if items == item:
                    basket.append(key)

        # print("basket:", basket)
        return basket

    var1 = get_cost_unit(products)
    var2 = get_by_cost(var1, cash)
    var3 = get_cost_calories(var2)
    basket = get_basket(var3)

    return basket


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

raport = greedy_algorithm(items, 100)
print("Кошик:", raport)

raport = dynamic_programming(items, 100)
print("Кошик:", raport)
