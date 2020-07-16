from time import sleep
from PIL import Image
import numpy as np


def _imag2dots(imag, rot_deg, background='white'):
    grey_imag = imag.convert('LA').rotate(rot_deg)
    arr = np.asarray(grey_imag)

    if background == 'white':
        code = {
            4: '  ',
            3: '░░',
            2: '▒▒',
            1: '▓▓',
            0: '██'
        }
    elif background == 'black':
        code = {
            0: '  ',
            1: '░░',
            2: '▒▒',
            3: '▓▓',
            4: '██'
        }
    else:
        raise ValueError(f'Unavailable color `{background}`')
    
    class_edge = np.linspace(0, 255+1, 6, dtype=int)
    
    white = arr[:,:,0]

    str_list = []
    for irow in range(white.shape[0]):
        class_ = np.sum((white[[irow],:].T - class_edge) >= 0, axis=1) - 1
        symbols = [code[c] for c in class_]
        str_row = ''.join(symbols)
        str_list.append(str_row + '\n')

    res = ''.join(str_list)
    return res


def _cstr(s, r, g, b):
    return f'\033[38;2;{r};{g};{b}m{s}\033[0m'


def _imag2cstr(imag, rot_deg):
    imag = imag.rotate(rot_deg)
    arr = np.asarray(imag)

    str_list = []
    shape = arr.shape
    for i in range(shape[0]):
        str_row = []
        for j in range(shape[1]):
            r, g, b, a = arr[i,j,:]
            symbol = _cstr('██', r, g, b)
            str_row.append(symbol)
        str_row = ''.join(str_row)
        str_list.append(str_row)

    res = '\n'.join(str_list)
    return res


def chihuahua(size=(35, 33), color=False, background='white', time=0.25, rotate=False):
    """
    size : 
        (width, height), image size (pixel)
    color : 
        bool, determine chihuahua is colored or black and white.
        This option can not work in some situations (e.g windows cmd).
    background : 
        'white' or 'black'. the console background color
        It is not necessary when color = True.
    time :
        Stopping time after each chihuahua is printed.
    rotate :
        bool, determine if chihuahua is rotated or not.
        
    Example
    -------
    >>> @chihuahua()
    >>> def test_func(a, b):
    >>>     return a + b
    >>>
    >>> test_func(1, b)
    
    """
    imag = Image.open('WhiteTanChihuahua2.png').resize(size)
    
    def decorator(func):
        def inner(*args, **kwargs):
            thetas = np.linspace(0, 360, 10) if rotate else [0]
            for theta in thetas:
                dogggggggg = _imag2cstr(imag, theta) if color else _imag2dots(imag, theta, background)
                print(dogggggggg)
                sleep(time)
            print('吉娃娃向你說好！')
            return func(*args, **kwargs)
        return inner
    
    return decorator