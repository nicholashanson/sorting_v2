import drawinsertionsort
import time
from insertionsort import insertionsort_

def sort_squares(squares_canvas, data_, speed):
    gen = insertionsort_( data_ )
    for data in gen:
        time.sleep( 2 / speed )
        yield
        step_squares( squares_canvas, data )
    time.sleep( 2 / speed )
    drawinsertionsort.reset()
    yield

def step_squares(squares_canvas, data):
    print( data )
    if len( data[ 0 ] ) == data[ 1 ]:
        drawinsertionsort.remove_bubble( squares_canvas, data[ 2 ] )
        return
    if ( data[ 3 ] == True ):
        drawinsertionsort.swap_squares( squares_canvas, data[ 2 ] )
    drawinsertionsort.select_squares( squares_canvas, data[ 1 ], data[ 2 ] )