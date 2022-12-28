# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.servicefabricmanagedclusters import ServiceFabricManagedClustersManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-servicefabricmanagedclusters
# USAGE
    python node_type_put_operation_example_max.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ServiceFabricManagedClustersManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.node_types.begin_create_or_update(
        resource_group_name="resRg",
        cluster_name="myCluster",
        node_type_name="BE",
        parameters={
            "properties": {
                "additionalDataDisks": [
                    {"diskLetter": "F", "diskSizeGB": 256, "diskType": "StandardSSD_LRS", "lun": 1},
                    {"diskLetter": "G", "diskSizeGB": 150, "diskType": "Premium_LRS", "lun": 2},
                ],
                "capacities": {"ClientConnections": "65536"},
                "dataDiskLetter": "S",
                "dataDiskSizeGB": 200,
                "dataDiskType": "Premium_LRS",
                "enableAcceleratedNetworking": True,
                "enableEncryptionAtHost": True,
                "enableOverProvisioning": False,
                "evictionPolicy": "Deallocate",
                "frontendConfigurations": [
                    {
                        "applicationGatewayBackendAddressPoolId": " /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resRg/providers/Microsoft.Network/applicationGateways/appgw-test/backendAddressPools/appgwBepoolTest",
                        "loadBalancerBackendAddressPoolId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resRg/providers/Microsoft.Network/loadBalancers/test-LB/backendAddressPools/LoadBalancerBEAddressPool",
                        "loadBalancerInboundNatPoolId": " /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resRg/providers/Microsoft.Network/loadBalancers/test-LB/inboundNatPools/LoadBalancerNATPool",
                    }
                ],
                "isPrimary": False,
                "isSpotVM": True,
                "isStateless": True,
                "multiplePlacementGroups": True,
                "placementProperties": {"HasSSD": "true", "NodeColor": "green", "SomeProperty": "5"},
                "spotRestoreTimeout": "PT30M",
                "useDefaultPublicLoadBalancer": True,
                "useEphemeralOSDisk": True,
                "vmExtensions": [
                    {
                        "name": "Microsoft.Azure.Geneva.GenevaMonitoring",
                        "properties": {
                            "autoUpgradeMinorVersion": True,
                            "enableAutomaticUpgrade": True,
                            "forceUpdateTag": "v.1.0",
                            "publisher": "Microsoft.Azure.Geneva",
                            "settings": {},
                            "type": "GenevaMonitoring",
                            "typeHandlerVersion": "2.0",
                        },
                    }
                ],
                "vmImageOffer": "WindowsServer",
                "vmImagePublisher": "MicrosoftWindowsServer",
                "vmImageSku": "2016-Datacenter-Server-Core",
                "vmImageVersion": "latest",
                "vmInstanceCount": 10,
                "vmManagedIdentity": {
                    "userAssignedIdentities": [
                        "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resRg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity",
                        "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resRg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity2",
                    ]
                },
                "vmSecrets": [
                    {
                        "sourceVault": {
                            "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resRg/providers/Microsoft.KeyVault/vaults/myVault"
                        },
                        "vaultCertificates": [
                            {
                                "certificateStore": "My",
                                "certificateUrl": "https://myVault.vault.azure.net:443/secrets/myCert/ef1a31d39e1f46bca33def54b6cda54c",
                            }
                        ],
                    }
                ],
                "vmSize": "Standard_DS3",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/servicefabricmanagedclusters/resource-manager/Microsoft.ServiceFabric/preview/2022-08-01-preview/examples/NodeTypePutOperation_example_max.json
if __name__ == "__main__":
    main()