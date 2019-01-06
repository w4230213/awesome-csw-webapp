import orm,asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop,user='csw', password='csw', db='awesome')

    u = User(name='CeaserWayne', email='maxjing1025@gmail.com', passwd='csw', image='about:blank')

    await u.save()

def run(task=None):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task(loop,**kw) or test(loop))


if __name__ == '__main__':

  run()