#!/usr/bin/env python3

import sys
import math
import base64
import tkinter

from io import BytesIO
from PIL import Image as PILImage

## NO ADDITIONAL IMPORTS ALLOWED!

class Image:
    def __init__(self, width, height, pixels):
        self.width = width
        self.height = height
        self.pixels = pixels

    def get_pixel(self, x, y):
        #handles out of bounds pixels
        if(x < 0):
            x = 0
        if(x >= self.width):
            x = self.width - 1
        if(y < 0):
            y = 0
        if(y >= self.height):
            y = self.height - 1
        #first bug- turns 2d value into 1d value
        value = y * self.width + x
        return self.pixels[value]

    def set_pixel(self, x, y, c):
        #second bug- same problem as first bug
        value = y * self.width + x
        self.pixels[value] = c

    def apply_per_pixel(self, func):
        result = Image.new(self.width, self.height)
        for x in range(result.width):
            for y in range(result.height):
                color = self.get_pixel(x, y)
                newcolor = func(color)
                #clips out of bounds pixel values
                if(newcolor < 0):
                    newcolor = 0
                if(newcolor > 255):
                    newcolor = 255  
                #bug- switched x and y
                #rounds newcolor float values to integers
                result.set_pixel(x, y, int(round(newcolor)))
        
        return result
    
    def correlation(self, kernel):
        #kernel = Image.new()
        result = Image.new(self.width, self.height)
        total = 0
        #the span is the max number of steps in a single dimension that it would take to reach all cells of the kernel
        span = math.floor(((kernel.width)-1)/2)
        for i in range(0, self.width):
            for j in range(0, self.height):
                #this total will come to equal the final value of the image pixel that lies below the middle pixel of the kernel
                total = 0
                for a in range(-span, span + 1):
                    for b in range(-span, span + 1):
                        pixel = self.get_pixel(i+a, j+b)
                        total += pixel * kernel.get_pixel(a + span, b + span)
                result.set_pixel(i, j, total)
        return result
    
    def blurred(self, n):
        #treat kernel as an image
        kern = Image.new(n, n)
        numBoxes = n*n
        element = float(1/numBoxes)
        for i in range(n):
            for j in range(n):
                kern.set_pixel(i, j, element)
        result = self.correlation(kern)
        
        #this whole section just rounds pixel values to nearest integer
        for x in range(result.width):
            for y in range(result.height):
                value = result.get_pixel(x, y)
                roundedValue = round(value)
                result.set_pixel(x, y, roundedValue)
        return result
    
    
    def sharpened(self, n):
        result = Image.new(self.width, self.height)
        blurredImage = self.blurred(n)
        for i in range(result.width):
            for j in range(result.height):
                #final value = int(round(2(imagePixel) - blurredPixel))
                initialValue = 2*(self.get_pixel(i, j))
                subtractingValue = blurredImage.get_pixel(i, j)
                finalValue = int(round(initialValue - subtractingValue))
                result.set_pixel(i, j, finalValue)
                result.sand(i, j)
        return result

    def sand(self, x, y):
        pixel = int(round(self.get_pixel(x, y)))
        if pixel < 0:
            self.set_pixel(x, y, 0)
        elif pixel > 255:
            self.set_pixel(x, y, 255)
    
    def edges(self):
        result = Image.new(self.width, self.height)
        kernelX = Image.new(3, 3)
        kernelY = Image.new(3, 3)
        
        #sets the two kernels used for all edge detection
        kernelX.set_pixel(0, 0, -1)
        kernelX.set_pixel(0, 1, -2)
        kernelX.set_pixel(0, 2, -1)
        kernelX.set_pixel(1, 0, 0)
        kernelX.set_pixel(1, 1, 0)
        kernelX.set_pixel(1, 2, 0)
        kernelX.set_pixel(2, 0, 1)
        kernelX.set_pixel(2, 1, 2)
        kernelX.set_pixel(2, 2, 1)
        
        kernelY.set_pixel(0, 0, -1)
        kernelY.set_pixel(0, 1, 0)
        kernelY.set_pixel(0, 2, 1)
        kernelY.set_pixel(1, 0, -2)
        kernelY.set_pixel(1, 1, 0)
        kernelY.set_pixel(1, 2, 2)
        kernelY.set_pixel(2, 0, -1)
        kernelY.set_pixel(2, 1, 0)
        kernelY.set_pixel(2, 2, 1)
        
        Ox = self.correlation(kernelX)
        Oy = self.correlation(kernelY)
        for i in range(result.width):
            for j in range(result.height):
                OxPixel = Ox.get_pixel(i, j)
                OyPixel = Oy.get_pixel(i, j)
                final = round(math.sqrt(OxPixel**2 + OyPixel**2))
                result.set_pixel(i, j, final)
                result.sand(i, j)   
        return result
        
    def sum_energies(self):
        total= 255 * self.height
        newTotal = 0
        removeCol = 0
        for i in range(self.width):
            for j in range(self.height):
                #newTotal will be the sum total of all the pixels for each column
                newTotal += self.get_pixel(i, j)
            #this conditional will find the least energetic column
            if newTotal < total:
                removeCol = i
                total = newTotal
            print(newTotal)
            newTotal = 0
        print(removeCol)
        return removeCol
    
    def retarget(self, iterations):
        original = self    
        for i in range(iterations):
            #computes a new energy map for each iteration
            energy = original.edges()
            #minus 1 because the new image will have 1 less column
            mutable = Image.new(original.width-1, original.height)            
            remove = energy.sum_energies()                        
            for x in range(original.width):
                #for all columns before the least energetic column
                if(x < remove):
                    for y in range(original.height):
                        value = original.get_pixel(x, y)
                        mutable.set_pixel(x, y, value)
                #for all columns immediately after the least energetic column
                elif(x != remove):
                    for y in range(original.height):
                        value = original.get_pixel(x,y)
                        mutable.set_pixel(x-1, y, value)
            original = mutable
        return mutable
                           

    def inverted(self):
        #bug- 256 switched to 255
        return self.apply_per_pixel(lambda c: 255-c)


    # Below this point are utilities for loading, saving, and displaying
    # images, as well as for testing.

    def __eq__(self, other):
        return all(getattr(self, i) == getattr(other, i)
                   for i in ('height', 'width', 'pixels'))

    @classmethod
    def load(cls, fname):
        """
        Loads an image from the given file and returns an instance of this
        class representing that image.  This also performs conversion to
        grayscale.

        Invoked as, for example:
           i = Image.load('test_images/cat.png')
        """
        with open(fname, 'rb') as img_handle:
            img = PILImage.open(img_handle)
            img_data = img.getdata()
            if img.mode.startswith('RGB'):
                pixels = [round(.299*p[0] + .587*p[1] + .114*p[2]) for p in img_data]
            elif img.mode == 'LA':
                pixels = [p[0] for p in img_data]
            elif img.mode == 'L':
                pixels = list(img_data)
            else:
                raise ValueError('Unsupported image mode: %r' % img.mode)
            w, h = img.size
            return cls(w, h, pixels)

    @classmethod
    def new(cls, width, height):
        """
        Creates a new blank image (all 0's) of the given height and width.

        Invoked as, for example:
            i = Image.new(640, 480)
        """
        return cls(width, height, [0 for i in range(width*height)])

    def save(self, fname, mode='PNG'):
        """
        Saves the given image to disk or to a file-like object.  If fname is
        given as a string, the file type will be inferred from the given name.
        If fname is given as a file-like object, the file type will be
        determined by the 'mode' parameter.
        """
        out = PILImage.new(mode='L', size=(self.width, self.height))
        out.putdata(self.pixels)
        if isinstance(fname, str):
            out.save(fname)
        else:
            out.save(fname, mode)
        out.close()

    def gif_data(self):
        """
        Returns a base 64 encoded string containing the given image as a GIF
        image.

        Utility function to make show_image a little cleaner.
        """
        buff = BytesIO()
        self.save(buff, mode='GIF')
        return base64.b64encode(buff.getvalue())

    def show(self):
        """
        Shows the given image in a new Tk window.
        """
        global WINDOWS_OPENED
        if tk_root is None:
            # if tk hasn't been properly initialized, don't try to do anything.
            return
        WINDOWS_OPENED = True
        toplevel = tkinter.Toplevel()
        # highlightthickness=0 is a hack to prevent the window's own resizing
        # from triggering another resize event (infinite resize loop).  see
        # https://stackoverflow.com/questions/22838255/tkinter-canvas-resizing-automatically
        canvas = tkinter.Canvas(toplevel, height=self.height,
                                width=self.width, highlightthickness=0)
        canvas.pack()
        canvas.img = tkinter.PhotoImage(data=self.gif_data())
        canvas.create_image(0, 0, image=canvas.img, anchor=tkinter.NW)
        def on_resize(event):
            # handle resizing the image when the window is resized
            # the procedure is:
            #  * convert to a PIL image
            #  * resize that image
            #  * grab the base64-encoded GIF data from the resized image
            #  * put that in a tkinter label
            #  * show that image on the canvas
            new_img = PILImage.new(mode='L', size=(self.width, self.height))
            new_img.putdata(self.pixels)
            new_img = new_img.resize((event.width, event.height), PILImage.NEAREST)
            buff = BytesIO()
            new_img.save(buff, 'GIF')
            canvas.img = tkinter.PhotoImage(data=base64.b64encode(buff.getvalue()))
            canvas.configure(height=event.height, width=event.width)
            canvas.create_image(0, 0, image=canvas.img, anchor=tkinter.NW)
        # finally, bind that function so that it is called when the window is
        # resized.
        canvas.bind('<Configure>', on_resize)
        toplevel.bind('<Configure>', lambda e: canvas.configure(height=e.height, width=e.width))


try:
    tk_root = tkinter.Tk()
    tk_root.withdraw()
    tcl = tkinter.Tcl()
    def reafter():
        tcl.after(500,reafter)
    tcl.after(500,reafter)
except:
    tk_root = None
WINDOWS_OPENED = False

if __name__ == '__main__':
    # code in this block will only be run when you explicitly run your script,
    # and not when the tests are being run.  this is a good place for
    # generating images, etc.
    
#    kernel = Image(5, 5,
#                       [0.04, 0.04, 0.04, 0.04, 0.04, 
#                        0.04, 0.04, 0.04, 0.04, 0.04,
#                        0.04, 0.04, 0.04, 0.04, 0.04,
#                        0.04, 0.04, 0.04, 0.04, 0.04,
#                        0.04, 0.04, 0.04, 0.04, 0.04])
#    
#    im = Image.load('test_images/pigbird.png')
#    retarget = im.retarget(100)
#    retarget.save('retargettedPigbird.png')

    # the following code will cause windows from Image.show to be displayed
    # properly, whether we're running interactively or not:
    if WINDOWS_OPENED and not sys.flags.interactive:
        tk_root.mainloop()
