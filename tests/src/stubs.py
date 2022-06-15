# Jormungandr - Term.sign
from func.src.domain.terms.model import TermsModel
from func.src.domain.validator import TermFiles


class UserUpdated:
    def __init__(self, acknowledged=None):
        self.acknowledged = acknowledged


stub_user_not_updated = UserUpdated(acknowledged=False)
stub_user_updated = UserUpdated(acknowledged=True)
stub_terms_file = {
    "terms_file": ["term_application", "term_open_account", "term_money_corp"]
}
stub_unique_id = "40db7fee-6d60-4d73-824f-1bf87edc4491"
stub_terms_type_validated = TermFiles(**stub_terms_file).dict()
stub_terms_model = TermsModel(unique_id=stub_unique_id, terms_type_validated=stub_terms_type_validated, terms_version=[1, 5, 3])
