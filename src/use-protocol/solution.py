# Use Protocol
from typing import Protocol, Any


class RESTProtocol(Protocol):
    def get(self, url : str, **kwargs : Any):
        ...
    def post(self, url : str, data: {}, **kwargs : Any) -> Any:
        ...
    def put(self, url : str, data: {}, **kwargs : Any) -> Any:
        ...
    def delete(self, url : str, data: {}, **kwargs : Any) -> Any:
        ...

class DummyREST:
    def get(self, url : str, **kwargs : Any):
        print("Getting")
    def post(self, url : str, data: {}, **kwargs : Any) -> Any:
        print("Posting")
    def put(self, url : str, data: {}, **kwargs : Any) -> Any:
        print("Putting")
    def delete(self, url : str, data: {}, **kwargs : Any) -> Any:
        print("Deleting")

x : RESTProtocol = DummyREST()
x.get("https://www.cnn.com")
x.post("https://www.cnn.com", {})
x.put("https://www.cnn.com", {})
x.delete("https://www.cnn.com", {})