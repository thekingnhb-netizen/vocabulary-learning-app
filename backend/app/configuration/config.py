import os
from dotenv import load_dotenv

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
load_dotenv(os.path.join(base_dir, ".env"))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///learn_vocabulary.db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    if os.getenv("TESTING") == "1":
        SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL", "sqlite:///:memory:")

    CORS_ORIGINS = ["http://localhost:5173"]
