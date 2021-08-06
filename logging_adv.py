import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# LOG TO FILE
formatter = logging.Formatter('%(asctime)s : %(filename)s : %(levelname)s : %(message)s')
file_handler = logging.FileHandler('log_adv.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# LOG TO CONSOLE
formatterCons = logging.Formatter('%(levelname)s : %(message)s')
cons_handler = logging.StreamHandler()
cons_handler.setFormatter(formatterCons)
logger.addHandler(cons_handler)

logger.info('logjdi')
