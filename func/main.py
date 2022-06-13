# Jormungandr - Term.Sign
from src.domain.enums.code import InternalCode
from src.domain.response.model import ResponseModel
from src.domain.validator import TermsFile
from src.services.jwt import JwtService
from src.services.terms import TermSignService

# Standards
from http import HTTPStatus

# Third party
from etria_logger import Gladsheim
from flask import request


async def terms_sign():
    raw_terms_type = request.json
    jwt = request.headers.get("x-thebes-answer")
    msg_error = "Unexpected error occurred"
    try:
        unique_id = await JwtService.decode_jwt_and_get_unique_id(jwt=jwt)
        terms_type_validated = TermsFile(**raw_terms_type).dict()
        terms_service = TermSignService(unique_id=unique_id, terms_type_validated=terms_type_validated)
        success = await terms_service.user_terms_sign()
        response = ResponseModel(
            success=success,
            message="Terms signed successfully",
            code=InternalCode.SUCCESS
        ).build_http_response(status=HTTPStatus.OK)
        return response

    except Exception as ex:
        Gladsheim.error(error=ex)
        response = ResponseModel(
            success=False, code=InternalCode.INTERNAL_SERVER_ERROR, message=msg_error
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response
