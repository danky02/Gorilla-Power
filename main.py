import json
import time
import os
import importlib
from gorilla import GorillaPlugin
from contextlib import contextmanager

@contextmanager
def import_plugin(main_folder, plugin_name):
    module_name = f"{main_folder}.{plugin_name}.main"
    try:
        imported_module = importlib.import_module(module_name)
        plugin_constructor = imported_module.Plugin
        if issubclass(plugin_constructor, GorillaPlugin):
            yield plugin_constructor
    except ModuleNotFoundError:
        yield None




if __name__ == "__main__":
    print("Starting Gorilla")

    # load key-bindings
    try:
        # TODO:
        
        plugins:list[GorillaPlugin] = []

        data:dict
        with open("config.json", mode="r") as f:
            data = json.loads(f.read())
        
        # import core plugins
        for pl_name, config in data['core'].items():
            with import_plugin("core", pl_name) as constructor:
                if constructor:
                    instance = constructor(config.get('hotkey', None))
                    if config.get('active', False) == True:
                        instance.activate()

                    plugins.append(instance)

        # import external plugins
        for pl_name, config in data['plugins'].items():
            with import_plugin("plugins", pl_name) as constructor:
                if constructor:
                    instance = constructor(config.get('hotkey', None))
                    if config.get('active', False) == True:
                        instance.activate()

                    plugins.append(instance)
            
        print(f"successfully installed {len(plugins)} core plugin{'s' if len(plugins) != 1 else ''}: { ', '.join([x.name for x in plugins])}")
        
        print("Running Gorilla")
        
        while True:
            time.sleep(10)

    except KeyboardInterrupt:
        for p in plugins:
            p.deactivate()
        
        print("Gorilla Stopped, bye")
        exit()
    except Exception as exc:
        with open("error.txt", mode="w+") as e:
            e.write(str(exc))
        print("Gorilla is looking for his bananas, but he has found nothing good at the moment")

    