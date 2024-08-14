import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Carregue a biblioteca compartilhada
lib = ctypes.CDLL('../libmandelbrot.so')

# Defina os tipos de argumentos e retorno da função
lib.calculate_mandelbrot.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte)]
lib.calculate_mandelbrot.restype = None

def generate_mandelbrot(width, height, max_iter):
    output = np.zeros((height, width), dtype=np.uint8)
    lib.calculate_mandelbrot(width, height, max_iter, output.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte)))
    return output

if __name__ == "__main__":
    width, height = 800, 600
    max_iter = 100
    
    mandelbrot = generate_mandelbrot(width, height, max_iter)
    
    plt.imshow(mandelbrot, cmap='hot', extent=[-2, 2, -2, 2])
    plt.colorbar()
    plt.title('Conjunto de Mandelbrot')
    plt.show()