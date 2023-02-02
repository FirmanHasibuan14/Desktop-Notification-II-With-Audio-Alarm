from winotify import Notification, audio
def notify(app_id,title,msg,label,launch):
    notif = Notification(app_id=app_id,
                        title=title,
                        msg=msg,
                        icon="C:\\Users\\ACER\\Downloads\\profile.ico",duration="long")
    notif.add_actions(label=label,
                    launch=launch)
    notif.set_audio(audio.LoopingCall, loop=False)
    notif.show()
app_id = input("Input your notification desktop title: \n")
title = input("Input your notification title: \n")
msg = input("Input your message: \n")
label = input("Input your label: \n")
launch = input("Input your source with url: \n")
notify(app_id,title,msg,label,launch)
