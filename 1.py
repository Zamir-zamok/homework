def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function

inner_function #вызов данной фукции выдает ошибку, вследствие различия пространства имён