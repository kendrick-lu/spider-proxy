from util.redis_util import RedisUtil

proxy_list = ['http://148558:148558@ip3.hahado.cn:48936',
              'http://148559:148559@ip3.hahado.cn:48937',
              'http://148560:148560@ip3.hahado.cn:48938',
              'http://148561:148561@ip3.hahado.cn:48939',
              'http://148562:148562@ip3.hahado.cn:48940',
              'http://148563:148563@ip3.hahado.cn:48941',
              'http://148564:148564@ip3.hahado.cn:48942',
              'http://148565:148565@ip3.hahado.cn:48943',
              'http://148566:148566@ip3.hahado.cn:48944',
              'http://148567:148567@ip3.hahado.cn:48945',
              'http://148568:148568@ip3.hahado.cn:48946',
              'http://148569:148569@ip3.hahado.cn:48947',
              'http://148570:148570@ip3.hahado.cn:48948',
              'http://148571:148571@ip3.hahado.cn:48949',
              'http://148572:148572@ip3.hahado.cn:48950',
              'http://126880:126880@ip5.hahado.cn:47204',
              'http://126881:126881@ip5.hahado.cn:47205',
              'http://151652:151652@ip5.hahado.cn:42057',
              'http://126884:126884@ip5.hahado.cn:47208',
              'http://135596:135596@ip5.hahado.cn:45947',
              'http://148573:148573@ip5.hahado.cn:48951',
              'http://148574:148574@ip5.hahado.cn:48952',
              'http://148575:148575@ip5.hahado.cn:48953',
              'http://148576:148576@ip5.hahado.cn:48954',
              'http://148577:148577@ip5.hahado.cn:48955',
              'http://148578:148578@ip5.hahado.cn:48956',
              'http://151651:151651@ip5.hahado.cn:42056',
              'http://148580:148580@ip5.hahado.cn:48958',
              'http://148581:148581@ip5.hahado.cn:48959',
              'http://148582:148582@ip5.hahado.cn:48960',
              'http://148583:148583@ip5.hahado.cn:48961',
              'http://148584:148584@ip5.hahado.cn:48962',
              'http://148585:148585@ip5.hahado.cn:48963',
              'http://148586:148586@ip5.hahado.cn:48964',
              'http://148587:148587@ip5.hahado.cn:48965']

redis_queues = ["rest:queue:app", "rest:queue:five", "rest:queue:rob", "rest:queue:c4", "rest:queue:all"]
redis_client = RedisUtil.get_redis_client('52.80.245.214', 30163, 5)


def update_proxy(proxy_str):
    for queue in redis_queues:
        pipeline = redis_client.pipeline()
        pipeline.zadd(queue, {proxy_str: 9999})
        pipeline.execute()


for proxy in proxy_list:
    update_proxy(proxy.strip())
    print(proxy + "\t    succeed..")
