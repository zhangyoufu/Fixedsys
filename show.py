from PIL import Image
import re
import sys

filename = sys.argv[1]

f = open( filename )
for i in xrange(5): f.readline()
height = int( re.match( 'height (\d+)', f.readline() ).group(1) )
for i in xrange(10): f.readline()

chars = []
rows = 14
cols = 16
max_width = 0
for i in xrange(256):
	assert f.readline() == 'char %d\n' % i
	width = int( re.match( 'width (\d+)', f.readline() ).group(1) )
	if i < 32 and width: rows = 16
	max_width = max( max_width, width )
	char = Image.new( '1', (width,height), 1 )
	if width:
		pix = char.load()
		for y in xrange(height):
			line = f.readline()
			for x in xrange(width):
				pix[x,y] = 1-int(line[x])
	chars.append( char )
	f.readline()

im = Image.new( '1', ((max_width+1)*cols+1,(height+1)*rows+1), 0 )
skip = 16-rows
for i in xrange(16*skip,256):
	x = i % 16 * (max_width+1) + 1
	y = (i // 16 - skip) * (height+1) + 1
	char = Image.new( '1', (max_width,height), 1 )
	char.paste( chars[i], (0,0) )
	im.paste( char, (x,y) )

if filename.endswith('.fd'): filename = filename[:-3]

im.save( filename+'.png' )
