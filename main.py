import tkinter as tk
root = tk.Tk()
import random
from tkinter import messagebox
import drawbubblesort
import drawcocktailsort
import drawselectionsort
import drawinsertionsort

import insertionsort

import settings
import bubblesortcommands
import cocktailsortcommands
import selectionsortcommands
import insertionsortcommands

root.geometry( str( settings.root_x ) + 'x' + str ( settings.root_y ) ) 

options_frame = tk.Frame( root, bg='pink' )
options_frame.place( width = settings.options_frame_width, 
                     height = settings.options_frame_height )

view_container_frame = tk.Frame( root, bg='lightgreen' )
view_container_frame.place( x = settings.view_container_x_offset, 
                            height = settings.view_container_frame_height )

status_bar = tk.Frame( root, bg='blue' )
status_bar.place( y = settings.status_bar_y_offset, 
                  width = settings.root_x, 
                  height = settings.status_bar_height )

view_frame = tk.Frame( view_container_frame,
                       width = settings.view_container_frame_width - 20,
                       height = settings.view_container_frame_height - 20, 
                       background = 'black' )
view_frame.place( x = 10, y = 10 )

algorithm_frame = tk.Frame( options_frame, 
                            width = settings.options_frame_width  - 20, 
                            height = 50 )

speed_frame = tk.Frame( options_frame, 
                        width = settings.options_frame_width - 20, 
                        height = 100 )

speed_label = tk.Label( speed_frame, text = "Speed:" )
speed_label.place( x = 10, y = 10 )

generator_frame = tk.Frame( options_frame, 
                            width = settings.options_frame_width - 20, 
                            height = 200,
                            padx = 10, pady = 10 )
generator_frame.place( in_ = speed_frame, 
                       relx = 0.0, x = 0, 
                       rely = 1.0, y = 10 )

mimimum_value_label = tk.Label( generator_frame, text = 'Minimum value:' )
mimimum_value_label.pack()

mimimum_value_slide = tk.Scale( generator_frame, from_= 0, to = 200, orient= tk.HORIZONTAL )
mimimum_value_slide.pack()

maximum_value_label = tk.Label( generator_frame, text = 'Maximum value:' )
maximum_value_label.pack()

maximum_value_slide = tk.Scale( generator_frame, from_= 0, to = 200, orient= tk.HORIZONTAL )
maximum_value_slide.pack()

number_of_elements_label = tk.Label( generator_frame, text = 'Number of elements:' )
number_of_elements_label.pack()

number_of_elements_slide = tk.Scale( generator_frame, from_= 0, to = 200, orient= tk.HORIZONTAL )
number_of_elements_slide.pack()

data = []

options = [ 
        'Bars', 
        'Squares'
] 

algorithm_options = [ 
    'Quicksort', 
    'Bubblesort',
    'Insertionsort',
    'Selectionsort',
    'Cocktailsort',
    'Bucketsort'
]

# datatype of menu text 
clicked = tk.StringVar() 
  
# initial menu text 
clicked.set( 'Squares' ) 

bars_canvas = tk.Canvas( view_frame,
                         width = settings.view_canvas_width, 
                         height = settings.view_canvas_height )
squares_canvas = tk.Canvas( view_frame, bd = -2,
                            width = settings.view_canvas_width, 
                            height = settings.view_canvas_height )

view_canvas = squares_canvas

view_canvas.place( x = ( settings.view_container_frame_width - 20 ) / 2,
                   y = ( settings.view_container_frame_height - 20 ) / 2,
                   anchor = 'center' )

def choose_view(view):
    global view_canvas
    print( view )
    view_canvas.place_forget()
    if ( view == 'Bars' ):
        view_canvas = bars_canvas
    else:
        view_canvas = squares_canvas
    view_canvas.place( x = ( root.winfo_width() - root.winfo_width() / 3 - 20 ) / 2,
                       y = ( root.winfo_height() - settings.status_bar_height - 20 ) / 2,
                       anchor = 'center' )

view = tk.OptionMenu( view_frame , clicked , *options, command = choose_view ) 
view.place( x = settings.view_container_frame_width - 30, y = 10, anchor = 'ne' )

gen = None
     

algorithm_label = tk.Label( algorithm_frame, text = 'Algorithm:' )
algorithm_label.place( x = 10, y = 10 )

selected_algorithm = tk.StringVar()
selected_algorithm.set( 'Quicksort' )
algorithm = tk.OptionMenu( algorithm_frame, 
                           selected_algorithm, 
                           *algorithm_options )
