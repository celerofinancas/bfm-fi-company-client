import grpc
from company_service_pb2_grpc import CompanyServiceStub
from company_service_pb2 import CreateCompanyRequest, DeactivateCompanyRequest, ReactivateCompanyRequest
from keycloak import KeycloakOpenID

def get_keycloak_token():
    pass

def create_company(stub, company_id, company_name, trade_name, registration_number):
    request = CreateCompanyRequest(
        company_id=company_id,
        company_name=company_name,
        trade_name=trade_name,
        registration_number=registration_number
    )
    response = stub.CreateCompany(request)
    return response

def deactivate_company(stub, company_id, reason):
    request = DeactivateCompanyRequest(
        company_id=company_id,
        reason=reason
    )
    response = stub.DeactivateCompany(request)
    return response

def reactivate_company(stub, company_id, reason):
    request = ReactivateCompanyRequest(
        company_id=company_id,
        reason=reason
    )
    response = stub.ReactivateCompany(request)
    return response

def run():
    token = get_keycloak_token()
    credentials = grpc.metadata_call_credentials(
        lambda context, callback: callback([("authorization", f"Bearer {token}")], None)
    )
    channel = grpc.secure_channel("localhost:50051", grpc.composite_channel_credentials(credentials))
    stub = CompanyServiceStub(channel)

if __name__ == "__main__":
    run()
