from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f'Clicked at (X: {x}, Y: {y})')

# Set up the listener
with mouse.Listener(on_click=on_click) as listener:
    print("Listener started. Click anywhere to get the coordinates. Press Ctrl+C to stop.")
    listener.join()
