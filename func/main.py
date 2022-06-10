# Jormungandr - Term.Sign
from src.domain.response.model import ResponseModel
from src.domain.enums.code import InternalCode
from src.services.jwt import JwtService

# Standards
from http import HTTPStatus


# Third party
from etria_logger import Gladsheim
from flask import request


def term_sign():
    raw_term_sign = request.json
    jwt = request.headers.get("x-thebes-answer")
    try:
        unique_id = JwtService.decode_jwt_and_get_unique_id(jwt=jwt)
        pass

    except Exception as ex:
        Gladsheim.error(error=ex)
        response = ResponseModel(
            success=False, code=InternalCode.INTERNAL_SERVER_ERROR, message=msg_error
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response
