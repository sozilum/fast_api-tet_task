from multiprocessing import Queue
from json import dumps

class MessageProcessing:
    def __init__(self) -> None:
        self.user_count = {}

    def process_message(self, user_id: int, data:str) -> str:
        user_id = str(user_id)
        self.user_count[user_id] += 1
        json_object = {
            'count':self.user_count[user_id],
            'user_id':user_id,
            'data':data,
            }
    
        return dumps(json_object)
    
    def create_user_count(self, user_id:int) -> None:
        user_id = str(user_id)
        self.user_count[user_id] = 0