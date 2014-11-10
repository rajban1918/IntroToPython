# def grid1():
#     print '+ - - - - + - - - - +'
#     print '|         |         |'
#     print '|         |         |'
#     print '|         |         |'
#     print '|         |         |'
#     print '+ - - - - + - - - - +'
#     print '|         |         |'
#     print '|         |         |'
#     print '|         |         |'
#     print '|         |         |'
#  # print '+ - - - - + - - - - +'

# #grid1()

def printed_grid(n): # This function lets you choose how many boxes, with 2 columns only
    s = '+ - - - - + - - - - +' + '\n'
    t = ('|         |         |' + '\n')*4
    mid_lines = int((n-2) // 2)
    middle = mid_lines*(t + s) + t
   
    if n ==1:
        print "Sorry, you need more than 1 box!"
    
    if n%2 != 0:
         print "The number of boxes is: ",n,"- 1 =", n-1
         n = n - 1
    elif n%2==0:
        print "The number of boxes is: ", n
   
    if n != 0:
        print s, middle, s

# printed_grid(6)

def printed_grids(length): #This function changes the sizes of the boxes , but is always a 2x2 grid
    c = int((length-2)//2) 
    s = ('+' + ' -' * c + ' +' + ' -' * c + ' +') + '\n'
    t = ('| ' + '  ' * c + '| ' + '  ' * c + '|') + '\n'
    middle = t*c + s + t*c   

    if (length<4) or (length%2 == 0):
        print 'Sorry! The argument should be bigger than 3 and an odd number'
    else:
        print s,middle,s

# printed_grids(19)

def dynamic_printed_grids(rows, columns, size): #this function lets you choose how many rows, columns, and the size of the boxes
    cSize = int((size-2)//2) 
    s = '+ ' + ((('- ' * cSize ) + '+ ')* columns)  + '\n'
    t =  '| ' + (('  ' * cSize + '| ') * columns)  + '\n'
    middle = (t*cSize + s) * rows

    if size <2:
        print "Choose an integer greater than 2"
    elif size%2 != 0:
        print "The size is: ", size, "- 1 =", size - 1, "and there are", rows, "rows with", columns, "columns"
    else:
        print "The size is", size, "and there are", rows, "rows with", columns, "columns"
    
    if size >=2:
        print s, middle

dynamic_printed_grids(4,3,6)

