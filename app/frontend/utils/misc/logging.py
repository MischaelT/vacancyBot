import logging

logging.basicConfig(
                    format=u'%(asctime)s - %(levelname)s - %(module)s %(funcName)s - %(message)s',
                    # level=logging.INFO,
                    level=logging.DEBUG,
                    # level=logging.ERROR,
                    filename='app.log',
                    filemode='w'
                    )
