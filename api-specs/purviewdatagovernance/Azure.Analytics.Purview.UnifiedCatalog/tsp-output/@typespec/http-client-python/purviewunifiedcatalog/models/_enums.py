# coding=utf-8

from enum import Enum
from corehttp.utils import CaseInsensitiveEnumMeta


class AudienceEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Audience enumeration for data products."""

    DATA_ENGINEER = "DataEngineer"
    """Data Engineer audience."""
    BI_ENGINEER = "BIEngineer"
    """BI Engineer audience."""
    DATA_ANALYST = "DataAnalyst"
    """Data Analyst audience."""
    DATA_SCIENTIST = "DataScientist"
    """Data Scientist audience."""
    BUSINESS_ANALYST = "BusinessAnalyst"
    """Business Analyst audience."""
    SOFTWARE_ENGINEER = "SoftwareEngineer"
    """Software Engineer audience."""
    BUSINESS_USER = "BusinessUser"
    """Business User audience."""
    EXECUTIVE = "Executive"
    """Executive audience."""


class CatalogApiServiceOrderDirection(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Ordering configuration for API service results."""

    ASC = "asc"
    """Ascending sort direction."""
    DESC = "desc"
    """Descending sort direction."""


class CatalogModelCriticalDataElementDataTypeEnum(  # pylint: disable=name-too-long
    str, Enum, metaclass=CaseInsensitiveEnumMeta
):
    """Data types supported for critical data elements."""

    TEXT = "TEXT"
    """Text data type."""
    NUMBER = "NUMBER"
    """Numeric data type."""
    DATE_TIME = "DATETIME"
    """Date and time data type."""
    BOOLEAN = "BOOLEAN"
    """Boolean data type."""


class CatalogModelDataProductTypeEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CatalogModelDataProductTypeEnum."""

    MASTER = "Master"
    """The status is Master."""
    REFERENCE = "Reference"
    """The status is Reference."""
    ANALYTICAL = "Analytical"
    """The status is Analytical."""
    AI = "AI"
    """The status is AI."""
    MASTER_DATA_AND_REFERENCE_DATA = "MasterDataAndReferenceData"
    """The status is MasterDataAndReferenceData."""
    BUSINESS_SYSTEM_OR_APPLICATION = "BusinessSystemOrApplication"
    """The status is BusinessSystemOrApplication."""
    MODEL_TYPES = "ModelTypes"
    """The status is ModelTypes."""
    DASHBOARDS_OR_REPORTS = "DashboardsOrReports"
    """The status is DashboardsOrReports."""
    OPERATIONAL = "Operational"
    """The status is Operational."""
    MLAI_TRAINING_DATA_SET = "MLAITrainingDataSet"
    """The status is MLAITrainingDataSet."""
    MLAI_TESTING_DATA_SET = "MLAITestingDataSet"
    """The status is MLAITestingDataSet."""
    TRANSACTIONAL_DATASET = "TransactionalDataset"
    """The status is TransactionalDataset."""
    ANALYTICS_MODEL = "AnalyticsModel"
    """The status is AnalyticsModel."""
    SEMANTIC_MODEL = "SemanticModel"
    """The status is SemanticModel."""


class CatalogModelDomainTypeEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CatalogModelDomainTypeEnum."""

    FUNCTIONAL_UNIT = "FunctionalUnit"
    """The status is FunctionalUnit."""
    LINE_OF_BUSINESS = "LineOfBusiness"
    """The status is LineOfBusiness."""
    DATA_DOMAIN = "DataDomain"
    """The status is DataDomain."""
    REGULATORY = "Regulatory"
    """The status is Regulatory."""
    PROJECT = "Project"
    """The status is Project."""


class CatalogModelStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of a catalog model entity indicating its lifecycle state."""

    DRAFT = "DRAFT"
    """The entity is in draft state."""
    PUBLISHED = "PUBLISHED"
    """The entity is published and active."""
    EXPIRED = "EXPIRED"
    """The entity has expired and is no longer active."""


class DataAssetProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of a data asset."""

    UNKNOWN = "Unknown"
    """The provisioning state is unknown."""
    SUCCEEDED = "Succeeded"
    """The resource has been successfully provisioned."""
    SOFT_DELETED = "SoftDeleted"
    """The resource has been soft deleted."""


