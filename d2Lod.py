import keyboard # pip install keyboard
import mouse    # pip install mouse

SCRIPT_IS_PAUSED = False

# figure out when right mouse button was clicked (not used in this script lol)
def on_right_click():
    print("Right Mouse was clicked!")


# figure out names of different keys
def print_pressed_keys(e):
    print(f'Key pressed: {e.name}')


# toggleScript is used to toggle the macros on/off using f10
def toggleScript():
    global SCRIPT_IS_PAUSED
    SCRIPT_IS_PAUSED = not SCRIPT_IS_PAUSED

    if SCRIPT_IS_PAUSED:
        print("Macros are now DEACTIVATED.")
    else:
        print("Macros are now ACTIVATED.")

# runMacro takes a key event and runs a macro if it is setup
def runMacro(e):
    # don't run any macros if the script is paused (but allow f10 when it is paused so that it can be unpaused)
    if SCRIPT_IS_PAUSED and e.name != "f10":
        return

    # match is python's switch
    match e.name: # access actual key value from KeyboardEvent by accessing its .name property, add more cases if you have more abilities bound
        case "q" | "w" | "e" | "r" | "t" | "y" | "a" | "s" | "d" | "f": # | means 'or' to handle multiple cases
            mouse.right_click()
        case "f10":
            toggleScript()
        case _: # default
            pass


def main():
    # find out which names the keyboard keys have
    # keyboard.on_press(print_pressed_keys)

    # print sth when right mouse is clicked
    # mouse.on_right_click(on_right_click)

    # ----

    print("Macros are active. Press f12 key to end this program. Press f10 to temporarily enable/disable the script.")

    # listen to keypresses and call function that contains macros
    keyboard.on_press(runMacro)
    
    # kill program when f12 is pressed (must be at END of program)
    keyboard.wait('f12')  
    

main()
# Script assumes that abilties are bound to right-click and to the keys q,w,e,r,...
# Usage: Press f10 to toggle this script on/off, press f12 to terminate this script
# Note: Script should be run as Admin so that it works while full screen application is running. Best way is to use a batch file to run it, create a shortcut to the batch file and then adjust the shortcut settings to run as admin.
# Batch File Example:
#    @echo off
#    python "<fullPathToPythonScript>"