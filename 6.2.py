# encapsulation


class ATM:
    def __init__(self, name, amount):
        self.name = name  # public
        self.__amount = amount  # private

    def show(self):
        print(f"{self.name}")
        print(f"{self.__amount}")


object = ATM("John", 1000)
object.show()
