import os
import sys


def generateKin():
	"""generates kin file for 256x256 image motion estimation"""
	
	aFile = open("anchorImage")
	nFile = open("newImageGold")
	kFile = open("kin", "w")	

	# write first 16 lines of newImage to kin
	for i in range(16):
		count = 0
		value = ""

		while(count < 256):
			value = nFile.readline().strip()
			kFile.write(value)
			kFile.write("\n")
			
			count += 1

	
	# write first 18 lines of anchor image to kin
	for i in range(18):
		count = 0
		value = ""

		while(count < 256):
			value = aFile.readline().strip()
			kFile.write(value)
			kFile.write("\n")
			
			count += 1

	# write 16rows of newimage follwed by 16 rows of anchor image for 14 times
	for i in range(14):
		# write 16 lines of newImage to kin
		for i in range(16):
			count = 0
			value = ""
	
			while(count < 256):
				value = nFile.readline().strip()
				kFile.write(value)
				kFile.write("\n")
				
				count += 1
	
		
		# write 16 lines of anchor image to kin
		for i in range(16):
			count = 0
			value = ""
	
			while(count < 256):
				value = aFile.readline().strip()
				kFile.write(value)
				kFile.write("\n")
				
				count += 1


	#at the end write remaining 16 rows of newImage and 14 rows of anchor image
	# write last 16 lines of newImage to kin
	for i in range(16):
		count = 0
		value = ""

		while(count < 256):
			value = nFile.readline().strip()
			kFile.write(value)
			kFile.write("\n")
			
			count += 1

	
	# write last 14 lines of anchor image to kin
	for i in range(14):
		count = 0
		value = ""

		while(count < 256):
			value = aFile.readline().strip()
			kFile.write(value)
			kFile.write("\n")
			
			count += 1
		

generateKin()
	
