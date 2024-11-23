# BFM FI Company Client

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

This project is a gRPC client for company management, developed to interact with Celero's `CompanyService`. It allows creating, deactivating, and reactivating companies through RPC calls.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See the [deployment](#deployment) section for notes on how to deploy the project on a live system.

### Prerequisites

You will need to have Python 3.13 installed. Additionally, make sure to have Poetry installed to manage the project's dependencies.

```sh
# Install Poetry
pip install poetry
```

### Installing

Follow the steps below to set up the development environment:

1. Clone the repository:

```sh
git clone https://github.com/your-username/bfm-fi-company-client.git
cd bfm-fi-company-client
```

2. Install the project dependencies using Poetry:

```sh
poetry install
```

3. Activate the Poetry virtual environment:

```sh
poetry shell
```

## Usage <a name = "usage"></a>

Here are some examples of how to use the `CompanyClient` to manage companies.

### Create a Company

```python
from app.client import CompanyClient

client = CompanyClient(address="grpc.server.address", ssl_cert="path/to/ssl_cert")
response = client.create_company(
    token="your-token",
    company_id="123",
    company_name="Company Name",
    trade_name="Trade Name",
    legal_entity_registration="00.000.000/0000-00"
)
print(response)
```

### Deactivate a Company

```python
response = client.deactivate_company(
    token="your-token",
    company_id="123",
    reason="Reason for deactivation"
)
print(response)
```

### Reactivate a Company

```python
response = client.reactivate_company(
    token="your-token",
    company_id="123",
    reason="Reason for reactivation"
)
print(response)
```