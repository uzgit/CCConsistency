#!/usr/bin/python3

class TripleThread:

    def __init__(self, source_node, register, thread):

        self.source_node = source_node
        self.register = register
        self.thread = thread

    def __repr__(self):
        representation = f"<{self.source_node}, {self.register}, {self.thread}>"
        return representation

    def __hash__(self):
        print(hash( self.__repr__() ))
        return hash( self.__repr__() )

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

class TripleRegister:

    def __init__(self, source_node, bad_register, potentially_bad_register):

        self.source_node = source_node
        self.bad_register = bad_register
        self.potentially_bad_register = potentially_bad_register

    def __repr__(self):
        representation = f"<{self.source_node}, {self.bad_register}, {self.potentially_bad_register}>"
        return representation

    def __hash__(self):
        print(hash( self.__repr__() ))
        return hash( self.__repr__() )

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

triple_1 = TripleThread("lalala", "hahaha", "penis")
triple_2 = TripleThread("lalala", "hahaha", "penis")
triple_3 = TripleThread("lalalafffff", "hahaha", "penis")
triple_4 = TripleRegister("lalalafffff", "hahaha", "penis")

alpha = set()
print(alpha)
alpha.add(triple_1)
print(alpha)
alpha.add(triple_2)
print(alpha)
alpha.add(triple_3)
print(alpha)
alpha.add(triple_4)
print(alpha)

