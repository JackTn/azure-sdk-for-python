# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.communication import CommunicationServiceManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-communication
# USAGE
    python delete_address.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CommunicationServiceManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="11112222-3333-4444-5555-666677778888",
    )

    client.suppression_list_addresses.delete(
        resource_group_name="MyResourceGroup",
        email_service_name="MyEmailServiceResource",
        domain_name="mydomain.com",
        suppression_list_name="aaaa1111-bbbb-2222-3333-aaaa11112222",
        address_id="11112222-3333-4444-5555-999999999999",
    )


# x-ms-original-file: specification/communication/resource-manager/Microsoft.Communication/preview/2023-06-01-preview/examples/suppressionLists/deleteAddress.json
if __name__ == "__main__":
    main()
