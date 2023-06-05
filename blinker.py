from tkinter import*
import tkinter.font
from gpiozero import LED 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

led_green = LED(4)
led_red = LED(14)
led_yellow =LED(15)

gridsq = Tk()
gridsq.title("***SCINTILLATE LED***")
gridsq.geometry("450x350")
Font = tkinter.font.Font(family= "Cambria", size = 12, weight = "bold")
window = Frame(gridsq)
window.pack()

def greenToggle():
    if led_green.is_lit:
        led_green.off()
        greenButton["text"] = "Turn GREEN LED ON"
    else:       
        led_red.off()
        led_yellow.off()
        led_green.on()
        greenButton["text"] = "Turn GREEN LED OFF"
        
def redToggle():
    if led_red.is_lit:
        led_red.off()
        redButton["text"] = "Turn RED LED ON"

    else:
        led_yellow.off()
        led_green.off()
        led_red.on()
        redButton["text"] = "Turn RED LED OFF"
    
def yellowToggle():
    if led_yellow.is_lit:
        led_yellow.off()
        yellowButton["text"] = "Turn YELLOW LED ON"

    else:
        led_green.off()
        led_red.off()
        led_yellow.on()
        yellowButton["text"] = "Turn YELLOW LED OFF"
        
def exit():
    RPi.GPIO.cleanup()
    window.destroy()
    
greenButton = Button(window, text = 'Turn GREEN LED ON', command = greenToggle, bg = 'green', height = 2, width = 25)
greenButton.grid(row = 1, column = 1)

redButton = Button(window, text = 'Turn RED LED ON', command = redToggle, bg = 'red', height = 2, width = 25)
redButton.grid(row = 2, column = 1)

yellowButton = Button(window, text = 'Turn YELLOW LED ON', command = yellowToggle, bg = 'yellow', height = 2, width = 25)
yellowButton.grid(row = 3, column = 1)

exit_button = Button(window, text= "EXIT", command = exit, bg = 'white', height = 2, width= 25)
exit_button.grid(row = 4, column = 1)


window.mainloop()



