class Audio:
    def __init__(self, controls):
        self.controls = controls

    def actions(self):
        print("Playing Audio...")
        if self.controls == 1:
            return "Audio Paused"
        else:
            return "Audio Stopped"


class Video:
    def __init__(self, controls):
        self.controls = controls

    def actions(self):
        print("Playing Video...")
        if self.controls == 1:
            return "Video Paused"
        else:
            return "Video Stopped"


class RadioStream:
    def __init__(self, controls):
        self.controls = controls

    def actions(self):
        print("Tuning Radio Station...")
        if self.controls == 1:
            return "Radio Paused"
        else:
            return "Radio Stopped"


def media_output(output):
    print(output.actions())    


media_type = int(input("Enter \n1. Audio \n2. Video \n3. Radio \n: "))

operation = int(input("Enter \n1. Pause \n2. Stop\n: "))

if media_type == 1:
    obj = Audio(operation)

elif media_type == 2:
    obj = Video(operation)

elif media_type == 3:
    obj = RadioStream(operation)

else:
    print("Invalid choice")
    exit()

media_output(obj)

    
    
class Demo:
    def add(self,*args):
        total=0
        for i in args:
            total+=i
        return total

d=Demo()
print(d.add(2,3))
print(d.add(3,4,5,6))

