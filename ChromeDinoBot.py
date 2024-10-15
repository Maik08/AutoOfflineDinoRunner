import pyautogui
import time
import keyboard
import threading

latest_screenshot = None

def jumping():
    pyautogui.press('space')
    time.sleep(0.01)

def screenshot_thread():
    global latest_screenshot
    while True:
        latest_screenshot = pyautogui.screenshot()
        time.sleep(0.01)  

def get_pixel_colors():
    global latest_screenshot
    if latest_screenshot is None:
        return (0, 0, 0), []  

    dino_pixel = latest_screenshot.getpixel((999, 288))  

   
    cactus_pixels = [
        latest_screenshot.getpixel((1110, 286)), 
        latest_screenshot.getpixel((1117, 280)), 
        latest_screenshot.getpixel((1115, 280)), 
        latest_screenshot.getpixel((1117, 285)),
        latest_screenshot.getpixel((1112, 283)), 
        latest_screenshot.getpixel((1114, 280)), 
        latest_screenshot.getpixel((1115, 280)), 
        latest_screenshot.getpixel((1113, 280))
    ]
    
    return dino_pixel, cactus_pixels


threading.Thread(target=screenshot_thread, daemon=True).start()

while True:
    dino_pixel, cactus_pixels = get_pixel_colors()
    
    
    if latest_screenshot is not None and latest_screenshot.getpixel((1272, 254)) == (8, 8, 8):
        pyautogui.press('space') 
        time.sleep(1)  

    background = (32, 33, 36)
    
    
    if dino_pixel[0] == 255:  
        if any(pixel == (172, 172, 172) for pixel in cactus_pixels):    
            jumping()
    else:  
        if any(pixel == (172, 172, 172) for pixel in cactus_pixels):
            jumping()     

    
    if keyboard.is_pressed('s'):
        break
    
    time.sleep(0.0001)  
