# External imports
import grpc

# Internal imports
from app.services.company import CompanyService
from app.protos.company_pb2 import (
    CreateCompanyRequest,
    DeactivateCompanyRequest,
    ReactivateCompanyRequest,
)


class CompanyClient:
    def __init__(self, address, token):
        self.token = token
        self.channel = self.create_channel(address)
        self.service = self.create_service()

    def create_channel(self, address):
        call_credentials = grpc.access_token_call_credentials(self.token)
        channel_credentials = grpc.ssl_channel_credentials()
        composite_credentials = grpc.composite_channel_credentials(
            channel_credentials, call_credentials
        )
        return grpc.secure_channel(address, composite_credentials)

    def create_service(self):
        return CompanyService(self.channel)

    def create_company(
        self,
        company_id,
        company_name,
        trade_name,
        registration_number,
    ):
        request = CreateCompanyRequest(
            company_id=company_id,
            company_name=company_name,
            trade_name=trade_name,
            registration_number=registration_number
        )
        response_stream = self.stub.CreateCompany(request)
        for response in response_stream:
            yield response

    def deactivate_company(self, company_id, reason):
        request = DeactivateCompanyRequest(
            company_id=company_id,
            reason=reason
        )
        response = self.stub.DeactivateCompany(request)
        return response

    def reactivate_company(self, company_id, reason):
        request = ReactivateCompanyRequest(
            company_id=company_id,
            reason=reason
        )
        response_stream = self.stub.ReactivateCompany(request)
        for response in response_stream:
            yield response
