from loguru import logger
from .model import ResultModel


class Functions:
    def __init__(self):
        pass

    @logger.catch
    def preprocess_bizlogic(self, queryStr: str) -> str:
        # bizlogic for preprocess here
        return queryStr.lower()


    @logger.catch
    def postprocess_bizlogic(self, response) -> ResultModel:

        # bizlogic for postprocess here

        if response is None:
            return ResultModel()

        return ResultModel(example=response)

    @logger.catch
    def process(
        self, queryStr: str, take: int = 10, skip: int = 0
    ) -> ResultModel:

        queryStr = self.preprocess_bizlogic(queryStr)

        response = self.__process(queryStr, take, skip)

        response = self.postprocess_bizlogic(response)

        return response

    @logger.catch
    def __process(self, queryStr: str, take: int = 10, skip: int = 0) -> callable:

        return "hellu {}".format(queryStr)
        