algorithm.place( x = settings.options_frame_width - 30, y = 10, anchor = 'ne' )
algorithm_frame.place( x = 10, y = 10 )

def handle_square_sort():
    global gen
    print( selected_algorithm.get() )
    speed = speed_slider.get()
    match selected_algorithm.get():
        case 'Bubblesort':
            gen = bubblesortcommands.sort_squares( squares_canvas, data, speed )
        case 'Cocktailsort':
            gen = cocktailsortcommands.sort_squares( squares_canvas, data, speed )
        case 'Selectionsort':
            gen = selectionsortcommands.sort_squares( squares_canvas, data, speed )
        case 'Insertionsort':
            gen = insertionsortcommands.sort_squares( squares_canvas, data, speed )
        case _: 
            pass

sort_button = tk.Button( view_frame, text = 'Sort', command = handle_square_sort )
sort_button.place( x = 10, y = settings.status_bar_y_offset - 30, anchor = 'sw' )

speed_frame.place( in_ = algorithm_frame, rely = 1.0, y = 10 , relx = 0.0, x = 0 )

speed_slider = tk.Scale( speed_frame, from_= 0, to = 200, orient= tk.HORIZONTAL )
speed_slider.place( x = settings.options_frame_width - 30, 
                    y = 10, 
                    anchor = 'ne' )

def draw_squares():
    match selected_algorithm.get():
        case 'Bubblesort':
            drawbubblesort.draw_squares( squares_canvas, data )
            drawbubblesort.draw_bars( bars_canvas, data )
        case 'Cocktailsort':
            drawcocktailsort.draw_squares( data, squares_canvas )
        case 'Selectionsort':
            drawselectionsort.draw_squares( squares_canvas, data )
        case 'Insertionsort':
            drawinsertionsort.draw_squares( squares_canvas, data )
        case _:
            pass

partially_sorted = tk.IntVar()
partially_sorted_checkbox = tk.Checkbutton( generator_frame, 
                                            text = 'Partiallly sorted', 
                                            variable = partially_sorted )
partially_sorted_checkbox.pack()

def partially_sort():
    pass

def generate():
    global data
    squares_canvas.delete('all') 
    data = []
    number_of_elements = number_of_elements_slide.get()
    minimum_value = mimimum_value_slide.get()
    maximum_value = maximum_value_slide.get()
    if minimum_value > maximum_value:
        messagebox.showerror('Error', 
                             'Minimum value is greater than maximum value.')
    for _ in range( number_of_elements ):
        data.append( random.randint( minimum_value, maximum_value ) )
    if partially_sorted.get() == 1:
        partially_sort()
    draw_squares()

generate_button = tk.Button( generator_frame, text = "Generate", command = generate )
generate_button.pack( pady = (5, 0) )

root.state( 'zoomed' )

def draw():
    options_frame.place( width = root.winfo_width() / 3, 
                         height = root.winfo_height() - settings.status_bar_height )
    
    view_container_frame.place( x = root.winfo_width() / 3, 
                                width = root.winfo_width() - root.winfo_width() / 3,
                                height = root.winfo_height() - settings.status_bar_height )
    
    status_bar.place( y = root.winfo_height() - settings.status_bar_height, relwidth = 1 )
    
    view_frame.place( width = root.winfo_width() - root.winfo_width() / 3 - 20,
                      height = root.winfo_height() - settings.status_bar_height - 20  )
    view.place( x = root.winfo_width() - ( root.winfo_width() / 3) - 30, y = 10, anchor = 'ne' )
    
    sort_button.place( x = 10, y = root.winfo_height() - settings.status_bar_height - 30, anchor = 'sw' )

    view_canvas.place( x = ( root.winfo_width() - root.winfo_width() / 3  - 20 ) / 2,
                       y = ( root.winfo_height() - settings.status_bar_height - 20 ) / 2,
                       anchor = 'center' )

draw()

last_window_width = this_window_width = root.winfo_width()
last_window_height = this_window_height = root.winfo_height()

while True:

    if last_window_width != this_window_width or last_window_height != this_window_height:
        draw()

    last_window_width = this_window_width
    last_window_height = this_window_height

    this_window_width = root.winfo_width()
    this_window_height = root.winfo_height()

    if gen != None:
        for i in gen:
            root.update()
            gen = None
    else: 
        root.update()





