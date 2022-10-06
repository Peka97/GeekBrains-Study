class QueueClass:
    def __init__(self):
        self.elems = []

    def push_in(self, el):
        self.elems.insert(0, el)

    def pop_out(self):
        return self.elems.pop()

    def all_out(self):
        self.elems.reverse()
        return self.elems
