from scale_list import scale_list
import random
from note import Note
from progression_list import common_major_progression, common_minor_progression


def generate_sequence(note, scale):
    note_name = note

    # for i in range(len(scale_list)):
    #     print(f'{i}:{scale_list[i].name[0]}')
    scale_index = scale
    print(f"Scale : {note_name} {scale_list[scale_index].name[0]}")
    index = -1
    total_notes = len(Note)
    notes_in_scale = []
    chord_seq = []
    progression = list
    for note in Note:
        if note_name == note.name:
            index = note.value[0]
            # print(f"Index of {note.name} in {note.value[0]}")
            break
    if index != -1:
        for scale in scale_list[scale_index].pattern[0]:
            # print(type(scale))
            offset = index + scale
            # print(f"index = {index}, scale = {scale}, offset = {offset}")
            if offset >= total_notes:
                offset -= total_notes
                # print(f"new offset = {offset}")
            my_note = list(Note)[offset].name
            notes_in_scale.append(my_note)
        print(f"Notes in scale {notes_in_scale}")

        if scale_index == 0:
            progression = common_major_progression
        elif scale_index == 1:
            progression = common_minor_progression

        for chord in random.choice(progression):
            n = notes_in_scale[chord.index]
            t = chord.type.name
            current_chord = f'{n}{t}'
            chord_seq.append(f"{current_chord}")

        print(f"Created Sequence {chord_seq}")
    else:
        print("Note not Found")


def generate_random_seq():
    note = random.choice(list(Note)).name
    scale_index = random.randint(0, len(scale_list)-1)
    print(f"Scale : {note} {scale_list[scale_index].name[0]}")
    generate_sequence(note=note, scale=scale_index)
