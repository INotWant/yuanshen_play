from util.convert import obtain_note_name


class Event:
    __slots__ = ('note', 'trigger_time')

    def __init__(self, note, trigger_time):
        self.note = note
        self.trigger_time = trigger_time

    def get_note(self):
        return self.note

    def get_trigger_time(self):
        return self.trigger_time

    def get_note_name(self):
        return obtain_note_name(self.note)

    def __str__(self):
        return '(note: ' + self.get_note_name() + ', trigger_time: ' + ('%.3f' % self.trigger_time) + ')'
