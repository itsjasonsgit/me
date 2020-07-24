import time, sys

indent = 0 # How many spaces to indent
indent_increasing = True # Whether the indentation is increasing or not

try:
    while True: # The main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(1) # Pause for 1/10 of a second

        if indent_increasing:
            # If indent_increasing = True, increase the no. of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indent_increasing = False
        
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indent_increasing = True
    
except KeyboardInterrupt:
    sys.exit()