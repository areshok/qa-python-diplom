class TestCaseBurget:

    def test_burger_set_buns(self, burger, bun):
        "тест: проверка добавление булки"
        assert burger.bun is None
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_burger_add_ingredient(self, burger, ingridient):
        "тест: проверка добавление ингридиента"
        assert len(burger.ingredients) == 0
        assert type(burger.ingredients) is list
        burger.add_ingredient(ingridient)
        assert len(burger.ingredients) == 1

    def test_burger_remove_ingredient(self, burger, ingridient, ingridient_2):
        "тест: проверка удаление ингридиента"
        assert len(burger.ingredients) == 0
        burger.add_ingredient(ingridient)
        burger.add_ingredient(ingridient_2)
        assert len(burger.ingredients) == 2
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == ingridient_2.get_name()

    def test_burger_move_ingredient(self, burger, ingridient, ingridient_2):
        "тест: проверка перемещение ингридиента"
        burger.add_ingredient(ingridient)
        burger.add_ingredient(ingridient_2)
        assert burger.ingredients[0].get_name() == ingridient.get_name()
        assert burger.ingredients[1].get_name() == ingridient_2.get_name()
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].get_name() == ingridient_2.get_name()
        assert burger.ingredients[1].get_name() == ingridient.get_name()

    def test_burger_get_price(self, burger, bun, ingridient):
        "тест: проверка получение цены"
        burger.set_buns(bun)
        burger.add_ingredient(ingridient)
        price_1 = (bun.get_price() * 2) + ingridient.get_price()
        price_2 = burger.get_price()
        assert price_2 == price_1

    def test_burger_get_receipt(self, burger, bun, ingridient):
        "тест: проверка получение рецепта"
        result_test = [f'(==== {bun.get_name()} ====)']
        result_test.append(f'= {str(ingridient.get_type()).lower()} {ingridient.get_name()} =')
        result_test.append(f'(==== {bun.get_name()} ====)\n')
        test_price = (bun.get_price() * 2) + ingridient.get_price()
        result_test.append(f'Price: {test_price}')
        result_test = "\n".join(result_test)

        burger.set_buns(bun)
        burger.add_ingredient(ingridient)
        result_burger = burger.get_receipt()
        assert result_burger == result_test
