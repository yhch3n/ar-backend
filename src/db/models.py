from sqlalchemy import Column, String, BigInteger
from db.database import Base
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ArDataAnnotation(Base):
    __tablename__ = 'arData'

    id: int
    roomId: str
    keyword: str
    modelMatrix: str
    anchorPose: str
    hashcode: str

    id = Column(BigInteger, primary_key = True, autoincrement=True)
    roomId = Column(String(50))
    keyword = Column(String(50))
    modelMatrix = Column(String(300))
    anchorPose = Column(String(50))
    hashcode = Column(String(50))

    def __init__(self, roomId, keyword, modelMatrix, anchorPose, hashcode):
        self.roomId = roomId
        self.keyword = keyword
        self.modelMatrix = modelMatrix
        self.anchorPose = anchorPose
        self.hashcode = hashcode
