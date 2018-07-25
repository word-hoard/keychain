## keychain

# A proof of concept script for using decorators to bind letter key-presses to functions.

Written in response to a tweet by [@AlSweigart](https://twitter.com/AlSweigart) for his [pykeymouse project](https://github.com/asweigart/pykeymouse) where he was asking what sort of api folk would like. I rather glibly asked for a decorator based format with only half an idea how it could be done, so I'm feeling pretty happy to have chased down the relevant stack overflow answers, read the right bit of 'fluent python' and hammered this together.

Getch only seems to work on letters and goes a bit odd for other keys, and I have paid no nevermind to keyboard variation. This is a quick sketch to flesh out an idea, not a real thing. 

# usage

    ============================================
    WARNING :
    CHECK THE ESC KEY IS 27 OR YOU WILL BE UPSET
    ============================================

```python
from keychain import bind_key, key_loop

print('press esc to exit')

test_var = 'a and s'

@bind_key('a', 's')
def test1(test= test_var):
     print(test)

@bind_key('d', 'w')
def test2():
    print('north, east')

key_loop()
```
