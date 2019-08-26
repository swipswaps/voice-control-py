import os


class Voice:
    """
    关于手势: https://www.jianshu.com/p/b887af45d5de
    """
    # 基础导航
    GO_HOMO = 'Go Home'
    GO_BACK = 'Go Back'

    # 叠层
    SHOW_NUMBERS = 'Show numbers'
    SHOW_NAMES = 'Show names'
    SHOW_GRID = 'Show grid'

    # 基本手势
    SCROLL_DOWN = 'Scroll down'
    SCROLL_UP = 'Scroll up'
    SCROLL_TO_BOTTOM = 'Scroll to bottom'
    SCROLL_TO_TOP = 'Scroll to top'
    SCROLL_LEFT = 'Scroll left'
    SCROLL_RIGHT = 'Scroll right'
    SCROLL_TO_LEFT_EDGE = 'Scroll to left edge'
    SCROLL_TO_RIGHT_EDGE = 'Scroll to right edge'

    ZOOM_IN = 'Zoom in'
    ZOOM_OUT = 'Zoom out'

    SINGLE_TAP = 'Single tap'
    DOUBLE_TAP = 'Double tap'

    LONG_PRESS = 'Long press'

    TWO_FINGER_TAP = 'Two finger tap'

    @classmethod
    def tap(cls, item_name) -> str:
        return f'Tap {item_name}'

    @classmethod
    def repeat_times(cls, count) -> str:
        return f'Repeat {count} times'

    @classmethod
    def long_press(cls, item_name) -> str:
        return f'Long press {item_name}'


class Control:
    @classmethod
    def execute(cls, voice_command):
        os.system(f'say {voice_command}')


if __name__ == "__main__":
    Control.execute(Voice.tap('hello'))
    Control.execute(Voice.SCROLL_DOWN)

