from pynput.keyboard import Key, Listener

keys = [] # contains all the keys that were pressed

def write_file(keys):
    f = open("log.txt", "w")
    # for key in keys:
    #     f.write(key)
    f.write("ok")
    f.close()

def on_press(key):
    global keys
    keys.append(key)
    print(key)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release ) as listener:
    listener.join()
    print(keys)