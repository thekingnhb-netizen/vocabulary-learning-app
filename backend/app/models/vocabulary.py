from app.extensions import db
from datetime import datetime


class Vocabulary(db.Model):
    __tablename__ = "vocabularies"

    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey("topics.id"), nullable=False)
    word = db.Column(db.String(255), nullable=False)
    meaning = db.Column(db.Text, nullable=False)
    ipa_uk = db.Column(db.String(255), nullable=True)
    ipa_us = db.Column(db.String(255), nullable=True)
    example_en = db.Column(db.Text, nullable=True)
    example_vn = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Relationship
    progress = db.relationship(
        "VocabularyProgress", backref="vocabulary", uselist=False, cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Vocabulary {self.word}>"

    def to_dict(self, include_progress=False):
        data = {
            "id": self.id,
            "topic_id": self.topic_id,
            "word": self.word,
            "meaning": self.meaning,
            "ipa_uk": self.ipa_uk,
            "ipa_us": self.ipa_us,
            "example_en": self.example_en,
            "example_vn": self.example_vn,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
        if include_progress and self.progress:
            data["progress"] = self.progress.to_dict()
        return data
