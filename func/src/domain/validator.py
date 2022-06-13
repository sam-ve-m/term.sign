# Jormungandr - Term.Sign
from .enums.types import TermsFileType

# Standards
from typing import List

# Third party
from pydantic import BaseModel


class TermFile(BaseModel):
    file_type: TermsFileType


class TermsFile(BaseModel):
    file_types: List[TermsFileType]
