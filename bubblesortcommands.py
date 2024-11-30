import drawbubblesort
import time
from bubblesort import bubblesort_

def sort_squares(squares, data_, speed):
    gen = bubblesort_( data_ )
    drawbubblesort.draw_bubble( squares, 0 )
    for data in gen:
        time.sleep( 5 / speed )
        yield
        step_squares( data, squares )
    time.sleep( 5 / speed )
    drawbubblesort.remove_bubble( squares )
    drawbubblesort.reset()
    yield

def sort_bars(bars):
    gen = bubblesort_( data_ )
    drawbubblesort.draw_bubble( bars, 0 )
    for data in gen:
        time.sleep( 0.5 )
        step_bars( data, bars )
    time.sleep( 0.5 )
    drawbubblesort.remove_bubble( bars )

def step_bars(data, bars):
    drawbubblesort.draw_bubble( bars, data[ 1 ]  )
    if ( data[ 2 ] == True ):
        drawbubblesort.swap_bars( bars, data[ 1 ] )

def step_squares(data, squares):
    drawbubblesort.draw_bubble( squares, data[ 1 ]  )
    print( data )
    if ( data[ 2 ] == True ):
        drawbubblesort.swap_squares( squares, data[ 1 ] )