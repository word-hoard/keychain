from msvcrt import getch

class Keychain:
    """
    ============================================
    WARNING :
    CHECK THE ESC KEY IS 27 OR YOU WILL BE UPSET
    ============================================
    a proof of concept for using decorators to 
    bind letter keypresses to functions.
    - getch only seems to work on letters
    and goes a bit odd for other keys
    """
    _esc = 27 # DO NOT GIVE TO USERS!
    _r = {}

    @classmethod
    def register_fn(cls, *args):
        def decorator(fn):
            cls._r[fn] = args
            return fn
        return decorator

    @classmethod
    def _check_key(cls, key):
        for fn in cls._r:
            if chr(key) in cls._r[fn]:
                fn()

    @classmethod
    def mainloop(cls):
        while True:
            key = ord(getch())
            if key == cls._esc: #ESC
                break
            else:
                try:
                    cls._check_key(key)
                except:
                    pass

bind_key = Keychain.register_fn
key_loop = Keychain.mainloop

if __name__ == '__main__':

    # tests

    test_var = 'a and s'

    @bind_key('a', 's')
    def test1(test= test_var):
         print(test)

    @bind_key('d', 'w')
    def test2():
        print('north, east')
    
    print(Keychain._r)
    key_loop()






