import drawquicksort
import time
from quicksort import quicksort_

def sort_squares(squares_canvas, data_, speed):
    gen = quicksort_( data_, 0, len( data_ ) - 1 )
    for data in gen:
        time.sleep( 5 / speed )
        yield
        step_squares( squares_canvas, data )
    time.sleep( 5 / speed )
    drawquicksort.reset()
    yield

def step_squares(squares_canvas, data):
    print( data )
    if len( data) > 2:
        drawquicksort.swap_squares( squares_canvas, data[ 1 ], data[ 2 ] ) 
    drawquicksort.select_square( squares_canvas, data[ 1 ] )