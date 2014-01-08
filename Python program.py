import os
import time

print 'Python program'

mount_point_dir = '/media/KARTA'

media_is_mounted = False

if os.path.isdir(mount_point_dir) and os.path.exists(mount_point_dir):
	media_is_mounted = True

print(media_is_mounted)

while True:
	media_is_mounted = False
	
	if os.path.isdir(mount_point_dir) and os.path.exists(mount_point_dir):
		media_is_mounted = True
	
	print(media_is_mounted)
	
	
	time.sleep(2)


