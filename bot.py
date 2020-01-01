import time, datetime
import telepot
from telepot.loop import MessageLoop

now = datetime.datetime.now()

#def action(msg):
#    chat_id = msg['chat']['id']
#    command = msg['text']
#
#    print 'Received: %s' % command
#
#    if command == '/hi':
#        GrassMudHorse_bot .sendMessage(chat_id, str("Hi! CircuitDigest"))
#    elif command == '/time':
#        GrassMudHorse_bot .sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
#    elif command == '/logo':
#        GrassMudHorse_bot .sendPhoto(chat_id,open('/home/pi/jpeg'))
#        print(chat_id)

#GrassMudHorse_bot .sendPhoto(chat_id,open('/home/pi/test.jpeg'))

GrassMudHorse_bot = telepot.Bot('1063039918:AAHk3tXH1O81DZeNM0AYf2BRkswgE1k8g-c')

GrassMudHorse_bot .sendPhoto(791392583,open('/home/pi/autophoto/merge.png'))
GrassMudHorse_bot .sendPhoto(148504986,open('/home/pi/autophoto/merge.png'))
#GrassMudHorse_bot .sendPhoto(201165083,open('/home/pi/autophoto/merge.png'))

exit()
#print(GrassMudHorse_bot.getMe())

#MessageLoop(GrassMudHorse_bot, action).run_as_thread()
#print 'Up and Running....'

#while 1:
#    time.sleep(10)
