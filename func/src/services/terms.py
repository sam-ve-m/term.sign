# Jormungandr - Term.Sign
from ..domain.exceptions import UserUniqueIdNotExists, TermVersionNotExists, ErrorOnUpdateUser
from ..domain.terms.model import TermsModel
from ..repositories.mongo_db.user.repository import UserRepository
from ..repositories.s3.repository import FileRepository
from ..transports.audit.transport import Audit


class TermSignService:
    def __init__(self, unique_id: str, terms_type_validated: dict):
        self.unique_id = unique_id
        self.terms_type_validated = terms_type_validated

    async def user_terms_sign(self):
        terms_version = await self._get_terms_version()
        terms_model = TermsModel(
            unique_id=self.unique_id,
            terms_version=terms_version,
            terms_type_validated=self.terms_type_validated
        )
        await Audit.register_terms_log(terms_model=terms_model)
        user_updated = await UserRepository.update_one_with_terms_signed(
            unique_id=self.unique_id,
            terms_signed=terms_model.terms_signed
        )
        if not user_updated.acknowledged:
            raise ErrorOnUpdateUser
        return True

    async def _get_terms_version(self):
        terms_version = list()
        for term_type in self.terms_type_validated["file_types"]:
            term_version = await FileRepository.get_current_term_version(
                term_type=term_type)
            if not term_version:
                raise TermVersionNotExists
            terms_version.append(term_version)
        return terms_version

    async def _verify_unique_id_exists(self):
        user = await UserRepository.find_one_by_unique_id(unique_id=self.unique_id)
        if not user:
            raise UserUniqueIdNotExists
