# Jormungandr
from src.domain.validators.validator import TermFiles

# Standards
from datetime import datetime


class TermsModel:
    def __init__(
        self, unique_id: str, terms_type_validated: TermFiles, terms_version: list
    ):
        self.unique_id = unique_id
        self.terms_version = terms_version
        self.terms_type = terms_type_validated.terms_file
        self.term_answer_time_stamp = int(datetime.utcnow().timestamp())
        self.terms_signed = self._get_term_and_sign()

    def get_user_terms_signed_audit_template(self) -> dict:
        user_terms_signed_template = {
            "unique_id": self.unique_id,
            "terms_type": self.terms_type,
            "terms_update": {self.terms_type[index].value: {
                "version": self.terms_version[index],
                "date": datetime.utcnow(),
                "is_deprecated": False,
            } for index in range(len(self.terms_version))},
            "user_accept": True,
            "term_answer_time_stamp": self.term_answer_time_stamp,
        }
        return user_terms_signed_template

    def _get_term_and_sign(self) -> dict:
        terms_signed = {
            f"terms.{self.terms_type[index].value}": {
                "version": self.terms_version[index],
                "date": datetime.utcnow(),
                "is_deprecated": False,
            } for index in range(len(self.terms_version))
        }
        return terms_signed
