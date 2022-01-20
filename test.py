import traceback

from main import send_proposal


# viktorosipovsrl@yandex.ru:j_gavmqfqaA9:Sun of the slee
# haritonmorozovpic@yandex.ru:qbw_wjzhgaL1:Отбились лебеди
# zinaidafilatovag@rambler.ru:dvsulytdmhF2

def tests():
    # email'ы можно использовать для тестирования, некоторые рабочие, некоторые нет. Прокси адреса указаны для примера
    examples = [('viktorosipovsrl@yandex.ru', 'j_gavmqfqaA9', 'imap.yandex.ru:993', '1.1.1.1:1080', '2.2.2.2:3128',
                 'Viktor', 'Osipov', 'omMvxNH6aj'),
                ('veraisakovsari@rambler.ru', 'llmdzqfsldV4', 'imap.rambler.ru:993', '1.1.1.1:1080', '2.2.2.2:3128',
                 'Vera', 'Isakova', 'EcKXnm02Gx'),
                ('veraisakovsari@rambler.ru', 'llmdzqfsldV4', 'imap.rambler.ru:993', '1.1.1.1:1080', '2.2.2.2:3128',
                 'Vera2', 'Isakova2', 'xbisliRgKo'),
                ('joseph-gomezd2@outlook.com', 'kIKBPWQKvfXi1', 'outlook.office365.com:993', '1.1.1.1:1080',
                 '2.2.2.2:3128', 'Joseph', 'Gomez', 'SyVIONW6H6')
                ]
    for example in examples:
        print(str(example))
        try:
            print(str(send_proposal(*example)))
        except Exception:
            print(traceback.format_exc())


if __name__ == '__main__':
    tests()
