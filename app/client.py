# External imports
import grpc

# Celero imports
from celero_bfm_fi_proto.company.company_pb2_grpc import CompanyServiceStub
from celero_bfm_fi_proto.company.company_pb2 import (
    CreateCompanyRequest,
    CreateCompanyResponse,
    DeactivateCompanyRequest,
    DeactivateCompanyResponse,
    ReactivateCompanyRequest,
    ReactivateCompanyResponse,
)


class CompanyClient:
    """CompanyClient is a gRPC client that deals with company management.

    :param address: The address of the gRPC server.
    """
    def __init__(self, address: str):
        self.address = address
        channel_credentials = grpc.ssl_channel_credentials()
        self.channel = grpc.secure_channel(
            self.address,
            channel_credentials=channel_credentials,
        )
        self.stub = CompanyServiceStub(self.channel)

    def create_company(
        self,
        token: str,
        company_id: str,
        company_name: str,
        trade_name: str,
        legal_entity_registration: str,
    ) -> CreateCompanyResponse:
        """Create a company. This method will call the CreateCompany RPC.

        :param token: The access token to authenticate the user.
        :param company_id: The ID of the company.
        :param company_name: The name of the company.
        :param trade_name: The trade name of the company.
        :param legal_entity_registration: Brazilian CNPJ.
        :return: The response from the CreateCompany RPC.
        """
        request = CreateCompanyRequest(
            company_id=company_id,
            company_name=company_name,
            trade_name=trade_name,
            legal_entity_registration=legal_entity_registration
        )
        response = self.stub.CreateCompany(
            request,
            call_credentials=grpc.access_token_call_credentials(token),
        )
        return response

    def deactivate_company(
        self,
        token: str,
        company_id: str,
        reason: str
    ) -> DeactivateCompanyResponse:
        """Deactivate a company calling the DeactivateCompany RPC.

        :param token: The access token to authenticate the user.
        :param company_id: The ID of the company.
        :param reason: The reason to deactivate the company.
        :return: The response from the DeactivateCompany RPC.
        """
        request = DeactivateCompanyRequest(
            company_id=company_id,
            reason=reason
        )
        response = self.stub.DeactivateCompany(
            request,
            call_credentials=grpc.access_token_call_credentials(token),
        )
        return response

    def reactivate_company(
        self,
        token: str,
        company_id: str,
        reason: str
    ) -> ReactivateCompanyResponse:
        """Reactivate a company calling the ReactivateCompany RPC.

        :param token: The access token to authenticate the user.
        :param company_id: The ID of the company.
        :param reason: The reason to reactivate the company.
        :return: The response from the ReactivateCompany RPC.
        """
        request = ReactivateCompanyRequest(
            company_id=company_id,
            reason=reason
        )
        response = self.stub.ReactivateCompany(
            request,
            call_credentials=grpc.access_token_call_credentials(token),
        )
        return response
