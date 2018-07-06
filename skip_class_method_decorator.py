
def skip(method_name):
    def wrap1(klass):

        def wrap2(*args, **kwargs):
            obj = klass(*args, **kwargs)
            setattr(obj, method_name, lambda *x, **y: None)
            return obj

        return wrap2
    return wrap1


@skip('ban')
class A:
    def man(self):
        return 1

    def ban(self):
        return 2


if __name__=='__main__':
    obj = A()
    print(obj.man())
    print(obj.ban())
