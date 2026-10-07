import logging

def setup_logger(nome_modulo):

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8'
        )
    
    return logging.getLogger(nome_modulo)