import ttkbootstrap as ttk
import bubblesort
from bucketsort import bucketsort_
from cocktailsort import cocktailsort_
from quicksort import quicksort_
from bubblesort import bubblesort_
from selectionsort import selectionsort_
from insertionsort import insertionsort_
import settings
import drawbubblesort
import window
import bubblesortcommands
import data


if __name__ == '__main__':

    
    f = ttk.Frame( master = window.w )
    
    bars = ttk.Canvas( master = f, 
                       height = settings.Y_HEIGHT + settings.square_width,
                       background = 'black' )
    squares = ttk.Canvas( master = f, 
                          height = settings.Y_HEIGHT + settings.square_width,
                          bg = 'lightcoral' )

    drawbubblesort.draw_bars( data.data_, bars )
    drawbubblesort.draw_squares( data.data_, squares )
    
    sort_squares_button = ttk.Button( window.w, text = "Sort Squares", command = lambda:
        bubblesortcommands.sort_squares( squares ) )
    sort_bars_button = ttk.Button( window.w, text = "Sort Bars", command = lambda:  
        bubblesortcommands.sort_bars( bars ) )
    
    options = [ 
        'Quicksort', 
        'Bubblesort',
        'Insertionsort',
        'Selectionsort',
        'Cocktailsort',
        'Bucketsort'
    ] 
  
    # datatype of menu text 
    clicked = ttk.StringVar() 
  
    # initial menu text 
    clicked.set( 'Quicksort' ) 
  
    # Create Dropdown menu 
    drop = ttk.OptionMenu( window.w , clicked , *options ) 
    drop.pack() 

    f.pack( side = 'left', fill = 'both', expand = True )
    bars.pack( side = 'left', fill = 'both', expand = True )
    squares.pack( side = 'left', fill = 'both', expand = True )
    sort_bars_button.pack()
    sort_squares_button.pack()
    ttk.Button(window.w, text="Quit", command=window.w.destroy).pack() 

    window.w.mainloop()