import drawselectionsort
import time
from selectionsort import selectionsort_

def sort_squares(squares_canvas, data_, speed):
    gen = selectionsort_( data_ )
    for data in gen:
        time.sleep( 5 / speed )
        yield
        step_squares( squares_canvas, data )
    time.sleep( 5 / speed )
    drawselectionsort.reset()
    yield

def step_squares(squares_canvas, data):
    print( data )
    if data[ 4 ] == True:
        drawselectionsort.swap_squares( squares_canvas, data[ 1 ], data[ 2 ] ) 
    drawselectionsort.select_squares( squares_canvas, len(data[0]), data[ 1 ], data[ 2 ], data[ 3 ] )