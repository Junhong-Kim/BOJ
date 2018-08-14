notes = input().split()

start_sequence = None
current_sequence = None
for index, note in enumerate(notes):
    try:
        if start_sequence is None:
            if note < notes[index + 1]:
                start_sequence = 'ascending'
                current_sequence = 'ascending'
            elif note > notes[index + 1]:
                start_sequence = 'descending'
                current_sequence = 'descending'
        else:
            if start_sequence != current_sequence:
                print('mixed')
                break
            else:
                if note < notes[index + 1]:
                    current_sequence = 'ascending'
                elif note > notes[index + 1]:
                    current_sequence = 'descending'
    except IndexError:
        print(current_sequence)
