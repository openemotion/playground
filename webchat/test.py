import webchat

s = webchat.Storage()

s.store_message("eli", "hello world")

for message in s.get_messages():
    print message