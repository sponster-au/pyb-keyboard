""" keyboard main state machine.

"""

STATE_IDLE = 0
STATE_KEY_DOWN = 1
STATE_KEY_PRESS = 2
STATE_KEY_UP = 3


def main():
    state = STATE_IDLE
    keymask = get_keymask()
    keymask = get_keymask()
    while True:
        state_ = state  # to ensure that state_ doesn't change while processing
        if state_ == STATE_IDLE:
            if keymask != 0:
                timer_start(KEY_DOWN_TIME, lambda: state=STATE_KEY_PRESS)
                state = STATE_KEY_DOWN
        if state_ == STATE_KEY_DOWN:
            new_keymask = get_keymask()
            if new_keymask != keymask:
                timer_start(KEY_DOWN_TIME, lambda: state=STATE_KEY_PRESS)
                keymask = new_keymask
        if state_ == STATE_KEY_PRESS:
            send_keyboard(keymask)
            state = STATE_KEY_UP
        if state_ == STATE_KEY_UP:
            keymask = get_keymask
            if keymask == 0:
                timer_start(DEBOUNCE_TIME, lambda: state=STATE_IDLE)
            else:
                timer_stop()
