# Jormungandr - Term.Sign
from func.src.services.terms import TermSignService
from .stubs import stub_terms_type_validated, stub_unique_id

# Third party
from pytest import fixture


@fixture(scope='function')
def term_sign_service():
    service_instance = TermSignService(
        unique_id=stub_unique_id,
        terms_type_validated=stub_terms_type_validated
    )
    return service_instance
