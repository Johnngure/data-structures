#function define outside of class
def f1(self, x, y):
    return min (x, x+y)
class c:
    f = f1
    def g(self):
        return 'hello world'

    h = g     