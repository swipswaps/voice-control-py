from voice_control.core import Control, VoiceCommand


class Douyin(Control):
    """抖音
    """
    pass


if __name__ == '__main__':
    # Douyin.execute(VoiceCommand.SCROLL_TO_BOTTOM)
    # Douyin.execute(VoiceCommand.repeat_times(2))
    Douyin.execute(VoiceCommand.tap('one'))
