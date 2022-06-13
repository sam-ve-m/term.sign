# Jormungandr - Onboarding
from ...infrastructures.s3.infrastructure import S3Infrastructure
from ...domain.enums.types import TermsFileType

# Third party
from etria_logger import Gladsheim
from decouple import config


class FileRepository:
    bucket_name = config("AWS_BUCKET_TERMS_SIGN")
    infra = S3Infrastructure

    @classmethod
    async def get_current_term_version(cls, term_type: TermsFileType) -> int:
        version = 0
        try:
            async with cls.infra.get_resource() as s3_resource:
                bucket = await s3_resource.Bucket(cls.bucket_name)
                async for s3_object in bucket.objects.filter(Prefix=term_type, Delimiter="/"):
                    version += 1
            return version
        except Exception as ex:
            Gladsheim.error(error=ex)
            raise ex
