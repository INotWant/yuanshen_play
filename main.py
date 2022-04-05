import time

from pretty_midi import pretty_midi
from pynput.keyboard import Controller

from model.event import Event
from util.convert import obtain_key, obtain_key_with_falling_tone


def process():
    events = []

    midi_fn = 'data/知足-五月天.midi'
    # midi_fn = 'data/让风告诉你.midi'
    # midi_fn = 'data/lemon.midi'

    midi_data = pretty_midi.PrettyMIDI(midi_fn)
    notes = midi_data.instruments[0].notes
    for item in notes:
        start = item.start
        pitch = item.pitch
        if pitch > 95 or pitch < 48:
            continue
        events.append(Event(pitch, start))

    keyboard = Controller()

    cur_time = 0
    for event in events:
        trigger_time = event.get_trigger_time()
        if trigger_time - cur_time > 0.001:
            time.sleep(trigger_time - cur_time)
            cur_time = trigger_time

        note_name = event.get_note_name()

        # key = obtain_key(note_name)
        key = obtain_key_with_falling_tone(note_name)
        print('key: %s, cur_time: %.3f' % (key, cur_time))

        keyboard.press(key)
        keyboard.release(key)

    print('total_time: %s' % cur_time)


if __name__ == '__main__':
    process()
