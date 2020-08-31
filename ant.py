import pygame
import numpy as np
from pygame import surfarray

from pygame import gfxdraw
from pygame import Color

from timeit import default_timer as timer

pygame.init()

s=1024
w = s
h = s
xM=w-1
yM=h-1

display = pygame.display.set_mode((w, h))

arr = np.zeros((w,h,3),dtype=np.uint8)

surf2 = pygame.Surface((w, h))


adir = 0
ax=int(s/2)
ay=int(s/2)


init_time = timer()
frames_displayed = 0
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	
	for i in range(10000): #100k =3.2fps @1024
		c=arr[ax,ay][0]
		if c == 0:
			c = 255
			if adir == 3:
				adir = 0
			else:
				adir = adir+1
		else:
			c = 0
			if adir == 0:
				adir = 3
			else:
				adir = adir-1
		
		arr[ax,ay][0]=c
		
		if adir == 0:
			if ax == xM:
				ax=0
			else:
				ax=ax+1
		elif adir == 1:
			if ay == yM:
				ay=0
			else:
				ay=ay+1
		elif adir == 2:
			if ax == 0:
				ax=xM
			else:
				ax=ax-1
		elif adir == 3:
			if ay == 0:
				ay=yM
			else:
				ay=ay-1
				
			

	#field[np.random.randint(w),np.random.randint(h)] = np.random.randint(255,size=3,dtype=np.uint8)
	
	# updating the image
	#for x in range(w):
	#	for y in range(h):
	#		c=Color(int(x*0.25),int(y*0.25),0)
	#		surf2.set_at((x, y), c) #5.2 fps @512


	surfarray.blit_array(display, arr) #slower
	#display.blit(surf2, (0, 0))
	pygame.display.flip()

	frames_displayed+=1


print("average frame rate:", frames_displayed/(timer()-init_time), "fps")

pygame.quit()
