# we define an abstract base class Handler with a method handle_request. All concrete handlers will implement this method.
from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass

# We create two concrete handlers, ConcreteHandlerA and ConcreteHandlerB, which implements the handle_request method to process or pass requests.
class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == 'A':
            print("Handled by Handler A")
        else:
            print("Passed to the parent handler")
            super().handle_request(request)

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == 'B':
            print("Handled by Handler B")
        else:
            print("Passed to the parent handler")
            super().handle_request(request)

# The Chain class manages a list of handlers and provides a method to add handlers and handle requests in sequence.
            
class Chain:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def handle_request(self, request):
        for handler in self.handlers:
            handler.handle_request(request)

# Client code
            
if __name__ == "__main__":
    chain = Chain()
    chain.add_handler(ConcreteHandlerA())
    chain.add_handler(ConcreteHandlerB())

    requests = ['A', 'B', 'C']

    for request in requests:
        print(f"Processing request: {request}")
        chain.handle_request(request)
        print()