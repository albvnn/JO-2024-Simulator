class Game:
    def __init__(self):
        pass  # Constructor, does nothing in this implementation

    def update(self):
        raise NotImplementedError()  # Method to update game state, to be implemented by subclasses

    def draw(self):
        raise NotImplementedError()  # Method to draw game elements, to be implemented by subclasses

    def onKeyDown(self, key):
        raise NotImplementedError()  # Method called when a key is pressed, to be implemented by subclasses

    def onKeyUp(self, key):
        raise NotImplementedError()  # Method called when a key is released, to be implemented by subclasses

    def onMouseDown(self, event):
        raise NotImplementedError()  # Method called when a mouse button is pressed, to be implemented by subclasses

    def onMouseUp(self, event):
        raise NotImplementedError()  # Method called when a mouse button is released, to be implemented by subclasses

    def onMouseWheel(self, event):
        pass  # Method called when the mouse wheel is scrolled, does nothing by default
