from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class BunData:
    CASES = [
        ("Classic Bun", 50.0),
        ("Black Bun",   75.5)
    ]


class IngredientData:
    SAUCE_CASES = [
        ("hot sauce",   100),
        ("sour cream",  200),
        ("chili sauce", 300)
    ]
    FILLING_CASES = [
        ("cutlet",   100),
        ("dinosaur", 200),
        ("sausage",  300)
    ]


class DatabaseData:
    BUN_CASES = [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ]
    INGREDIENT_CASES = [
        (0, INGREDIENT_TYPE_SAUCE,   "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE,   "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE,   "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300)
    ]


class BurgerData:
    MOVE_CASES = [
        (["Lettuce", "Tomato", "Onion"],         0, 2, ["Tomato", "Onion", "Lettuce"]),
        (["Patty", "Cheese", "Bacon", "Pickle"], 3, 1, ["Patty", "Pickle", "Cheese", "Bacon"])
    ]

    RECEIPT_BUN_NAME = "TestBun"
    RECEIPT_BUN_PRICE = 3.0
    RECEIPT_INGREDIENTS = [
        ("sauce",   "Hot",  1.0),
        ("filling", "Meat", 4.0)
    ]
