# "Stopwatch: The Game"

import simplegui

# define global variables
counter = 0
stop_counter = 0
hit_counter = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    time_string = ""
    D = str(t % 10)
    C = str(t / 10 % 10)
    B = str(t / 100 % 6)
    A = str (t / 600)
    if t == 6000:
        t = 0
        print "This stopwatch works up to one hour only!!!"
    time_string = A + ":" + B + C + "." + D
    return time_string
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running = True

def stop():
    global stop_counter
    global hit_counter
    global counter
    global running
    timer.stop()
    if running == True:
        stop_counter += 1
        if counter % 10 == 0:
            hit_counter += 1
    running = False

def reset():
    global counter
    global running
    global stop_counter
    global hit_counter
    running = False
    timer.stop()
    counter = 0
    stop_counter = 0
    hit_counter = 0

# define event handler for timer with 0.1 sec interval
def count_time():
    global counter
    counter += 1
    
# define draw handler
def draw_time(canvas):
    global counter
    global stop_counter
    global hit_counter
    stop_hit = str(hit_counter) + "/" + str(stop_counter)
    canvas.draw_text(format(counter), (60, 90), 34, 'White')
    canvas.draw_text(stop_hit, (140,23), 26, "Green")

# create frame
frame = simplegui.create_frame("Stopwatch Game", 200, 150)

# register event handlers
start_button = frame.add_button("Start", start, 100)
stop_button = frame.add_button("Stop", stop, 100)
reset_button = frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100, count_time)
frame.set_draw_handler(draw_time)

# start frame
frame.start()



