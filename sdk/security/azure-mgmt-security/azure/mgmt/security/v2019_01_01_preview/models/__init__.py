# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AdditionalData
from ._models_py3 import AlertsSuppressionRule
from ._models_py3 import AlertsSuppressionRulesList
from ._models_py3 import Automation
from ._models_py3 import AutomationAction
from ._models_py3 import AutomationActionEventHub
from ._models_py3 import AutomationActionLogicApp
from ._models_py3 import AutomationActionWorkspace
from ._models_py3 import AutomationList
from ._models_py3 import AutomationRuleSet
from ._models_py3 import AutomationScope
from ._models_py3 import AutomationSource
from ._models_py3 import AutomationTriggeringRule
from ._models_py3 import AutomationValidationStatus
from ._models_py3 import AzureResourceDetails
from ._models_py3 import AzureTrackedResourceLocation
from ._models_py3 import CVE
from ._models_py3 import CVSS
from ._models_py3 import CloudErrorBody
from ._models_py3 import ContainerRegistryVulnerabilityProperties
from ._models_py3 import ETag
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import Kind
from ._models_py3 import OnPremiseResourceDetails
from ._models_py3 import OnPremiseSqlResourceDetails
from ._models_py3 import RegulatoryComplianceAssessment
from ._models_py3 import RegulatoryComplianceAssessmentList
from ._models_py3 import RegulatoryComplianceControl
from ._models_py3 import RegulatoryComplianceControlList
from ._models_py3 import RegulatoryComplianceStandard
from ._models_py3 import RegulatoryComplianceStandardList
from ._models_py3 import Resource
from ._models_py3 import ResourceDetails
from ._models_py3 import ScopeElement
from ._models_py3 import SecuritySubAssessment
from ._models_py3 import SecuritySubAssessmentList
from ._models_py3 import ServerVulnerabilityProperties
from ._models_py3 import SqlServerVulnerabilityProperties
from ._models_py3 import SubAssessmentStatus
from ._models_py3 import SuppressionAlertsScope
from ._models_py3 import Tags
from ._models_py3 import TrackedResource
from ._models_py3 import VendorReference

from ._security_center_enums import ActionType
from ._security_center_enums import AssessedResourceType
from ._security_center_enums import EventSource
from ._security_center_enums import Operator
from ._security_center_enums import PropertyType
from ._security_center_enums import RuleState
from ._security_center_enums import Severity
from ._security_center_enums import Source
from ._security_center_enums import State
from ._security_center_enums import SubAssessmentStatusCode
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AdditionalData",
    "AlertsSuppressionRule",
    "AlertsSuppressionRulesList",
    "Automation",
    "AutomationAction",
    "AutomationActionEventHub",
    "AutomationActionLogicApp",
    "AutomationActionWorkspace",
    "AutomationList",
    "AutomationRuleSet",
    "AutomationScope",
    "AutomationSource",
    "AutomationTriggeringRule",
    "AutomationValidationStatus",
    "AzureResourceDetails",
    "AzureTrackedResourceLocation",
    "CVE",
    "CVSS",
    "CloudErrorBody",
    "ContainerRegistryVulnerabilityProperties",
    "ETag",
    "ErrorAdditionalInfo",
    "Kind",
    "OnPremiseResourceDetails",
    "OnPremiseSqlResourceDetails",
    "RegulatoryComplianceAssessment",
    "RegulatoryComplianceAssessmentList",
    "RegulatoryComplianceControl",
    "RegulatoryComplianceControlList",
    "RegulatoryComplianceStandard",
    "RegulatoryComplianceStandardList",
    "Resource",
    "ResourceDetails",
    "ScopeElement",
    "SecuritySubAssessment",
    "SecuritySubAssessmentList",
    "ServerVulnerabilityProperties",
    "SqlServerVulnerabilityProperties",
    "SubAssessmentStatus",
    "SuppressionAlertsScope",
    "Tags",
    "TrackedResource",
    "VendorReference",
    "ActionType",
    "AssessedResourceType",
    "EventSource",
    "Operator",
    "PropertyType",
    "RuleState",
    "Severity",
    "Source",
    "State",
    "SubAssessmentStatusCode",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()