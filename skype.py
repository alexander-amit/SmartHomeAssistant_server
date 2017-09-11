from skpy import Skype


from skpy import SkypeConnection, SkypeLiveAuthProvider
prov = SkypeLiveAuthProvider(SkypeConnection())
bool = prov.checkUser("amit.prag.chanakya@gmail.com")
print(bool)



sk = Skype('amit.prag.chanakya@gmail.com', 'Or@6alexander') # connect to Skype

































sk.user # you
list = sk.contacts # your contacts
sk.chats # your conversations


print(list)
#ch = sk.chats.create(["joe.4", "daisy.5"]) # new group conversation
#ch = sk.contacts["astha.gupta.254"].chat # 1-to-1 conversation

#ch.sendMsg('hello_msg from bot_dsfsdfsdf') # plain-text message
#ch.sendFile(open("song.mp3", "rb"), "song.mp3") # file upload
#ch.sendContact(sk.contacts["daisy.5"]) # contact sharing
print('reached here')
#ch.getMsgs() # retrieve recent messages