# Class and Object


# single inheritance


class vehicle:
    def properties(self):
        print("color:red")


class engine(vehicle):
    def prop(self):
        print("speed:2hp")


object = engine()
object.prop()


# multilevel inheritance


class A:
    def showA(self):
        print("class A")


class B(A):
    def showB(self):
        print("class B")


class C(B):
    def showC(self):
        print("class C")


object = C()
object.showA()
object.showB()
object.showC()


# heirarchical inheritance


class A:
    def ShowA(self):
        print("class A")


class B:
    def ShowB(self):
        print("class B")


class C(A, B):
    def showC(self):
        print("class C")


object = C()
object.ShowA()
object.ShowB()
object.showC()
