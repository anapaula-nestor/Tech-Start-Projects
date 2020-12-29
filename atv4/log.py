from datetime import datetime

path = 'Data/log.txt'


def save_log(message: str) -> None:
    file = open(path, 'a')
    message = message.replace("['", "").replace("']", " ")
    file.write(f"[{datetime.today().strftime('%d/%m/%Y %H:%M:%S')}]: {message}\n")
    file.close()
