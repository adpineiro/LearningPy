import logging

logger=logging.getLogger(__name__)
file_handler = logging.FileHandler('log.log')
logger.setLevel(logging.INFO)
formatter = logging.Formatter(" %(asctime)s: %(levelname)s:" " %(message)s", "%d/%m/%Y %H:%M:%S")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def suma():
    logger.info("Suma realizada")
    return 5+2


print("Programa iniciado")
logger.info('program launched')
print("Programa finalizado")
logger.info('Programa finalizado')
suma()






