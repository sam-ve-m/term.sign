# Jormungandr
from ..validators.validator import TermFiles

# Standards
from datetime import datetime


class TermsModel:
    def __init__(
        self, unique_id: str, terms_type_validated: TermFiles, terms_version: list
    ):
        self.unique_id = unique_id
        self.terms_version = terms_version
        self.terms_type = terms_type_validated
        self.term_answer_time_stamp = int(datetime.utcnow().timestamp())
        self.terms_signed = self._get_term_and_sign()

    def get_user_terms_signed_audit_template(self) -> dict:
        user_terms_signed_template = {
            "unique_id": self.unique_id,
            "terms_type": self.terms_type.dict(),
            "terms_update": self.terms_signed,
            "user_accept": True,
            "term_answer_time_stamp": self.term_answer_time_stamp,
        }
        return user_terms_signed_template

    def _get_term_and_sign(self) -> dict:
        terms_signed = dict()
        terms_length = len(self.terms_version)
        term_type_list = self.terms_type.terms_file
        for index in range(terms_length):
            terms_signed.update(
                {
                    f"terms.{term_type_list[index]}": {
                        "version": self.terms_version[index],
                        "date": datetime.utcnow(),
                        "is_deprecated": False,
                    }
                }
            )
        return terms_signed
