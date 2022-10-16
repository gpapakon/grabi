import pyautogui
import keyboard


while True:
  if keyboard.is_pressed('f1'):
    keyboard.press_and_release('ctrl+tab')
    pyautogui.write('giorgos.papakonstantinou1999@gmail.com')
    pyautogui.hotkey('tab')
    pyautogui.write('Weww1211!@!!')
    pyautogui.hotkey('enter')
    break