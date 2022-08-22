# Jormungandr - Term.Sign
from func.src.domain.enums.types import TermsType

# Standards
from typing import List

# Third party
from pydantic import BaseModel


class TermFiles(BaseModel):
    terms_file: List[TermsType]
