# Jormungandr - Term.Sign
from .enums.types import TermsFileType

# Standards
from typing import List

# Third party
from pydantic import BaseModel


class TermFile(BaseModel):
    file_type: TermsFileType

    @classmethod
    def as_form(cls, file_type: str = Form(...)):
        return cls(file_type=file_type)


class TermsFile(BaseModel):
    file_types: List[TermsFileType]