class DataAssetRelationshipType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of relationship between data assets."""

    RELATED = "Related"
    """Related relationship type."""
    SYNONYM = "Synonym"
    """Synonym relationship type."""


class DataAssetType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of a data asset."""

    AZURE_SQL_TABLE = "AzureSqlTable"
    """Azure SQL Table data asset type."""
    ADLS_GEN2_PATH = "ADLSGen2Path"
    """ADLS Gen2 Path data asset type."""
    GENERAL = "General"
    """General data asset type."""


class DataColumnRelationshipType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of relationship between data columns."""

    RELATED = "Related"
    """Related relationship type."""
    SYNONYM = "Synonym"
    """Synonym relationship type."""
    PARENT = "Parent"
    """Parent relationship type."""


class EntityCategory(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Categories of entities that can be managed in the catalog."""

    DOMAIN = "DOMAIN"
    """Domain entity category."""
    DATA_PRODUCT = "DATAPRODUCT"
    """Data product entity category."""
    TERM = "TERM"
    """Term entity category."""
    DATA_ASSET = "DATAASSET"
    """Data asset entity category."""
    OBJECTIVE = "OBJECTIVE"
    """Objective entity category."""
    KEY_RESULT = "KEYRESULT"
    """Key result entity category."""
    CRITICAL_DATA_ELEMENT = "CRITICALDATAELEMENT"
    """Critical data element entity category."""
    DATA_COLUMN = "DATACOLUMN"
    """Data column entity category."""
    CUSTOM_METADATA = "CUSTOMMETADATA"
    """Custom metadata entity category."""
    ATTRIBUTE = "ATTRIBUTE"
    """Attribute entity category."""
    ATTRIBUTE_INSTANCE = "ATTRIBUTEINSTANCE"
    """Attribute instance entity category."""
    WORKFLOW = "WORKFLOW"
    """Workflow entity category."""
    CATALOG_SNAPSHOT = "CATALOGSNAPSHOT"
    """Catalog snapshot entity category."""
    WORKFLOW_RUN = "WORKFLOWRUN"
    """Workflow run entity category."""


class OkrSharedEntityStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """OkrSharedEntityStatus."""

    DRAFT = "Draft"
    """The status is Draft."""
    PUBLISHED = "Published"
    """The status is published."""
    CLOSED = "Closed"
    """The status is Closed."""


class OverallStatusEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """OverallStatusEnum."""

    NOT_TRACKED = "NotTracked"
    """The status is NotTracked."""
    ON_TRACK = "OnTrack"
    """The status is OnTrack."""
    BEHIND = "Behind"
    """The status is Behind."""
    AT_RISK = "AtRisk"
    """The status is AtRisk."""


class RelatedCollectionParentCollectionTypeEnum(  # pylint: disable=name-too-long
    str, Enum, metaclass=CaseInsensitiveEnumMeta
):
    """Related collection parent collection type enumeration."""

    COLLECTION_REFERENCE = "CollectionReference"
    """Collection reference type."""


class SharedEntityStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of shared entities in the catalog."""

    DRAFT = "Draft"
    """The entity is in draft state."""
    PUBLISHED = "Published"
    """The entity is published and active."""
    EXPIRED = "Expired"
    """The entity has expired and is no longer active."""


class TermRelationshipType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """TermRelationshipType."""

    RELATED = "Related"
    """The status is Related."""
    SYNONYM = "Synonym"
    """The status is Synonym."""
    PARENT = "Parent"
    """The status is Parent."""


class TypePropertiesFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The format of the SQL table."""

    TABLE = "Table"
    """Table format."""
    VIEW = "View"
    """View format."""


class UpdateFrequencyEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """UpdateFrequencyEnum."""

    HOURLY = "Hourly"
    """The status is Hourly."""
    DAILY = "Daily"
    """The status is Daily."""
    WEEKLY = "Weekly"
    """The status is Weekly."""
    MONTHLY = "Monthly"
    """The status is Monthly."""
    QUARTERLY = "Quarterly"
    """The status is Quarterly."""
    YEARLY = "Yearly"
    """The status is Yearly."""
