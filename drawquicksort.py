import settings
import drawing

squares = []
values = []

def draw_squares(squares_canvas, data):
    for index, data_point in enumerate(data):      
        square, value = drawing.draw_square( squares_canvas,
                                             index, 
                                             data_point,
                                             settings.unsorted_partition_color )
        squares.append( square )
        values.append( value )

def swap_squares(squares_canvas, lhs_index, rhs_index):
    drawing.swap_elements( squares_canvas, 
                           squares, 
                           lhs_index, 
                           rhs_index, 
                           settings.square_span,
                           dimensions = 2 )
    drawing.swap_elements( squares_canvas,
                           values,
                           lhs_index,
                           rhs_index,
                           settings.square_span,
                           dimensions = 2 )

def select_sorted_squares(squares_canvas, index):
    squares_canvas.itemconfig( squares[ index ], fill = settings.sorted_partition_color )

def select_square(squares_canvas, index):
    squares_canvas.itemconfig( squares[ index ], 
                               fill = settings.text_color )
    squares_canvas.itemconfig( values[ index ], 
                               fill = settings.selected_color )
              
def remove_bubble(squares_canvas, temp):
    select_sorted_squares( squares_canvas, temp )
    select_sorted_squares( squares_canvas, temp - 1 )

def reset():
    global squares
    global values
    squares = []
    values = []
