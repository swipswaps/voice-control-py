import os


class Voice:
    GO_HOMO = 'Go Home'
    GO_BACK = 'Go Back'
    SCROLL_DOWN = 'Scroll down'
    
    @classmethod
    def tap(cls, item_name):
        return f'Tap {item_name}'



class Control:
    def execute(self, voice_command):
        os.system(f'say {voice_command}');


if __name__ == "__main__":
    c = Control()
    c.execute(Voice.tap('abc'))
    c.execute(Voice.SCROLL_DOWN)

