from django.shortcuts import render
from .data import DATA


def recipe_view(request, dish):
    # Получаем рецепт по имени блюда
    recipe = DATA.get(dish)

    # Если блюда нет — показываем страницу "не найдено"
    if recipe is None:
        return render(request, 'recipes/not_found.html', {'dish': dish})

    # Получаем число порций из GET-параметра (по умолчанию 1)
    servings_raw = request.GET.get('servings', 1)

    try:
        servings = int(servings_raw)
        if servings < 1:
            servings = 1
    except (ValueError, TypeError):
        servings = 1

    # Умножаем каждый ингредиент на число порций
    ingredients = {}
    for name, amount in recipe.items():
        ingredients[name] = amount * servings

    context = {
        'dish': dish,
        'ingredients': ingredients,
        'servings': servings,
    }
    return render(request, 'recipes/recipe.html', context)