# card_public_key=5764801
# door_public_key=17807724
card_public_key=15335876
door_public_key=15086442

def calc_loop_size():
    loops=0
    subject_number=7
    dividend=20201227
    value=1
    def transform_value():
        nonlocal value, subject_number, dividend
        value*=subject_number
        value = value % dividend
        return value
    return transform_value

def find_loop_size(public_key):
    find_card_loop = calc_loop_size()
    card_val = 0
    card_counter = 0
    while card_val != public_key:
        card_counter+=1
        card_val = find_card_loop()
    return card_counter

def decrypt_key(public_key, loop_size):
    subject_number=public_key
    dividend=20201227
    value = 1
    for i in range(loop_size):
        value*=subject_number
        value = value % dividend
    return value


door_loop_size = find_loop_size(door_public_key)
encryption_key = decrypt_key(card_public_key, door_loop_size)

print(encryption_key)
