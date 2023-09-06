from json import load, dump

class MessageProcessing:
    def __init__(self) -> None:
        self.counter = int()

    def set_message(self, user_id: int, data:str) -> None:
        user_id = str(user_id)
        self.counter += 1
        with open('json/messages.json', 'r') as read_file:
            file = load(read_file)

            if user_id not in file:
                file.update({user_id:{}})
                file[user_id][str(self.counter)] = data

            else:
                file[user_id][str(self.counter)] = data

        with open('json/messages.json', 'w') as write_file:
            dump(file, write_file, indent= 2)


    def get_message(self, user_id:int) -> str:
        user_id = str(user_id)
        with open('json/messages.json', 'r') as read_file:
            last_message = load(read_file)
            return '{}. {}: {}'.format(self.counter ,user_id ,last_message[user_id][str(self.counter)])