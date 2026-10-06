from app.extensions import db
from datetime import datetime
from enum import Enum


class ProgressStatus(Enum):
    NEW = "NEW"
    LEARNING = "LEARNING"
    REVIEW = "REVIEW"
    MASTERED = "MASTERED"


class VocabularyProgress(db.Model):
    __tablename__ = "vocabulary_progress"

    id = db.Column(db.Integer, primary_key=True)
    vocabulary_id = db.Column(
        db.Integer, db.ForeignKey("vocabularies.id"), nullable=False, unique=True
    )
    status = db.Column(
        db.String(20), default=ProgressStatus.NEW.value, nullable=False
    )
    level = db.Column(db.Integer, default=0, nullable=False)  # 0-6
    correct_count = db.Column(db.Integer, default=0, nullable=False)
    wrong_count = db.Column(db.Integer, default=0, nullable=False)
    review_count = db.Column(db.Integer, default=0, nullable=False)
    next_review_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_reviewed_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    def __repr__(self):
        return f"<VocabularyProgress vocabulary_id={self.vocabulary_id} level={self.level}>"

    def to_dict(self):
        return {
            "id": self.id,
            "vocabulary_id": self.vocabulary_id,
            "status": self.status,
            "level": self.level,
            "correct_count": self.correct_count,
            "wrong_count": self.wrong_count,
            "review_count": self.review_count,
            "next_review_at": self.next_review_at.isoformat(),
            "last_reviewed_at": self.last_reviewed_at.isoformat() if self.last_reviewed_at else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
