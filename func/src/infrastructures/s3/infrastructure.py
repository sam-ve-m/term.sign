# Third party
from contextlib import asynccontextmanager
from decouple import config
from etria_logger import Gladsheim
import aioboto3


class S3Infrastructure:

    session = None

    @classmethod
    async def _get_session(cls):
        if cls.session is None:
            try:
                cls.session = aioboto3.Session(
                    aws_access_key_id=config("AWS_ACCESS_KEY_ID"),
                    aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"),
                    region_name=config("REGION_NAME"),
                )
            except Exception as ex:
                Gladsheim.error(error=ex)
        return cls.session

    @classmethod
    @asynccontextmanager
    async def get_client(cls):
        try:
            session = await S3Infrastructure._get_session()
            async with session.client("s3") as s3_client:
                yield s3_client
        except Exception as ex:
            Gladsheim.error(error=ex)
            raise ex

    @classmethod
    @asynccontextmanager
    async def get_resource(cls):
        try:
            session = await S3Infrastructure._get_session()
            async with session.resource("s3") as s3_resource:
                yield s3_resource
        except Exception as ex:
            Gladsheim.error(error=ex)
            raise ex
