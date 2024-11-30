import drawcocktailsort
import time
from cocktailsort import cocktailsort_

def sort_squares(squares, data_, speed):
    gen = cocktailsort_( data_ )
    for data in gen:
        time.sleep( 5 / speed )
        yield
        step_squares( data, squares )
    time.sleep( 5 / speed )
    drawcocktailsort.remove_bubble( squares )
    yield

def step_squares(data, squares):
    drawcocktailsort.draw_bubble( squares, data[ 1 ], data[ 2 ] )
    print( data )
    if ( data[ 3 ] == True ):
        drawcocktailsort.swap_squares( squares, data[ 1 ], data[ 2 ] )