# Jormungandr - Term.Sign
from ..enums.types import TermsType

# Standards
from typing import List

# Third party
from pydantic import BaseModel


class TermFiles(BaseModel):
    terms_file: List[TermsType]
