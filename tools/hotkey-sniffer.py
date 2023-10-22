import keyboard

if __name__ == "__main__":
    print("press a hotkey")
    res = keyboard.read_hotkey()
    print(f"recorded: {res}")
    exit()