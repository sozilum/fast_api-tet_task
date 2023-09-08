from json import load, dump

class MessageProcessing:
    @staticmethod
    def process_message(user_id: int, data:str) -> str:
        user_id = str(user_id)
        with open('json/messages.json', 'r') as read_file:
            file = load(read_file)
            file[user_id][str(len(file[user_id].keys()) + 1)] = data

        yield '{}. {}: {}'.format(len(file[user_id].keys()) ,user_id ,data)

        with open('json/messages.json', 'w') as write_file:
            dump(file, write_file, indent= 2)

    @staticmethod
    def create_user_json(user_id:int) -> None:
        user_id = str(user_id)
        with open('json/messages.json', 'r') as read_file:
            file = load(read_file)
            file[user_id] = {}

        with open('json/messages.json', 'w') as write_file:
            dump(file, write_file, indent= 2)