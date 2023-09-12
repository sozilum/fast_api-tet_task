from json import dumps


class MessageProcessing:
    def __init__(self) -> None:
        self.user_count = {}

    def process_message(self, user_id: int, data:str) -> dict:

        if user_id not in self.user_count:
            self.user_count[user_id] = 0

        self.user_count[user_id] += 1
        json_object = {
            'count':self.user_count[user_id],
            'user_id':user_id,
            'data':data,
            }

        return dumps(json_object)


    def clear_desconnected_user_count(self, user_id:int) -> None:
        self.user_count[user_id] = 0