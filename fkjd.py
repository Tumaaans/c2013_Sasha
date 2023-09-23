import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="fkjd.py.Log",
                    filemode="w",
                    format="We have massage: %\(asc time)s:%(levelname)s:%(message)s")

logging.debug("debug")
logging.info("info log")
logging.warning("warning aaaaaaaaaaaa")
logging.error("error")
logging.critical("system dead")


