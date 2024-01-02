from uuid import uuid4
from datetime import datetime
from typing import Dict
from models import storage

def loadInstance(self):

    self.id = uuid4()
    self.created_at = datetime.now()
    self.updated_at = self.created_at
    storage.new(self)


def loadKwargs(self, kwargs: Dict[str, str]):

    format_time = "%Y-%m-%dT%H:%M:%S.%f"

    dates = ("created_at", "updated_at")

    for date in dates:
        value = kwargs[date]
        setattr(self, date, datetime.strptime(value, format_time))

    for key, value in kwargs.items():
        if key in ("__class__", *dates):
            continue
        setattr(self, key, value)


class BaseModel:

    def __init__(self, *args, **kwargs):
        if bool(kwargs):
            loadKwargs(self, kwargs)
        if not bool(kwargs):
            loadInstance(self)

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self) -> Dict[str, str]:
        dict_obj = dict(self.__dict__)
        dict_obj["__class__"] = type(self).__name__
        dict_obj["created_at"] = dict_obj["created_at"].isoformat()
        dict_obj["updated_at"] = dict_obj["updated_at"].isoformat()
        return dict_obj
