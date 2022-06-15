from inspect import getmembers, isabstract, isclass

from rest_framework.viewsets import ModelViewSet

from . import api

class ApiFactory:
    apis = dict()

    def __init__(self) -> None:
        self.load_apis()

    def load_apis(self) -> None:
        classes = getmembers(api, lambda c: isclass(c) and not isabstract(c))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, ModelViewSet):
                self.apis.update([[name, _type]])

    def return_class(self, api_name: str) -> ModelViewSet:
        if api_name in self.apis:
            return self.apis[api_name]
        else:
            raise ValueError(f'API named "{api_name}" cannot be found.')
