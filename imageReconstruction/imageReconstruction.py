import numpy
import sys

def decodeBlkRowColIndex(blockId):
	row = (blockId/4)*4
	col = (blockId%4)*4

	return row, col

def imageReconstruction(anchorImage, motionVecFile):
	"""Reconstructs the Image from Anchor image and motion vector file"""	

	totRows   = 16
	totCols   = 16
	rowsInBlk = 4
	colsInBlk = 4
	totBlocks = 16	

	#initialize the anchor image and new image matrix
	aImage = numpy.zeros((totRows, totCols), dtype = numpy.uint8)
	nImage = numpy.zeros((totRows, totCols), dtype = numpy.uint8)

	#read in the anchor image file
	aFile = open(anchorImage)
	for row in range(totRows):
		for col in range(totCols):
			aImage[row][col] = int(aFile.readline().strip())

	#read in the redundant image file
	blockId = 0	
	rowVec = numpy.zeros(1, dtype = numpy.int8)
	colVec = numpy.zeros(1, dtype = numpy.int8)
	data   = numpy.zeros(1, dtype = numpy.int8)
	
	mFile = open(motionVecFile)
	for blk in range(totBlocks):
		#(0,0) position in new image
		blkRow, blkCol = decodeBlkRowColIndex(blockId)
		
		#signed displacement of motion vector
		rowVec[0] = int(mFile.readline())
		colVec[0] = int(mFile.readline())
		
		#the(0,0) position in anchor image
		# the (rowVec, colVec) = (x, y)
		# movement along "X" axis is movement along column
		# movement along "Y" axis is movement along row
		aImgRow = blkRow - colVec[0]			
		aImgCol = blkCol + rowVec[0]			
	
		#print "blk = " + str(blk) + " " + str((blkRow, blkCol)) + " " + str((rowVec[0], colVec[0])) + " " + str((aImgRow, aImgCol))
		for bRow in range(rowsInBlk):
			for bCol in range(rowsInBlk):

				data[0] = int(mFile.readline())
				nImage[blkRow][blkCol] = aImage[aImgRow][aImgCol] - data[0]
				
				#print str((blkRow, blkCol)) + " " + str((blkRow, blkCol)) + " " +str((aImgRow, aImgCol))
				#increment the column indices
				blkCol  += 1
				aImgCol += 1

			#increment the row indices		
			blkRow  += 1
			aImgRow += 1
			blkCol  -= 4
			aImgCol -= 4
		#increment the block id
		blockId += 1	

	#write file result to new image file
	nFile = open("newImage", "w")
	
	for nRow in range(totRows):	
		for nCol in range(totCols):
			nFile.write(str(nImage[nRow][nCol]))
			nFile.write("\n")

	
imageReconstruction("kin", "motionVec")
