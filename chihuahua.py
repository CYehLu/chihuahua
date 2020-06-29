from time import sleep
from PIL import Image
import numpy as np


def _imag2dots(rot_deg, background='white'):
    imag = Image.open('WhiteTanChihuahua5.png')
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


def chihuahua(background='white', time=0.25, rotate=False):
    def decorator(func):
        def inner(*args, **kwargs):
            thetas = np.linspace(0, 360, 10) if rotate else [0]
            for theta in thetas:
                dogggggggg = _imag2dots(theta, background)
                print(dogggggggg)
                sleep(time)
            print('吉娃娃向你說好！')
            return func(*args, **kwargs)
        return inner
    return decorator