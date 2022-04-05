class Song:
    __slots__ = 'events'

    def __init__(self, events):
        self.events = events

    def get_events(self):
        return self.events
