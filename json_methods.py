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
            'data':data
            }
    
        return dumps(json_object)
    
    def create_user_count(self, user_id:int) -> None:
        user_id = str(user_id)
        self.user_count[user_id] = 0


#На всякий случай
# class Queue_init(MessageProcessing):
#     def __init__(self) -> None:
#         super().__init__()
#         self.queue = Queue()

#     def create_user_count(self, user_id: int) -> None:
#         self.queue.put(super().create_user_count(user_id))
#         return self.queue.get()

#     def process_message(self, user_id: int, data: str) -> str:

#         return super().process_message(user_id, data)