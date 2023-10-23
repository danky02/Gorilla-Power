import json
import keyboard
import time
import pyautogui
import pyperclip
from contextlib import contextmanager
import os
import importlib
from gorilla import GorillaPlugin

        
        
def import_module_from_subfolder(subfolder_name):
    module_name = f"plugins.{subfolder_name}.main"
    try:
        imported_module = importlib.import_module(module_name)
        return imported_module
    except ModuleNotFoundError:
        return None
    
def get_entry_point_function(module):
    if module:
        plugin:GorillaPlugin = module.Plugin
        if issubclass(plugin, GorillaPlugin):
            return plugin
    return None




if __name__ == "__main__":
    print("Starting Gorilla")

    # load key-bindings
    try:
        # TODO:
        
        plugins:list[GorillaPlugin] = []

        for name in os.listdir("plugins"):
            module = import_module_from_subfolder(name)
            plugin = get_entry_point_function(module)
            if plugin:
                instance = plugin()
                plugins.append(instance)
                instance.set_hotkey('f5')
                instance.activate()
        
        while True:
            time.sleep(1)
    except Exception as e:
        raise e
        print("Gorilla is looking for his bananas, but he has found nothing good at the moment")

    