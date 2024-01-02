from typing import Dict
from json import dump, load

class FileStorage:

    __file_path: str = "file.json"
    __objects: Dict = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects
        class_name = type(obj).__name__
        self.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self, obj):
        dict_objects = {}
        for key, obj in self.__objects.items():
            dict_objects[key] = obj.to_dict()

        with open(self.__file_path, mode='w') as file:
            dump(dict_objects, file)

    def reload(self):
        
        load_data = {}

        try:
            with open(self.__file_path, mode='r') as file:
                load_data = load(file)
        except FileNotFoundError:
            pass

        for key, kwargs in load_data.items():
            class_name = kwargs["__class__"]
            self.__objects[key] = eval(class_name)(**kwargs)


