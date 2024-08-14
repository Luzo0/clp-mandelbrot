#include "../include/mandelbrot.h"
#include <complex.h>

void calculate_mandelbrot(int width, int height, int max_iter, unsigned char* output) {
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            double real = (x - width/2.0) * 4.0/width;
            double imag = (y - height/2.0) * 4.0/height;
            double complex c = real + imag*I;
            double complex z = 0 + 0*I;
            int iter;
            
            for (iter = 0; iter < max_iter; iter++) {
                if (cabs(z) > 2.0) break;
                z = z*z + c;
            }
            
            output[y*width + x] = iter % 256;
        }
    }
}