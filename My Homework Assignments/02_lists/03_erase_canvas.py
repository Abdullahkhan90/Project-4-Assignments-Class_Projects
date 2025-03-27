from graphics import Canvas  
import time  


CANVAS_WIDTH : int = 400
CANVAS_HEIGHT : int = 400

CELL_SIZE : int = 40  
ERASER_SIZE : int = 20  

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:  
            canvas.set_color(overlapping_object, 'white')

def main():
    # Create the canvas object with specified dimensions
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Calculate number of rows and columns based on the canvas size and cell size
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    # Draw the grid of blue cells
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE  # Calculate the left edge of the cell
            top_y = row * CELL_SIZE  # Calculate the top edge of the cell
            right_x = left_x + CELL_SIZE  # Calculate the right edge of the cell
            bottom_y = top_y + CELL_SIZE  # Calculate the bottom edge of the cell
            
            # Create a blue rectangle for the cell
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
    
    # Wait for a click to start the eraser
    canvas.wait_for_click()
    
    # Get the starting position for the eraser based on the user's click
    last_click_x, last_click_y = canvas.get_last_click()
    
    # Create the eraser at the initial click position
    eraser = canvas.create_rectangle(
        last_click_x, 
        last_click_y, 
        last_click_x + ERASER_SIZE, 
        last_click_y + ERASER_SIZE, 
        'pink'
    )
    
    # Move the eraser with the mouse and erase objects as it moves
    while True:
        # Get current mouse position and move the eraser
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        
        # Call the function to erase objects in contact with the eraser
        erase_objects(canvas, eraser) 
        
        # Slow down the loop to make the eraser's movement visible
        time.sleep(0.05)

if __name__ == '__main__':
    main()  # Run the main function when the script is executed
