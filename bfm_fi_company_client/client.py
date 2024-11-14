import grpc
from company_service_pb2_grpc import CompanyServiceStub
from company_service_pb2 import CreateCompanyRequest, DeactivateCompanyRequest, ReactivateCompanyRequest
from celero_flask_idp.core.helpers.functions.jwt import jwtoken
from celero_flask_idp.core.exceptions import IDPTransgressionError

def is_token_valid(token):
    try:
        jwt = jwtoken()
        jwt.set_token_data(token)
        jwt.validate()
        return True
    except IDPTransgressionError:
        return False

def create_company(stub, company_id, company_name, trade_name, registration_number, token):
    if not is_token_valid(token):
        raise IDPTransgressionError("Invalid or expired token")
    request = CreateCompanyRequest(
        company_id=company_id,
        company_name=company_name,
        trade_name=trade_name,
        registration_number=registration_number
    )
    response = stub.CreateCompany(request)
    return response

def deactivate_company(stub, company_id, reason, token):
    if not is_token_valid(token):
        raise IDPTransgressionError("Invalid or expired token")

    request = DeactivateCompanyRequest(
        company_id=company_id,
        reason=reason
    )
    response = stub.DeactivateCompany(request)
    return response

def reactivate_company(stub, company_id, reason, token):
    if not is_token_valid(token):
        raise IDPTransgressionError("Invalid or expired token")

    request = ReactivateCompanyRequest(
        company_id=company_id,
        reason=reason
    )
    response = stub.ReactivateCompany(request)
    return response

def run():
    token = jwtoken()  # Obtém o token usando a função jwtoken()
    credentials = grpc.metadata_call_credentials(
        lambda context, callback: callback([("authorization", f"Bearer {token}")], None)
    )
    channel = grpc.secure_channel("localhost:50051", grpc.composite_channel_credentials(credentials))
    stub = CompanyServiceStub(channel)

if __name__ == "__main__":
    run()
