import os
import workflow.mainflow as mainflow
from dotenv import load_dotenv
from loguru import logger


pwd_path = os.path.abspath(os.path.dirname(__file__))
env_file = os.path.join(pwd_path, ".env")

if __name__ == '__main__':
    load_dotenv(env_file, override=True)
    logger.info(f"env_file:{env_file}, {os.environ}")
    mainflow.execute()
