import json
import keyboard
import time
import pyautogui
import pyperclip

def hotkey_cb():
    # save clipboard
    prev_clipboard = pyperclip.paste()

    # copy
    pyautogui.hotkey('ctrl', 'c')
    code_block = pyperclip.paste()

    # execute
    res_block = code_block
    
    # paste
    pyperclip.copy(res_block)
    pyautogui.hotkey('ctrl', 'v')
    
    # restore clipboard
    pyperclip.copy(prev_clipboard)

if __name__ == "__main__":
    print("Starting Gorilla")

    # load key-bindings
    try:
        # TODO:
        # with open("key-bindings.json", mode="r") as file:
        #     data = json.loads(file.read())

        keyboard.add_hotkey(hotkey="ctrl+f2", callback=hotkey_cb)

        while True:
            time.sleep(1)
    except Exception as e:
        raise e
        print("Gorilla is looking for his bananas, but he has found nothing good at the moment")

    