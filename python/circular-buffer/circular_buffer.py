import collections


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.d = collections.deque(maxlen=capacity)

    def read(self):
        try:
            return self.d.popleft()
        except IndexError:
            raise BufferEmptyException("Can't read an empty buffer.")

    def write(self, data):
        if len(self.d) == self.d.maxlen:
            raise BufferFullException("Can't write to a full buffer.")
        else:
            self.d.append(data)

    def overwrite(self, data):
        self.d.append(data)

    def clear(self):
        self.d.clear()
