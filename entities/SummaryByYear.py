#!/usr/bin/env python

class SummaryByYear:
    """
    A class used to represent a full year of studies in summary format,
    ... 

    Attributes
    ----------
    year : str
        represent the year of study, for instance, the first/second/third year
    ranking : str
        general ranking (for the current year)
    grade : str
        grade point average
    mention : str
        mention obtained
    Methods
    -------
    getter/setter()
    """
    def __init__(self, year:str=None, grade:str=None, ranking:str=None, mention:str=None) -> None:
        self.__year = year
        self.__grade = grade
        self.__ranking = ranking
        self.__mention = mention

    def getYear(self) -> str:
        return self.__year
    
    def setYear(self, year:str) -> None:
        self.__year = year

    def getGrade(self) -> str:
        return self.__grade
    
    def setGrade(self, grade:str) -> None:
        self.__grade = grade

    def getRanking(self) -> str:
        return self.__ranking
    
    def setRanking(self, ranking:str) -> None:
        self.__ranking = ranking

    def getMention(self) -> str:
        return self.__mention
    
    def setMention(self, mention:str) -> None:
        self.__mention = mention