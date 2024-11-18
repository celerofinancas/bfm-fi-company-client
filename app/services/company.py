"""Service layer for company domain."""

# Internal imports
from app.protos.company_pb2_grpc import CompanyStub
from app.protos.company_pb2 import (
    CreateCompanyRequest,
    DeactivateCompanyRequest,
    ReactivateCompanyRequest,
)


class CompanyService:
    def __init__(self, channel):
        self.stub = CompanyStub(channel)

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
