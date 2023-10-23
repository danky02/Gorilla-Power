from abc import ABC, abstractmethod
import keyboard
import pyperclip
import pyautogui

class GorillaPluginError(Exception):
    pass

class GorillaPlugin:
    name:str = "Gorilla Parser"
    custom_options:dict = {}

    # PARSER OPTIONS
    suppress:bool = False
    copy_enable:bool = False
    paste_enable:bool = False

    __hotkey__:str=None
    __is_active__:bool=False
    
    @abstractmethod
    def parser(self, text:str) -> str:
        raise Exception("method not implemented")

    def error(self, text:str) -> str:
        raise GorillaPluginError(text)
    
    def run(self):
        prev_clipboard = pyperclip.paste()
        try:
            selected_text:str = None
            # copy
            if self.copy_enable:
                pyautogui.hotkey('ctrl', 'c')
                selected_text = pyperclip.paste()

            # parse
            parser_result = self.parser(selected_text)

            # paste
            if self.paste_enable:
                pyperclip.copy(parser_result),
                pyautogui.hotkey('ctrl', 'v')

            # optionally select code
                if (wrote_chars := len(parser_result)) <= 50:
                    with pyautogui.hold('shift'):
                        pyautogui.press('left', presses=wrote_chars)
            
        except GorillaPluginError as exc:
            print(f"Gorilla is angry: {exc.with_traceback()}")
        finally:
            pyperclip.copy(prev_clipboard)
    
    def activate(self):
        assert self.__hotkey__, "Invalid Plugin Hotkey"
        self.__is_active__ = True
        keyboard.add_hotkey(
            self.__hotkey__,
            self.run,
            suppress=self.suppress
        )

    def deactivate(self):
        self.__is_active__ = False
        keyboard.remove_hotkey(self.run)
    
    def reload(self):
        self.deactivate()
        self.activate()

    def set_hotkey(self, new_hotkey):
        self.__hotkey__ = new_hotkey

