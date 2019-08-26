from voice_control.core import Control, VoiceCommand


class WeChat(Control):
    """微信
    """
    pass


if __name__ == '__main__':
    WeChat.execute(VoiceCommand.GO_HOMO)
