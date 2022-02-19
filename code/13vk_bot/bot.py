# from _token import token
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import logging
import logging.config

from log_settings import log_config

try:
    import settings
except ImportError:
    exit("DO import settings.py.default settings.py and set token!")

# group_id = 206048641

logging.config.dictConfig(log_config)
log_file = logging.getLogger("file")
log_stream = logging.getLogger("stream")


def configure_logging():
    log = "tüm log_gile ve log_stream yerine kullanılmıştı, tek logger içindi"
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler("bot_log.log", encoding="utf-8")
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s", datefmt= "%d-%m-%Y %H:%M:%S"))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)
# stream_handler.setLevel(logging.DEBUG)  # info koyarsan debug artık algılanmaz
# handlera atamak zorunda değilsin sadece daha hard core

# debug ta hepsi kapsarnır
# logging.DEBUG
# logging.INFO
# logging.ERROR
# logging.CRITICAL


class Bot:
    """
    echo bot for vk.com
    """

    def __init__(self, group_id, token):
        """
        :param group_id: vk grubun id'si
        :param token: grup token
        """
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(
            self.vk,
            self.group_id,
            )
        self.api = self.vk.get_api()

    def run(self):
        """
        botu başlatma
        """
        for event in self.long_poller.listen():
            log_file.debug("Catched event!")
            try:
                self._on_event(event)
            except Exception:
                log_file.exception("ошибка в обработке события")
                # print("err", e)

    def _on_event(self, event: VkBotEventType):
        """
        yeni mesaj geldiyse cevap verir
        :param event: VkBotEventType object
        :return:
        """
        if event.type == VkBotEventType.MESSAGE_NEW:
            # print(event.object.text)
            log_file.debug("re-send message back")
            custom_responce = self._mess_to_send(str(event.object.text))
            self.api.messages.send(
                message=custom_responce,
                random_id=random.randint(0, 2 ** 20),
                peer_id=event.object.peer_id,
            )
        else:
            log_file.info("not found wiki for %s", event.type)
            log_stream.info("not found wiki for %s", event.type)
            # print("not found type", event.type)

    def _mess_to_send(self, raw_mess):
        """
        yeni mesaj için text üretir
        :param raw_message: mesajda gelen text
        """
        return "len: " + str(len(raw_mess)) + "|" + raw_mess.upper()


if __name__ == "__main__":
    # configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()
