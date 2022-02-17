class SingleLinkedList(object):

    def _init_(self):
        """Init "SingleLinkedList"""
        self.begin = None
        self.end = None
        
    def push(self, obj):
        """Appends a new value on the end of the list."""
        if self.count() == 0:
            self.begin=obj
        self.end = obj
        
    def pop(self):
        """Removes the last item and returns it."""
        
    def shift(self, obj):
        """Another name for push."""
        
    def unshift(self):
        """Removes the first item and returns it."""
        
    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        
    def first(self):
        """Returns a *reference* to the first item, and does not remove."""
        
    def last(self):
        """Returns a reference to the last item, and does not remove."""

    def count(self):
        """Counts the number of items in the list."""
        return len(self)

    def get(self, index):
        """Get the value at index."""

    def dump(self, mark):
        """Debugging function that dumps the contents of a list."""