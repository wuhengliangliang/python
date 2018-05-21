import logging
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="logger.log",#存在某个文
#     filemode="w",#改成不追加的模式
#     format="%(asctime)s [%(lineno)s] %(message)s"
# )
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")
logger=logging.getLogger()
fh=logging.FileHandler("test_log")
ch=logging.StreamHandler()
fm=logging.Formatter("%(asctime)s %(message)s")

fh.setFormatter(fm)
ch.setFormatter(fm)
logger.addHandler(fh)
logger.addHandler(ch)
logging.basicConfig(
    level=logging.DEBUG,
    filename="test_log",
    filemode="w",)
logger.debug("hello")
logger.info("info")
logger.warning("warning")
logger.error("error")


