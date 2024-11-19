# External imports
import grpc

# Internal imports
from app.protos.company_pb2_grpc import CompanyServiceStub
from app.protos.company_pb2 import (
    CreateCompanyRequest,
    DeactivateCompanyRequest,
    ReactivateCompanyRequest,
)


class CompanyClient:
    def __init__(self, address):
        self.address = address
        self.channel = None
        self.stub = None

    def _create_channel(self, token):
        call_credentials = grpc.access_token_call_credentials(token)
        channel_credentials = grpc.ssl_channel_credentials()
        composite_credentials = grpc.composite_channel_credentials(
            channel_credentials, call_credentials
        )
        self.channel = grpc.secure_channel(self.address, composite_credentials)
        self.stub = CompanyServiceStub(self.channel)

    def create_company(
        self,
        token,
        company_id,
        company_name,
        trade_name,
        legal_entity_registration,
    ):
        self._create_channel(token)
        request = CreateCompanyRequest(
            company_id=company_id,
            company_name=company_name,
            trade_name=trade_name,
            legal_entity_registration=legal_entity_registration
        )
        response = self.stub.CreateCompany(request)
        return response

    def deactivate_company(self, token, company_id, reason):
        self._create_channel(token)
        request = DeactivateCompanyRequest(
            company_id=company_id,
            reason=reason
        )
        response = self.stub.DeactivateCompany(request)
        return response

    def reactivate_company(self, token, company_id, reason):
        self._create_channel(token)
        request = ReactivateCompanyRequest(
            company_id=company_id,
            reason=reason
        )
        response = self.stub.ReactivateCompany(request)
        return response
