#!/usr/bin/env python
from datetime import datetime
from SummaryByYear import SummaryByYear

class Degree:
    """
    A class used to represent a Degree
    ...

    Attributes
    ----------
    degreeName : str
        the name of the Degree
    degreeEstablishment : str
        the establishment that awarded the degree
    startingDate : datetime.date
        starting date of the training
    finishingDate : datetime.date
        finishing date of the training
    description : str
        description of the subjects followed
    ranking : str
        general ranking (final year)
    grade : str
        grade point average
    mention : str
        mention obtained
    otherInformation : str
        additional information like scholarship or major work
    Methods
    -------
    displayDate(date:datetime.date)
        Prints the date in the appropriate format (YYYY-DD-MM)
    getter/setter()
    """
    def __init__(self, degreeName:str, degreeEstablishment:str, 
                startingDate:datetime.date, finishingDate:datetime.date, description:str=None, 
                ranking:str=None, grade:str=None, mention:str=None, otherInformation:str=None, summaryByYear:list=[]) -> None:
        self.__degreeName = degreeName
        self.__degreeEstablishment = degreeEstablishment
        self.__startingDate = startingDate
        self.__finishingDate = finishingDate
        self.__description = description
        self.__ranking = ranking
        self.__grade = grade
        self.__mention = mention
        self.__otherInformation = otherInformation
        self.__summaryByYear = summaryByYear
    
    @staticmethod
    def displayDate(date:datetime.date):
        return f"{date.year}-{date.day}-{date.month}"
    
    def getDegreeName(self) -> str:
        return self.__degreeName
    
    def setDegreeName(self, degreeName:str) -> None:
        self.__degreeName = degreeName
    
    def getDegreeEstablishment(self) -> str:
        return self.__degreeEstablishment
    
    def setDegreeEstablishment(self, degreeEstablishment:str) -> None:
        self.__degreeEstablishment = degreeEstablishment
    
    def getStartingDate(self) -> datetime.date:
        return self.__startingDate
    
    def setStartingDate(self, startingDate:datetime.date) -> None:
        self.__startingDate = startingDate

    def getFinishingDate(self) -> datetime.date:
        return self.__finishingDate
    
    def setFinishingDate(self, finishingDate:datetime.date) -> None:
        self.__finishingDate = finishingDate
    
    def getDescription(self) -> str:
        if self.__description is not None:
            return self.__description
        return "None"
    
    def setDescription(self, description:str) -> None:
        self.__description = description

    def getRanking(self) -> str:
        if self.__ranking is not None:
            return self.__ranking
        return "None"
    
    def setRanking(self, ranking:str) -> None:
        self.__ranking = ranking

    def getGrade(self) -> str:
        if self.__grade is not None:
            return self.__grade
        return "None"
    
    def setGrade(self, grade:str) -> None:
        self.__grade = grade
    
    def getMention(self) -> str:
        if self.__mention is not None:
            return self.__mention
        return "None"
    
    def setMention(self, mention:str) -> None:
        self.__mention = mention

    def getOtherInformation(self) -> str:
        if self.__otherInformation is not None:
            return self.__otherInformation
        return "None"
    
    def setOtherInformation(self, otherInformation:str) -> None:
        self.__otherInformation = otherInformation
    
    def getSummaryByYear(self) -> list:
        return self.__summaryByYear
    
    def setSummaryByYear(self, summaryByYear:list) -> None:
        self.__summaryByYear = summaryByYear
    
    def addSummaryByYear(self, elt:SummaryByYear) -> None:
        self.getSummaryByYear().append(elt)
    
    def deleteSummaryByYear(self, elt:SummaryByYear) -> None:
        self.getSummaryByYear().remove(elt)
