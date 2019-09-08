# DUCK TYPING
class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Compiling")
        print("Compiling")
        print("Running")


class Laptop:

    def code(self, ide):
        ide.execute()


lap1 = Laptop()
ide = MyEditor()

lap1.code(ide)