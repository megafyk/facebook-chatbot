from fbchat import log, Client
import json
import os

class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        log.info("{} from {} in {}".format(
            message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id,
                      thread_type=thread_type)

user_data = json.load(open('user.json'))
user_data_email = user_data['users'][0]['email']
user_data_password = user_data['users'][0]['password']
client = EchoBot(user_data_email, user_data_password)
client.listen()
