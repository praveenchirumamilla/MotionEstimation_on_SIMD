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

	# write 12rows of newimage follwed by 12 rows of anchor image for 19 times
	for i in range(19):
		# write 12 lines of newImage to kin
		for i in range(12):
			count = 0
			value = ""
	
			while(count < 256):
				value = nFile.readline().strip()
				kFile.write(value)
				kFile.write("\n")
				
				count += 1
	
		
		# write 12 lines of anchor image to kin
		for i in range(12):
			count = 0
			value = ""
	
			while(count < 256):
				value = aFile.readline().strip()
				kFile.write(value)
				kFile.write("\n")
				
				count += 1


	#at the end write remaining 12 rows of newImage and 10 rows of anchor image
	# write last 12 lines of newImage to kin
	for i in range(12):
		count = 0
		value = ""

		while(count < 256):
			value = nFile.readline().strip()
			kFile.write(value)
			kFile.write("\n")
			
			count += 1

	
	# write last 10 lines of anchor image to kin
	for i in range(10):
		count = 0
		value = ""

		while(count < 256):
			value = aFile.readline().strip()
			kFile.write(value)
			kFile.write("\n")
			
			count += 1
		

generateKin()
	
