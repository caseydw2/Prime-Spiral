# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 18:01:56 2022

@author: Casey
"""

from PIL import Image, ImageDraw
from math import sin,cos

def isprime(n):
    upper_bound = round(n**(0.5))
    i = upper_bound
    while i > 1:
        if n%i == 0:
            return False
        i -= 1
    return True

def plot_polar(p,center):
    return (p*cos(p)+center[0],p*sin(p)+center[1])

def draw_circle(point,im,factor):
    draw = ImageDraw.Draw(im)
    x,y = point[0],point[1]
    draw.ellipse([x-factor*0.25,y-factor*0.25,x+factor*0.25,y+factor*0.25],fill = "white")

def draw_spiral(sprl_num,factor = 50,save = False):
    size = (factor * sprl_num + round(factor/4),factor * sprl_num +round(factor/4) )
    i,k,j,l = 1,1,0,0
    
    im = Image.new("RGB",size)
    draw = ImageDraw.Draw(im)
    x,y = round(size[0]/2), round(size[1]/2)
    while k <= sprl_num:
        direction = 1 - 2*(k%2)
        newx,newy = x - direction*factor, y 
        draw.line([(x,y),(newx,newy)],width = 2)
        x,y = newx,newy
        while j < k:
            newx,newy = x, y + direction*factor
            draw.line([(x,y),(newx,newy)],width = 2)
            x,y = newx,newy
            i += 1
            if isprime(i):
                draw_circle((newx,newy),im,factor)
            j += 1
        j = 0
        while l < k:
            newx,newy = x + direction*factor, y
            draw.line([(x,y),(newx,newy)],width = 2)
            x,y = newx,newy
            i += 1
            if isprime(i):
                draw_circle((newx,newy),im,factor)
            l +=1
        l=0
        k +=1
    if save:
        im.save("Prime Spiral sprl_num {}, factor {}.png".format(sprl_num,factor))
    im.show()
    
def polar_prime_plot(ten_pwr,factor = 10,save=False):
    size = (round(10**ten_pwr*factor/5) ,round(10**ten_pwr*factor/5) )
    im = Image.new("RGB",size)
    x,y = round(size[0]/2), round(size[1]/2)
    for i in range(round(10**ten_pwr)):
        if isprime(i):
            draw_circle(plot_polar(i,(x,y)),im,factor*8)
    if save:
        im.save("polar prime plot ten_pwr {}, factor {}.png".format(ten_pwr,factor))
    im.show()
            