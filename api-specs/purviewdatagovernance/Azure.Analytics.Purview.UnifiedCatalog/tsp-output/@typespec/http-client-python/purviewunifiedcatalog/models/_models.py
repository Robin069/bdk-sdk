# pylint: disable=line-too-long,useless-suppression,too-many-lines
# coding=utf-8
# pylint: disable=useless-super-delegation

import datetime
from typing import Any, Literal, Mapping, Optional, TYPE_CHECKING, Union, overload

from .._utils.model_base import Model as _Model, rest_discriminator, rest_field
from ._enums import DataAssetType

if TYPE_CHECKING:
    from .. import models as _models


class AttributeRule(_Model):
    """AttributeRule.

    :ivar kind: The kind of attribute rule. Required.
    :vartype kind: str
    :ivar id: The unique identifier of the attribute rule. Required.
    :vartype id: str
    :ivar name: The name of the attribute rule. Required.
    :vartype name: str
    :ivar dnf_condition: The description of the attribute rule. Required.
    :vartype dnf_condition: list[list[~purviewunifiedcatalog.models.Condition]]
    """

    kind: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The kind of attribute rule. Required."""
    id: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the attribute rule. Required."""
    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name of the attribute rule. Required."""
    dnf_condition: list[list["_models.Condition"]] = rest_field(
        name="dnfCondition", visibility=["read", "create", "update", "delete", "query"]
    )
    """The description of the attribute rule. Required."""

    @overload
    def __init__(
        self,
        *,
        kind: str,
        id: str,  # pylint: disable=redefined-builtin
        name: str,
        dnf_condition: list[list["_models.Condition"]],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogApiServiceOrderBy(_Model):
    """Ordering configuration for API service results.

    :ivar field: The field name to order by.
    :vartype field: str
    :ivar direction: The sort direction (asc or desc). Known values are: "asc" and "desc".
    :vartype direction: str or ~purviewunifiedcatalog.models.CatalogApiServiceOrderDirection
    """

    field: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The field name to order by."""
    direction: Optional[Union[str, "_models.CatalogApiServiceOrderDirection"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The sort direction (asc or desc). Known values are: \"asc\" and \"desc\"."""

    @overload
    def __init__(
        self,
        *,
        field: Optional[str] = None,
        direction: Optional[Union[str, "_models.CatalogApiServiceOrderDirection"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogModelContactsValueInner(_Model):
    """Contact information for catalog entities.

    :ivar id: AAD oid for the person or group.
    :vartype id: str
    :ivar description: A description of this user assignment.
    :vartype description: str
    """

    id: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """AAD oid for the person or group."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """A description of this user assignment."""

    @overload
    def __init__(
        self,
        *,
        id: Optional[str] = None,  # pylint: disable=redefined-builtin
        description: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogModelDataAssetSchema(_Model):
    """Schema of the asset.

    :ivar name: Name of the asset.
    :vartype name: str
    :ivar description: Description of the asset.
    :vartype description: str
    :ivar classifications: A list of classification labels. example: [PII, PHI].
    :vartype classifications: list[str]
    :ivar type: Type of the asset.
    :vartype type: str
    """

    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Name of the asset."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Description of the asset."""
    classifications: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """A list of classification labels. example: [PII, PHI]."""
    type: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Type of the asset."""

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        classifications: Optional[list[str]] = None,
        type: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogModelDataAssetSource(_Model):
    """Source information for data assets.

    :ivar type: The type of the data asset source.
    :vartype type: str
    :ivar asset_id: Link to the data map asset ID.
    :vartype asset_id: str
    :ivar asset_type: Data map asset type. Example: adls_gen2_path, azure_sql_table, etc.
    :vartype asset_type: str
    :ivar asset_attributes: Type properties of the asset.
    :vartype asset_attributes: list[str]
    :ivar fqn: Fully qualified name of the data asset.
    :vartype fqn: str
    :ivar account_name: The data map account name of the data asset.
    :vartype account_name: str
    :ivar last_refreshed_at: Date of the last sync time.
    :vartype last_refreshed_at: ~datetime.datetime
    :ivar last_refreshed_by: ID of the user who last refreshed the asset.
    :vartype last_refreshed_by: str
    """

    type: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The type of the data asset source."""
    asset_id: Optional[str] = rest_field(name="assetId", visibility=["read", "create", "update", "delete", "query"])
    """Link to the data map asset ID."""
    asset_type: Optional[str] = rest_field(name="assetType", visibility=["read", "create", "update", "delete", "query"])
    """Data map asset type. Example: adls_gen2_path, azure_sql_table, etc."""
    asset_attributes: Optional[list[str]] = rest_field(
        name="assetAttributes", visibility=["read", "create", "update", "delete", "query"]
    )
    """Type properties of the asset."""
    fqn: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Fully qualified name of the data asset."""
    account_name: Optional[str] = rest_field(
        name="accountName", visibility=["read", "create", "update", "delete", "query"]
    )
    """The data map account name of the data asset."""
    last_refreshed_at: Optional[datetime.datetime] = rest_field(
        name="lastRefreshedAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """Date of the last sync time."""
    last_refreshed_by: Optional[str] = rest_field(
        name="lastRefreshedBy", visibility=["read", "create", "update", "delete", "query"]
    )
    """ID of the user who last refreshed the asset."""

    @overload
    def __init__(
        self,
        *,
        type: Optional[str] = None,
        asset_id: Optional[str] = None,
        asset_type: Optional[str] = None,
        asset_attributes: Optional[list[str]] = None,
        fqn: Optional[str] = None,
        account_name: Optional[str] = None,
        last_refreshed_at: Optional[datetime.datetime] = None,
        last_refreshed_by: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogModelDataAssetSourceRequest(_Model):
    """Source information for data assets request.

    :ivar asset_id: Link to the data map asset ID.
    :vartype asset_id: str
    """

    asset_id: Optional[str] = rest_field(name="assetId", visibility=["read", "create", "update", "delete", "query"])
    """Link to the data map asset ID."""

    @overload
    def __init__(
        self,
        *,
        asset_id: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogModelDataProductAllOfAdditionalProperties(_Model):  # pylint: disable=name-too-long
    """Additional properties for data product model.

    :ivar asset_count: The number of assets in the data product.
    :vartype asset_count: int
    """

    asset_count: Optional[int] = rest_field(
        name="assetCount", visibility=["read", "create", "update", "delete", "query"]
    )
    """The number of assets in the data product."""

    @overload
    def __init__(
        self,
        *,
        asset_count: Optional[int] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogModelDomainAllOfThumbnail(_Model):
    """Catalog model domain thumbnail properties.

    :ivar color: The color of the thumbnail.
    :vartype color: str
    """

    color: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The color of the thumbnail."""

    @overload
    def __init__(
        self,
        *,
        color: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogModelExternalLink(_Model):
    """External link model for data product.

    :ivar url: The URL of the external link.
    :vartype url: str
    :ivar name: The name of the external link.
    :vartype name: str
    :ivar data_asset_id: The data asset identifier associated with the link.
    :vartype data_asset_id: str
    """

    url: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The URL of the external link."""
    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name of the external link."""
    data_asset_id: Optional[str] = rest_field(
        name="dataAssetId", visibility=["read", "create", "update", "delete", "query"]
    )
    """The data asset identifier associated with the link."""

    @overload
    def __init__(
        self,
        *,
        url: Optional[str] = None,
        name: Optional[str] = None,
        data_asset_id: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogModelKeyResult(_Model):
    """Catalog model key result.

    :ivar status: The status of the key result. Known values are: "NotTracked", "OnTrack",
     "Behind", and "AtRisk".
    :vartype status: str or ~purviewunifiedcatalog.models.OverallStatusEnum
    :ivar system_data: The system data associated with the key result.
    :vartype system_data: ~purviewunifiedcatalog.models.SystemData
    :ivar id: The unique identifier of the key result.
    :vartype id: str
    :ivar definition: The definition of the key result.
    :vartype definition: str
    :ivar domain_id: The unique identifier of the domain.
    :vartype domain_id: str
    :ivar progress: The progress of the key result.
    :vartype progress: float
    :ivar goal: The goal value for the key result.
    :vartype goal: float
    :ivar max: The maximum value for the key result.
    :vartype max: float
    """

    status: Optional[Union[str, "_models.OverallStatusEnum"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The status of the key result. Known values are: \"NotTracked\", \"OnTrack\", \"Behind\", and
     \"AtRisk\"."""
    system_data: Optional["_models.SystemData"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """The system data associated with the key result."""
    id: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the key result."""
    definition: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The definition of the key result."""
    domain_id: Optional[str] = rest_field(name="domainId", visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the domain."""
    progress: Optional[float] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The progress of the key result."""
    goal: Optional[float] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The goal value for the key result."""
    max: Optional[float] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The maximum value for the key result."""

    @overload
    def __init__(
        self,
        *,
        status: Optional[Union[str, "_models.OverallStatusEnum"]] = None,
        system_data: Optional["_models.SystemData"] = None,
        id: Optional[str] = None,  # pylint: disable=redefined-builtin
        definition: Optional[str] = None,
        domain_id: Optional[str] = None,
        progress: Optional[float] = None,
        goal: Optional[float] = None,
        max: Optional[float] = None,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogModelManagedAttribute(_Model):
    """Managed attribute configuration for catalog entities.

    :ivar name: The name of the managed attribute.
    :vartype name: str
    :ivar value: The value of the attribute.
    :vartype value: str
    :ivar is_required: Whether this attribute is required.
    :vartype is_required: bool
    """

    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name of the managed attribute."""
    value: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The value of the attribute."""
    is_required: Optional[bool] = rest_field(
        name="isRequired", visibility=["read", "create", "update", "delete", "query"]
    )
    """Whether this attribute is required."""

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        value: Optional[str] = None,
        is_required: Optional[bool] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogModelPlatformDomain(_Model):
    """Catalog model platform domain.

    :ivar name: The name of the platform domain.
    :vartype name: str
    :ivar friendly_name: The friendly name of the platform domain.
    :vartype friendly_name: str
    :ivar related_collections: The related collections of the platform domain.
    :vartype related_collections: list[~purviewunifiedcatalog.models.CatalogModelRelatedCollection]
    """

    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name of the platform domain."""
    friendly_name: Optional[str] = rest_field(
        name="friendlyName", visibility=["read", "create", "update", "delete", "query"]
    )
    """The friendly name of the platform domain."""
    related_collections: Optional[list["_models.CatalogModelRelatedCollection"]] = rest_field(
        name="relatedCollections", visibility=["read", "create", "update", "delete", "query"]
    )
    """The related collections of the platform domain."""

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        friendly_name: Optional[str] = None,
        related_collections: Optional[list["_models.CatalogModelRelatedCollection"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogModelRelatedCollection(_Model):
    """Catalog model related collection.

    :ivar name: The name of the related collection.
    :vartype name: str
    :ivar friendly_name: The friendly name of the related collection.
    :vartype friendly_name: str
    :ivar parent_collection: The parent collection of the related collection.
    :vartype parent_collection:
     ~purviewunifiedcatalog.models.CatalogModelRelatedCollectionParentCollection
    """

    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name of the related collection."""
    friendly_name: Optional[str] = rest_field(
        name="friendlyName", visibility=["read", "create", "update", "delete", "query"]
    )
    """The friendly name of the related collection."""
    parent_collection: Optional["_models.CatalogModelRelatedCollectionParentCollection"] = rest_field(
        name="parentCollection", visibility=["read", "create", "update", "delete", "query"]
    )
    """The parent collection of the related collection."""

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        friendly_name: Optional[str] = None,
        parent_collection: Optional["_models.CatalogModelRelatedCollectionParentCollection"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogModelRelatedCollectionParentCollection(_Model):  # pylint: disable=name-too-long
    """Catalog model related collection parent collection.

    :ivar type: The type of the parent collection. "CollectionReference"
    :vartype type: str or ~purviewunifiedcatalog.models.RelatedCollectionParentCollectionTypeEnum
    :ivar ref_name: The reference name of the parent collection.
    :vartype ref_name: str
    """

    type: Optional[Union[str, "_models.RelatedCollectionParentCollectionTypeEnum"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The type of the parent collection. \"CollectionReference\""""
    ref_name: Optional[str] = rest_field(name="refName", visibility=["read", "create", "update", "delete", "query"])
    """The reference name of the parent collection."""

    @overload
    def __init__(
        self,
        *,
        type: Optional[Union[str, "_models.RelatedCollectionParentCollectionTypeEnum"]] = None,
        ref_name: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogModelSystemDataWithExpired(_Model):
    """System metadata with expiration information for catalog entities.

    :ivar provisioning_state: The provisioning state of the record. ex: softdeleted. Known values
     are: "Unknown", "Succeeded", and "SoftDeleted".
    :vartype provisioning_state: str or ~purviewunifiedcatalog.models.DataAssetProvisioningState
    :ivar created_at: The timestamp when the record was created.
    :vartype created_at: ~datetime.datetime
    :ivar created_by: The unique identifier of the user who created the record.
    :vartype created_by: str
    :ivar last_modified_at: The timestamp when the record was last modified.
    :vartype last_modified_at: ~datetime.datetime
    :ivar last_modified_by: The unique identifier of the user who last modified the record.
    :vartype last_modified_by: str
    :ivar expired_at: The timestamp when the record expires.
    :vartype expired_at: ~datetime.datetime
    :ivar expired_by: The unique identifier of the user who expired the record.
    :vartype expired_by: str
    """

    provisioning_state: Optional[Union[str, "_models.DataAssetProvisioningState"]] = rest_field(
        name="provisioningState", visibility=["read", "create", "update", "delete", "query"]
    )
    """The provisioning state of the record. ex: softdeleted. Known values are: \"Unknown\",
     \"Succeeded\", and \"SoftDeleted\"."""
    created_at: Optional[datetime.datetime] = rest_field(
        name="createdAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The timestamp when the record was created."""
    created_by: Optional[str] = rest_field(name="createdBy", visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the user who created the record."""
    last_modified_at: Optional[datetime.datetime] = rest_field(
        name="lastModifiedAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The timestamp when the record was last modified."""
    last_modified_by: Optional[str] = rest_field(
        name="lastModifiedBy", visibility=["read", "create", "update", "delete", "query"]
    )
    """The unique identifier of the user who last modified the record."""
    expired_at: Optional[datetime.datetime] = rest_field(
        name="expiredAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The timestamp when the record expires."""
    expired_by: Optional[str] = rest_field(name="expiredBy", visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the user who expired the record."""

    @overload
    def __init__(
        self,
        *,
        provisioning_state: Optional[Union[str, "_models.DataAssetProvisioningState"]] = None,
        created_at: Optional[datetime.datetime] = None,
        created_by: Optional[str] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        expired_at: Optional[datetime.datetime] = None,
        expired_by: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogModelTermResource(_Model):
    """Catalog model term resource.

    :ivar name: The name of the resource.
    :vartype name: str
    :ivar url: The URL of the resource.
    :vartype url: str
    """

    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name of the resource."""
    url: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The URL of the resource."""

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        url: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogProperties(_Model):
    """CatalogProperties.

    :ivar description: The description of the catalog.
    :vartype description: str
    :ivar decision_rules: The type of the catalog.
    :vartype decision_rules: list[~purviewunifiedcatalog.models.DecisionRule]
    :ivar attribute_rules: The attribute rules of the catalog.
    :vartype attribute_rules: list[~purviewunifiedcatalog.models.AttributeRule]
    :ivar entity: The entity reference of the catalog. Required.
    :vartype entity: ~purviewunifiedcatalog.models.EntityReference
    :ivar parent_entity_name: The parent entity name of the catalog.
    :vartype parent_entity_name: str
    """

    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The description of the catalog."""
    decision_rules: Optional[list["_models.DecisionRule"]] = rest_field(
        name="decisionRules", visibility=["read", "create", "update", "delete", "query"]
    )
    """The type of the catalog."""
    attribute_rules: Optional[list["_models.AttributeRule"]] = rest_field(
        name="attributeRules", visibility=["read", "create", "update", "delete", "query"]
    )
    """The attribute rules of the catalog."""
    entity: "_models.EntityReference" = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The entity reference of the catalog. Required."""
    parent_entity_name: Optional[str] = rest_field(
        name="parentEntityName", visibility=["read", "create", "update", "delete", "query"]
    )
    """The parent entity name of the catalog."""

    @overload
    def __init__(
        self,
        *,
        entity: "_models.EntityReference",
        description: Optional[str] = None,
        decision_rules: Optional[list["_models.DecisionRule"]] = None,
        attribute_rules: Optional[list["_models.AttributeRule"]] = None,
        parent_entity_name: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogResponse(_Model):
    """CatalogResponse.

    :ivar values_property: The list of catalog values. Required.
    :vartype values_property: list[~purviewunifiedcatalog.models.CatalogValue]
    :ivar skip_token: The continuation token for pagination.
    :vartype skip_token: str
    """

    values_property: list["_models.CatalogValue"] = rest_field(
        name="values", visibility=["read", "create", "update", "delete", "query"], original_tsp_name="values"
    )
    """The list of catalog values. Required."""
    skip_token: Optional[str] = rest_field(name="skipToken", visibility=["read", "create", "update", "delete", "query"])
    """The continuation token for pagination."""

    @overload
    def __init__(
        self,
        *,
        values_property: list["_models.CatalogValue"],
        skip_token: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CatalogValue(_Model):
    """CatalogValue.

    :ivar name: The name of the catalog. Required.
    :vartype name: str
    :ivar id: The unique identifier of the catalog. Required.
    :vartype id: str
    :ivar version: The version of the catalog. Required.
    :vartype version: int
    :ivar properties: The properties of the catalog. Required.
    :vartype properties: ~purviewunifiedcatalog.models.CatalogProperties
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name of the catalog. Required."""
    id: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the catalog. Required."""
    version: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The version of the catalog. Required."""
    properties: "_models.CatalogProperties" = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The properties of the catalog. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        id: str,  # pylint: disable=redefined-builtin
        version: int,
        properties: "_models.CatalogProperties",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CdeRelationship(_Model):
    """Relationship information between entities.

    :ivar relationship_type: Type of the relationship.
    :vartype relationship_type: str
    :ivar entity_id: Unique identifier of the related entity. Required.
    :vartype entity_id: str
    """

    relationship_type: Optional[str] = rest_field(
        name="relationshipType", visibility=["read", "create", "update", "delete", "query"]
    )
    """Type of the relationship."""
    entity_id: str = rest_field(name="entityId", visibility=["create"])
    """Unique identifier of the related entity. Required."""

    @overload
    def __init__(
        self,
        *,
        entity_id: str,
        relationship_type: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CdeRelationshipWithSystemData(_Model):
    """CDC Relationship information between entities.

    :ivar system_data: System metadata for the relationship.
    :vartype system_data: ~purviewunifiedcatalog.models.SystemData
    :ivar description: Description of the relationship.
    :vartype description: str
    :ivar relationship_type: Type of the relationship.
    :vartype relationship_type: str
    :ivar entity_id: Unique identifier of the related entity. Required.
    :vartype entity_id: str
    """

    system_data: Optional["_models.SystemData"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """System metadata for the relationship."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Description of the relationship."""
    relationship_type: Optional[str] = rest_field(
        name="relationshipType", visibility=["read", "create", "update", "delete", "query"]
    )
    """Type of the relationship."""
    entity_id: str = rest_field(name="entityId", visibility=["create"])
    """Unique identifier of the related entity. Required."""

    @overload
    def __init__(
        self,
        *,
        entity_id: str,
        system_data: Optional["_models.SystemData"] = None,
        description: Optional[str] = None,
        relationship_type: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Condition(_Model):
    """Condition.

    :ivar attribute_name: The name of the attribute. Required.
    :vartype attribute_name: str
    :ivar attribute_value_includes: The operator of the condition.
    :vartype attribute_value_includes: str
    :ivar attribute_value_included_in: The values included in the condition.
    :vartype attribute_value_included_in: list[str]
    :ivar from_rule: The rule from which the condition is derived.
    :vartype from_rule: str
    """

    attribute_name: str = rest_field(name="attributeName", visibility=["read", "create", "update", "delete", "query"])
    """The name of the attribute. Required."""
    attribute_value_includes: Optional[str] = rest_field(
        name="attributeValueIncludes", visibility=["read", "create", "update", "delete", "query"]
    )
    """The operator of the condition."""
    attribute_value_included_in: Optional[list[str]] = rest_field(
        name="attributeValueIncludedIn", visibility=["read", "create", "update", "delete", "query"]
    )
    """The values included in the condition."""
    from_rule: Optional[str] = rest_field(name="fromRule", visibility=["read", "create", "update", "delete", "query"])
    """The rule from which the condition is derived."""

    @overload
    def __init__(
        self,
        *,
        attribute_name: str,
        attribute_value_includes: Optional[str] = None,
        attribute_value_included_in: Optional[list[str]] = None,
        from_rule: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ContactsMap(_Model):
    """A dictionary of contact lists keyed by contact type (e.g., 'Owner', 'Expert').

    :ivar owner: List of owner contacts.
    :vartype owner: list[~purviewunifiedcatalog.models.CatalogModelContactsValueInner]
    :ivar expert: List of expert contacts.
    :vartype expert: list[~purviewunifiedcatalog.models.CatalogModelContactsValueInner]
    :ivar database_admin: List of database administrator contacts.
    :vartype database_admin: list[~purviewunifiedcatalog.models.CatalogModelContactsValueInner]
    """

    owner: Optional[list["_models.CatalogModelContactsValueInner"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """List of owner contacts."""
    expert: Optional[list["_models.CatalogModelContactsValueInner"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """List of expert contacts."""
    database_admin: Optional[list["_models.CatalogModelContactsValueInner"]] = rest_field(
        name="databaseAdmin", visibility=["read", "create", "update", "delete", "query"]
    )
    """List of database administrator contacts."""

    @overload
    def __init__(
        self,
        *,
        owner: Optional[list["_models.CatalogModelContactsValueInner"]] = None,
        expert: Optional[list["_models.CatalogModelContactsValueInner"]] = None,
        database_admin: Optional[list["_models.CatalogModelContactsValueInner"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CriticalDataElement(_Model):
    """Represents a critical data element in the catalog with metadata and relationships.

    :ivar status: The current status of the critical data element. Known values are: "DRAFT",
     "PUBLISHED", and "EXPIRED".
    :vartype status: str or ~purviewunifiedcatalog.models.CatalogModelStatus
    :ivar data_type: The data type of the critical data element. Known values are: "TEXT",
     "NUMBER", "DATETIME", and "BOOLEAN".
    :vartype data_type: str or
     ~purviewunifiedcatalog.models.CatalogModelCriticalDataElementDataTypeEnum
    :ivar id: The unique identifier of the critical data element. Required.
    :vartype id: str
    :ivar name: The name of the critical data element.
    :vartype name: str
    :ivar system_data: System metadata including creation and modification information.
    :vartype system_data: ~purviewunifiedcatalog.models.CatalogModelSystemDataWithExpired
    :ivar domain: The unique identifier of the domain this element belongs to.
    :vartype domain: str
    :ivar description: A detailed description of the critical data element.
    :vartype description: str
    :ivar contacts: The contacts associated with this critical data element.
    :vartype contacts: ~purviewunifiedcatalog.models.ContactsMap
    :ivar managed_attributes: Managed attributes associated with this critical data element.
    :vartype managed_attributes: list[~purviewunifiedcatalog.models.CatalogModelManagedAttribute]
    """

    status: Optional[Union[str, "_models.CatalogModelStatus"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The current status of the critical data element. Known values are: \"DRAFT\", \"PUBLISHED\",
     and \"EXPIRED\"."""
    data_type: Optional[Union[str, "_models.CatalogModelCriticalDataElementDataTypeEnum"]] = rest_field(
        name="dataType", visibility=["read", "create", "update", "delete", "query"]
    )
    """The data type of the critical data element. Known values are: \"TEXT\", \"NUMBER\",
     \"DATETIME\", and \"BOOLEAN\"."""
    id: str = rest_field(visibility=["create"])
    """The unique identifier of the critical data element. Required."""
    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name of the critical data element."""
    system_data: Optional["_models.CatalogModelSystemDataWithExpired"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """System metadata including creation and modification information."""
    domain: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the domain this element belongs to."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """A detailed description of the critical data element."""
    contacts: Optional["_models.ContactsMap"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The contacts associated with this critical data element."""
    managed_attributes: Optional[list["_models.CatalogModelManagedAttribute"]] = rest_field(
        name="managedAttributes", visibility=["read", "create", "update", "delete", "query"]
    )
    """Managed attributes associated with this critical data element."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        status: Optional[Union[str, "_models.CatalogModelStatus"]] = None,
        data_type: Optional[Union[str, "_models.CatalogModelCriticalDataElementDataTypeEnum"]] = None,
        name: Optional[str] = None,
        system_data: Optional["_models.CatalogModelSystemDataWithExpired"] = None,
        domain: Optional[str] = None,
        description: Optional[str] = None,
        contacts: Optional["_models.ContactsMap"] = None,
        managed_attributes: Optional[list["_models.CatalogModelManagedAttribute"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CriticalDataElementFacetRequest(_Model):
    """CriticalDataElementFacetRequest.

    :ivar ids: To filter by Ids.
    :vartype ids: list[str]
    :ivar domain_ids: To filter by domain Ids.
    :vartype domain_ids: list[str]
    :ivar name_keyword: To filter by name keyword.
    :vartype name_keyword: str
    :ivar owners: To filter by owners.
    :vartype owners: list[str]
    :ivar status: To filter by status. Known values are: "Draft", "Published", and "Expired".
    :vartype status: str or ~purviewunifiedcatalog.models.SharedEntityStatus
    :ivar multi_status: To filter by multiple status.
    :vartype multi_status: list[str or ~purviewunifiedcatalog.models.SharedEntityStatus]
    :ivar facets: To filter by multiple facets.
    :vartype facets: list[~purviewunifiedcatalog.models.ModelsFacetRequestObject]
    """

    ids: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by Ids."""
    domain_ids: Optional[list[str]] = rest_field(
        name="domainIds", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by domain Ids."""
    name_keyword: Optional[str] = rest_field(
        name="nameKeyword", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by name keyword."""
    owners: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by owners."""
    status: Optional[Union[str, "_models.SharedEntityStatus"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by status. Known values are: \"Draft\", \"Published\", and \"Expired\"."""
    multi_status: Optional[list[Union[str, "_models.SharedEntityStatus"]]] = rest_field(
        name="multiStatus", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by multiple status."""
    facets: Optional[list["_models.ModelsFacetRequestObject"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by multiple facets."""

    @overload
    def __init__(
        self,
        *,
        ids: Optional[list[str]] = None,
        domain_ids: Optional[list[str]] = None,
        name_keyword: Optional[str] = None,
        owners: Optional[list[str]] = None,
        status: Optional[Union[str, "_models.SharedEntityStatus"]] = None,
        multi_status: Optional[list[Union[str, "_models.SharedEntityStatus"]]] = None,
        facets: Optional[list["_models.ModelsFacetRequestObject"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CriticalDataElementProperties(_Model):
    """Properties for critical data element relationships.

    :ivar system_data: System metadata for the relationship.
    :vartype system_data: ~purviewunifiedcatalog.models.SystemData
    :ivar description: Description of the relationship.
    :vartype description: str
    :ivar relationship_type: Type of the relationship.
    :vartype relationship_type: str
    :ivar asset_id: Unique identifier of the associated asset.
    :vartype asset_id: str
    :ivar entity_id: Name of the associated asset. Required.
    :vartype entity_id: str
    """

    system_data: Optional["_models.SystemData"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """System metadata for the relationship."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Description of the relationship."""
    relationship_type: Optional[str] = rest_field(
        name="relationshipType", visibility=["read", "create", "update", "delete", "query"]
    )
    """Type of the relationship."""
    asset_id: Optional[str] = rest_field(name="assetId", visibility=["read", "create", "update", "delete", "query"])
    """Unique identifier of the associated asset."""
    entity_id: str = rest_field(name="entityId", visibility=["read", "create", "update", "delete", "query"])
    """Name of the associated asset. Required."""

    @overload
    def __init__(
        self,
        *,
        entity_id: str,
        system_data: Optional["_models.SystemData"] = None,
        description: Optional[str] = None,
        relationship_type: Optional[str] = None,
        asset_id: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CriticalDataElementQueryRequest(_Model):
    """Request parameters for querying critical data elements.

    :ivar skip: Number of items to skip.
    :vartype skip: int
    :ivar top: Number of items to return.
    :vartype top: int
    :ivar orderby: Ordering criteria for the results.
    :vartype orderby: list[~purviewunifiedcatalog.models.CatalogApiServiceOrderBy]
    :ivar ids: To filter by Ids.
    :vartype ids: list[str]
    :ivar domain_ids: To filter by domain Ids.
    :vartype domain_ids: list[str]
    :ivar name_keyword: To filter by name keyword.
    :vartype name_keyword: str
    :ivar owners: To filter by owners.
    :vartype owners: list[str]
    :ivar status: To filter by status. Known values are: "Draft", "Published", and "Expired".
    :vartype status: str or ~purviewunifiedcatalog.models.SharedEntityStatus
    :ivar multi_status: To filter by multiple status.
    :vartype multi_status: list[str or ~purviewunifiedcatalog.models.SharedEntityStatus]
    :ivar managed_attributes: To filter by managed attributes.
    :vartype managed_attributes:
     list[~purviewunifiedcatalog.models.SharedSearchManageAttributeSearchFilter]
    """

    skip: Optional[int] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Number of items to skip."""
    top: Optional[int] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Number of items to return."""
    orderby: Optional[list["_models.CatalogApiServiceOrderBy"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Ordering criteria for the results."""
    ids: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by Ids."""
    domain_ids: Optional[list[str]] = rest_field(
        name="domainIds", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by domain Ids."""
    name_keyword: Optional[str] = rest_field(
        name="nameKeyword", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by name keyword."""
    owners: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by owners."""
    status: Optional[Union[str, "_models.SharedEntityStatus"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by status. Known values are: \"Draft\", \"Published\", and \"Expired\"."""
    multi_status: Optional[list[Union[str, "_models.SharedEntityStatus"]]] = rest_field(
        name="multiStatus", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by multiple status."""
    managed_attributes: Optional[list["_models.SharedSearchManageAttributeSearchFilter"]] = rest_field(
        name="managedAttributes", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by managed attributes."""

    @overload
    def __init__(
        self,
        *,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        orderby: Optional[list["_models.CatalogApiServiceOrderBy"]] = None,
        ids: Optional[list[str]] = None,
        domain_ids: Optional[list[str]] = None,
        name_keyword: Optional[str] = None,
        owners: Optional[list[str]] = None,
        status: Optional[Union[str, "_models.SharedEntityStatus"]] = None,
        multi_status: Optional[list[Union[str, "_models.SharedEntityStatus"]]] = None,
        managed_attributes: Optional[list["_models.SharedSearchManageAttributeSearchFilter"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CriticalDataElementRelationshipRequest(_Model):
    """Request body for creating relationships with critical data element properties."""


class DataAsset(_Model):
    """DataAsset.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    DataAssetAdlsGen2Path, DataAssetAzureSqlTable, DataAssetGeneral

    :ivar id: The data asset identifier. Required.
    :vartype id: str
    :ivar name: Name of the data asset. Required.
    :vartype name: str
    :ivar system_data: System data associated with the asset.
    :vartype system_data: ~purviewunifiedcatalog.models.DataAssetSystemData
    :ivar description: A description about the relationship.
    :vartype description: str
    :ivar source: Source of the asset.
    :vartype source: ~purviewunifiedcatalog.models.CatalogModelDataAssetSource
    :ivar contacts: Contacts associated with the asset.
    :vartype contacts: ~purviewunifiedcatalog.models.ContactsMap
    :ivar classifications: A list of classification labels.
    :vartype classifications: list[str]
    :ivar type: Type of the data asset. Required. Known values are: "AzureSqlTable",
     "ADLSGen2Path", and "General".
    :vartype type: str or ~purviewunifiedcatalog.models.DataAssetType
    :ivar schema: Schema of the asset.
    :vartype schema: list[~purviewunifiedcatalog.models.CatalogModelDataAssetSchema]
    :ivar open_in_url: A redirection link.
    :vartype open_in_url: str
    """

    __mapping__: dict[str, _Model] = {}
    id: str = rest_field(visibility=["create"])
    """The data asset identifier. Required."""
    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Name of the data asset. Required."""
    system_data: Optional["_models.DataAssetSystemData"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """System data associated with the asset."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """A description about the relationship."""
    source: Optional["_models.CatalogModelDataAssetSource"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Source of the asset."""
    contacts: Optional["_models.ContactsMap"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Contacts associated with the asset."""
    classifications: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """A list of classification labels."""
    type: str = rest_discriminator(name="type", visibility=["read", "create", "update", "delete", "query"])
    """Type of the data asset. Required. Known values are: \"AzureSqlTable\", \"ADLSGen2Path\", and
     \"General\"."""
    schema: Optional[list["_models.CatalogModelDataAssetSchema"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Schema of the asset."""
    open_in_url: Optional[str] = rest_field(
        name="openInUrl", visibility=["read", "create", "update", "delete", "query"]
    )
    """A redirection link."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        name: str,
        type: str,
        system_data: Optional["_models.DataAssetSystemData"] = None,
        description: Optional[str] = None,
        source: Optional["_models.CatalogModelDataAssetSource"] = None,
        contacts: Optional["_models.ContactsMap"] = None,
        classifications: Optional[list[str]] = None,
        schema: Optional[list["_models.CatalogModelDataAssetSchema"]] = None,
        open_in_url: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataAssetAdlsGen2Path(DataAsset, discriminator="ADLSGen2Path"):
    """Data asset of type ADLS Gen2 Path.

    :ivar id: The data asset identifier. Required.
    :vartype id: str
    :ivar name: Name of the data asset. Required.
    :vartype name: str
    :ivar system_data: System data associated with the asset.
    :vartype system_data: ~purviewunifiedcatalog.models.DataAssetSystemData
    :ivar description: A description about the relationship.
    :vartype description: str
    :ivar source: Source of the asset.
    :vartype source: ~purviewunifiedcatalog.models.CatalogModelDataAssetSource
    :ivar contacts: Contacts associated with the asset.
    :vartype contacts: ~purviewunifiedcatalog.models.ContactsMap
    :ivar classifications: A list of classification labels.
    :vartype classifications: list[str]
    :ivar schema: Schema of the asset.
    :vartype schema: list[~purviewunifiedcatalog.models.CatalogModelDataAssetSchema]
    :ivar open_in_url: A redirection link.
    :vartype open_in_url: str
    :ivar type: Type of the data asset. Required. ADLS Gen2 Path data asset type.
    :vartype type: str or ~purviewunifiedcatalog.models.ADLS_GEN2_PATH
    :ivar type_properties: Type properties of the ADLS Gen2 path asset.
    :vartype type_properties: ~purviewunifiedcatalog.models.DataAssetAdlsGen2PathTypeProperties
    """

    type: Literal[DataAssetType.ADLS_GEN2_PATH] = rest_discriminator(name="type", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Type of the data asset. Required. ADLS Gen2 Path data asset type."""
    type_properties: Optional["_models.DataAssetAdlsGen2PathTypeProperties"] = rest_field(
        name="typeProperties", visibility=["read", "create", "update", "delete", "query"]
    )
    """Type properties of the ADLS Gen2 path asset."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        name: str,
        system_data: Optional["_models.DataAssetSystemData"] = None,
        description: Optional[str] = None,
        source: Optional["_models.CatalogModelDataAssetSource"] = None,
        contacts: Optional["_models.ContactsMap"] = None,
        classifications: Optional[list[str]] = None,
        schema: Optional[list["_models.CatalogModelDataAssetSchema"]] = None,
        open_in_url: Optional[str] = None,
        type_properties: Optional["_models.DataAssetAdlsGen2PathTypeProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.type = DataAssetType.ADLS_GEN2_PATH  # type: ignore


class DataAssetAdlsGen2PathTypeProperties(_Model):
    """Type properties for an ADLS Gen2 path data asset.

    :ivar server_endpoint: The server endpoint of the ADLS Gen2 path.
    :vartype server_endpoint: str
    :ivar container: The container name of the ADLS Gen2 path.
    :vartype container: str
    :ivar folder_path: The folder path of the ADLS Gen2 path.
    :vartype folder_path: str
    :ivar file_name: The file name of the ADLS Gen2 path.
    :vartype file_name: str
    """

    server_endpoint: Optional[str] = rest_field(
        name="serverEndpoint", visibility=["read", "create", "update", "delete", "query"]
    )
    """The server endpoint of the ADLS Gen2 path."""
    container: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The container name of the ADLS Gen2 path."""
    folder_path: Optional[str] = rest_field(
        name="folderPath", visibility=["read", "create", "update", "delete", "query"]
    )
    """The folder path of the ADLS Gen2 path."""
    file_name: Optional[str] = rest_field(name="fileName", visibility=["read", "create", "update", "delete", "query"])
    """The file name of the ADLS Gen2 path."""

    @overload
    def __init__(
        self,
        *,
        server_endpoint: Optional[str] = None,
        container: Optional[str] = None,
        folder_path: Optional[str] = None,
        file_name: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataAssetAzureSqlTable(DataAsset, discriminator="AzureSqlTable"):
    """Data asset of type Azure SQL Table.

    :ivar id: The data asset identifier. Required.
    :vartype id: str
    :ivar name: Name of the data asset. Required.
    :vartype name: str
    :ivar system_data: System data associated with the asset.
    :vartype system_data: ~purviewunifiedcatalog.models.DataAssetSystemData
    :ivar description: A description about the relationship.
    :vartype description: str
    :ivar source: Source of the asset.
    :vartype source: ~purviewunifiedcatalog.models.CatalogModelDataAssetSource
    :ivar contacts: Contacts associated with the asset.
    :vartype contacts: ~purviewunifiedcatalog.models.ContactsMap
    :ivar classifications: A list of classification labels.
    :vartype classifications: list[str]
    :ivar schema: Schema of the asset.
    :vartype schema: list[~purviewunifiedcatalog.models.CatalogModelDataAssetSchema]
    :ivar open_in_url: A redirection link.
    :vartype open_in_url: str
    :ivar type: Type of the data asset. Required. Azure SQL Table data asset type.
    :vartype type: str or ~purviewunifiedcatalog.models.AZURE_SQL_TABLE
    :ivar type_properties: Type properties of the Azure SQL table asset.
    :vartype type_properties: ~purviewunifiedcatalog.models.DataAssetAzureSqlTableTypeProperties
    """

    type: Literal[DataAssetType.AZURE_SQL_TABLE] = rest_discriminator(name="type", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Type of the data asset. Required. Azure SQL Table data asset type."""
    type_properties: Optional["_models.DataAssetAzureSqlTableTypeProperties"] = rest_field(
        name="typeProperties", visibility=["read", "create", "update", "delete", "query"]
    )
    """Type properties of the Azure SQL table asset."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        name: str,
        system_data: Optional["_models.DataAssetSystemData"] = None,
        description: Optional[str] = None,
        source: Optional["_models.CatalogModelDataAssetSource"] = None,
        contacts: Optional["_models.ContactsMap"] = None,
        classifications: Optional[list[str]] = None,
        schema: Optional[list["_models.CatalogModelDataAssetSchema"]] = None,
        open_in_url: Optional[str] = None,
        type_properties: Optional["_models.DataAssetAzureSqlTableTypeProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.type = DataAssetType.AZURE_SQL_TABLE  # type: ignore


class DataAssetAzureSqlTableTypeProperties(_Model):
    """Type properties for an Azure SQL table data asset.

    :ivar format: The format of the sql table. Known values are: "Table" and "View".
    :vartype format: str or ~purviewunifiedcatalog.models.TypePropertiesFormat
    :ivar server_endpoint: The server endpoint of the sql table.
    :vartype server_endpoint: str
    :ivar database_name: The database name of the sql table.
    :vartype database_name: str
    :ivar schema_name: The schema name of the sql table.
    :vartype schema_name: str
    :ivar table_name: The table name of the sql table.
    :vartype table_name: str
    """

    format: Optional[Union[str, "_models.TypePropertiesFormat"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The format of the sql table. Known values are: \"Table\" and \"View\"."""
    server_endpoint: Optional[str] = rest_field(
        name="serverEndpoint", visibility=["read", "create", "update", "delete", "query"]
    )
    """The server endpoint of the sql table."""
    database_name: Optional[str] = rest_field(
        name="databaseName", visibility=["read", "create", "update", "delete", "query"]
    )
    """The database name of the sql table."""
    schema_name: Optional[str] = rest_field(
        name="schemaName", visibility=["read", "create", "update", "delete", "query"]
    )
    """The schema name of the sql table."""
    table_name: Optional[str] = rest_field(name="tableName", visibility=["read", "create", "update", "delete", "query"])
    """The table name of the sql table."""

    @overload
    def __init__(
        self,
        *,
        format: Optional[Union[str, "_models.TypePropertiesFormat"]] = None,
        server_endpoint: Optional[str] = None,
        database_name: Optional[str] = None,
        schema_name: Optional[str] = None,
        table_name: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataAssetGeneral(DataAsset, discriminator="General"):
    """Data asset of type General.

    :ivar id: The data asset identifier. Required.
    :vartype id: str
    :ivar name: Name of the data asset. Required.
    :vartype name: str
    :ivar system_data: System data associated with the asset.
    :vartype system_data: ~purviewunifiedcatalog.models.DataAssetSystemData
    :ivar description: A description about the relationship.
    :vartype description: str
    :ivar source: Source of the asset.
    :vartype source: ~purviewunifiedcatalog.models.CatalogModelDataAssetSource
    :ivar contacts: Contacts associated with the asset.
    :vartype contacts: ~purviewunifiedcatalog.models.ContactsMap
    :ivar classifications: A list of classification labels.
    :vartype classifications: list[str]
    :ivar schema: Schema of the asset.
    :vartype schema: list[~purviewunifiedcatalog.models.CatalogModelDataAssetSchema]
    :ivar open_in_url: A redirection link.
    :vartype open_in_url: str
    :ivar type: Type of the data asset. Required. General data asset type.
    :vartype type: str or ~purviewunifiedcatalog.models.GENERAL
    """

    type: Literal[DataAssetType.GENERAL] = rest_discriminator(name="type", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Type of the data asset. Required. General data asset type."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        name: str,
        system_data: Optional["_models.DataAssetSystemData"] = None,
        description: Optional[str] = None,
        source: Optional["_models.CatalogModelDataAssetSource"] = None,
        contacts: Optional["_models.ContactsMap"] = None,
        classifications: Optional[list[str]] = None,
        schema: Optional[list["_models.CatalogModelDataAssetSchema"]] = None,
        open_in_url: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.type = DataAssetType.GENERAL  # type: ignore


class DataAssetQueryRequest(_Model):
    """DataAssetQueryRequest.

    :ivar ids: To filter by Ids.
    :vartype ids: list[str]
    :ivar name_keyword: To filter by name keyword.
    :vartype name_keyword: str
    :ivar owners: To filter by owners.
    :vartype owners: list[str]
    :ivar source_asset_ids: To filter by data map asset Ids.
    :vartype source_asset_ids: list[str]
    :ivar asset_types: To filter by data map asset types.
    :vartype asset_types: list[str]
    :ivar including_orphans: To filter by status.
    :vartype including_orphans: bool
    """

    ids: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by Ids."""
    name_keyword: Optional[str] = rest_field(
        name="nameKeyword", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by name keyword."""
    owners: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by owners."""
    source_asset_ids: Optional[list[str]] = rest_field(
        name="sourceAssetIds", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by data map asset Ids."""
    asset_types: Optional[list[str]] = rest_field(
        name="assetTypes", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by data map asset types."""
    including_orphans: Optional[bool] = rest_field(
        name="includingOrphans", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by status."""

    @overload
    def __init__(
        self,
        *,
        ids: Optional[list[str]] = None,
        name_keyword: Optional[str] = None,
        owners: Optional[list[str]] = None,
        source_asset_ids: Optional[list[str]] = None,
        asset_types: Optional[list[str]] = None,
        including_orphans: Optional[bool] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataAssetRelationship(_Model):
    """Properties for data asset relationships.

    :ivar description: Description of the relationship.
    :vartype description: str
    :ivar relationship_type: Type of the relationship. Known values are: "Related" and "Synonym".
    :vartype relationship_type: str or ~purviewunifiedcatalog.models.DataAssetRelationshipType
    :ivar entity_id: Name of the associated entity. ex:dataproduct id. Required.
    :vartype entity_id: str
    """

    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Description of the relationship."""
    relationship_type: Optional[Union[str, "_models.DataAssetRelationshipType"]] = rest_field(
        name="relationshipType", visibility=["read", "create", "update", "delete", "query"]
    )
    """Type of the relationship. Known values are: \"Related\" and \"Synonym\"."""
    entity_id: str = rest_field(name="entityId", visibility=["create"])
    """Name of the associated entity. ex:dataproduct id. Required."""

    @overload
    def __init__(
        self,
        *,
        entity_id: str,
        description: Optional[str] = None,
        relationship_type: Optional[Union[str, "_models.DataAssetRelationshipType"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataAssetRequest(_Model):
    """DataAsset.

    :ivar source: Source of the asset.
    :vartype source: ~purviewunifiedcatalog.models.CatalogModelDataAssetSourceRequest
    :ivar contacts: Contacts associated with the asset.
    :vartype contacts: ~purviewunifiedcatalog.models.ContactsMap
    :ivar open_in_url: A redirection link.
    :vartype open_in_url: str
    """

    source: Optional["_models.CatalogModelDataAssetSourceRequest"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Source of the asset."""
    contacts: Optional["_models.ContactsMap"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Contacts associated with the asset."""
    open_in_url: Optional[str] = rest_field(
        name="openInUrl", visibility=["read", "create", "update", "delete", "query"]
    )
    """A redirection link."""

    @overload
    def __init__(
        self,
        *,
        source: Optional["_models.CatalogModelDataAssetSourceRequest"] = None,
        contacts: Optional["_models.ContactsMap"] = None,
        open_in_url: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataAssetSystemData(_Model):
    """System metadata with expiration information for data assets.

    :ivar provisioning_state: The provisioning state of the record. Known values are: "Unknown",
     "Succeeded", and "SoftDeleted".
    :vartype provisioning_state: str or ~purviewunifiedcatalog.models.DataAssetProvisioningState
    :ivar created_at: The timestamp when the record was created.
    :vartype created_at: ~datetime.datetime
    :ivar created_by: The unique identifier of the user who created the record.
    :vartype created_by: str
    :ivar last_modified_at: The timestamp when the record was last modified.
    :vartype last_modified_at: ~datetime.datetime
    :ivar last_modified_by: The unique identifier of the user who last modified the record.
    :vartype last_modified_by: str
    :ivar expired_at: The timestamp when the record expires.
    :vartype expired_at: ~datetime.datetime
    :ivar expired_by: The unique identifier of the user who expired the record.
    :vartype expired_by: str
    """

    provisioning_state: Optional[Union[str, "_models.DataAssetProvisioningState"]] = rest_field(
        name="provisioningState", visibility=["read", "create", "update", "delete", "query"]
    )
    """The provisioning state of the record. Known values are: \"Unknown\", \"Succeeded\", and
     \"SoftDeleted\"."""
    created_at: Optional[datetime.datetime] = rest_field(
        name="createdAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The timestamp when the record was created."""
    created_by: Optional[str] = rest_field(name="createdBy", visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the user who created the record."""
    last_modified_at: Optional[datetime.datetime] = rest_field(
        name="lastModifiedAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The timestamp when the record was last modified."""
    last_modified_by: Optional[str] = rest_field(
        name="lastModifiedBy", visibility=["read", "create", "update", "delete", "query"]
    )
    """The unique identifier of the user who last modified the record."""
    expired_at: Optional[datetime.datetime] = rest_field(
        name="expiredAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The timestamp when the record expires."""
    expired_by: Optional[str] = rest_field(name="expiredBy", visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the user who expired the record."""

    @overload
    def __init__(
        self,
        *,
        provisioning_state: Optional[Union[str, "_models.DataAssetProvisioningState"]] = None,
        created_at: Optional[datetime.datetime] = None,
        created_by: Optional[str] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        expired_at: Optional[datetime.datetime] = None,
        expired_by: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataAssetWithLineage(_Model):
    """Data asset model that includes lineage details for GetById responses.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    DataAssetWithLineageAdlsGen2Path, DataAssetWithLineageAzureSqlTable,
    DataAssetWithLineageGeneral

    :ivar id: The data asset identifier. Required.
    :vartype id: str
    :ivar name: Name of the data asset. Required.
    :vartype name: str
    :ivar system_data: System data associated with the asset.
    :vartype system_data: ~purviewunifiedcatalog.models.DataAssetSystemData
    :ivar description: A description about the relationship.
    :vartype description: str
    :ivar source: Source of the asset.
    :vartype source: ~purviewunifiedcatalog.models.CatalogModelDataAssetSource
    :ivar contacts: Contacts associated with the asset.
    :vartype contacts: ~purviewunifiedcatalog.models.ContactsMap
    :ivar classifications: A list of classification labels.
    :vartype classifications: list[str]
    :ivar type: Type of the data asset. Required. Known values are: "AzureSqlTable",
     "ADLSGen2Path", and "General".
    :vartype type: str or ~purviewunifiedcatalog.models.DataAssetType
    :ivar schema: Schema of the asset.
    :vartype schema: list[~purviewunifiedcatalog.models.CatalogModelDataAssetSchema]
    :ivar open_in_url: A redirection link.
    :vartype open_in_url: str
    :ivar lineage: Lineage information for the asset. See example responses for detailed structure.
    :vartype lineage: ~purviewunifiedcatalog.models.LineageObject
    """

    __mapping__: dict[str, _Model] = {}
    id: str = rest_field(visibility=["create"])
    """The data asset identifier. Required."""
    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Name of the data asset. Required."""
    system_data: Optional["_models.DataAssetSystemData"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """System data associated with the asset."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """A description about the relationship."""
    source: Optional["_models.CatalogModelDataAssetSource"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Source of the asset."""
    contacts: Optional["_models.ContactsMap"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Contacts associated with the asset."""
    classifications: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """A list of classification labels."""
    type: str = rest_discriminator(name="type", visibility=["read", "create", "update", "delete", "query"])
    """Type of the data asset. Required. Known values are: \"AzureSqlTable\", \"ADLSGen2Path\", and
     \"General\"."""
    schema: Optional[list["_models.CatalogModelDataAssetSchema"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Schema of the asset."""
    open_in_url: Optional[str] = rest_field(
        name="openInUrl", visibility=["read", "create", "update", "delete", "query"]
    )
    """A redirection link."""
    lineage: Optional["_models.LineageObject"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Lineage information for the asset. See example responses for detailed structure."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        name: str,
        type: str,
        system_data: Optional["_models.DataAssetSystemData"] = None,
        description: Optional[str] = None,
        source: Optional["_models.CatalogModelDataAssetSource"] = None,
        contacts: Optional["_models.ContactsMap"] = None,
        classifications: Optional[list[str]] = None,
        schema: Optional[list["_models.CatalogModelDataAssetSchema"]] = None,
        open_in_url: Optional[str] = None,
        lineage: Optional["_models.LineageObject"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataAssetWithLineageAdlsGen2Path(DataAssetWithLineage, discriminator="ADLSGen2Path"):
    """Data asset with lineage of type ADLS Gen2 Path.

    :ivar id: The data asset identifier. Required.
    :vartype id: str
    :ivar name: Name of the data asset. Required.
    :vartype name: str
    :ivar system_data: System data associated with the asset.
    :vartype system_data: ~purviewunifiedcatalog.models.DataAssetSystemData
    :ivar description: A description about the relationship.
    :vartype description: str
    :ivar source: Source of the asset.
    :vartype source: ~purviewunifiedcatalog.models.CatalogModelDataAssetSource
    :ivar contacts: Contacts associated with the asset.
    :vartype contacts: ~purviewunifiedcatalog.models.ContactsMap
    :ivar classifications: A list of classification labels.
    :vartype classifications: list[str]
    :ivar schema: Schema of the asset.
    :vartype schema: list[~purviewunifiedcatalog.models.CatalogModelDataAssetSchema]
    :ivar open_in_url: A redirection link.
    :vartype open_in_url: str
    :ivar lineage: Lineage information for the asset. See example responses for detailed structure.
    :vartype lineage: ~purviewunifiedcatalog.models.LineageObject
    :ivar type: Type of the data asset. Required. ADLS Gen2 Path data asset type.
    :vartype type: str or ~purviewunifiedcatalog.models.ADLS_GEN2_PATH
    :ivar type_properties: Type properties of the ADLS Gen2 path asset.
    :vartype type_properties: ~purviewunifiedcatalog.models.DataAssetAdlsGen2PathTypeProperties
    """

    type: Literal[DataAssetType.ADLS_GEN2_PATH] = rest_discriminator(name="type", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Type of the data asset. Required. ADLS Gen2 Path data asset type."""
    type_properties: Optional["_models.DataAssetAdlsGen2PathTypeProperties"] = rest_field(
        name="typeProperties", visibility=["read", "create", "update", "delete", "query"]
    )
    """Type properties of the ADLS Gen2 path asset."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        name: str,
        system_data: Optional["_models.DataAssetSystemData"] = None,
        description: Optional[str] = None,
        source: Optional["_models.CatalogModelDataAssetSource"] = None,
        contacts: Optional["_models.ContactsMap"] = None,
        classifications: Optional[list[str]] = None,
        schema: Optional[list["_models.CatalogModelDataAssetSchema"]] = None,
        open_in_url: Optional[str] = None,
        lineage: Optional["_models.LineageObject"] = None,
        type_properties: Optional["_models.DataAssetAdlsGen2PathTypeProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.type = DataAssetType.ADLS_GEN2_PATH  # type: ignore


class DataAssetWithLineageAzureSqlTable(DataAssetWithLineage, discriminator="AzureSqlTable"):
    """Data asset with lineage of type Azure SQL Table.

    :ivar id: The data asset identifier. Required.
    :vartype id: str
    :ivar name: Name of the data asset. Required.
    :vartype name: str
    :ivar system_data: System data associated with the asset.
    :vartype system_data: ~purviewunifiedcatalog.models.DataAssetSystemData
    :ivar description: A description about the relationship.
    :vartype description: str
    :ivar source: Source of the asset.
    :vartype source: ~purviewunifiedcatalog.models.CatalogModelDataAssetSource
    :ivar contacts: Contacts associated with the asset.
    :vartype contacts: ~purviewunifiedcatalog.models.ContactsMap
    :ivar classifications: A list of classification labels.
    :vartype classifications: list[str]
    :ivar schema: Schema of the asset.
    :vartype schema: list[~purviewunifiedcatalog.models.CatalogModelDataAssetSchema]
    :ivar open_in_url: A redirection link.
    :vartype open_in_url: str
    :ivar lineage: Lineage information for the asset. See example responses for detailed structure.
    :vartype lineage: ~purviewunifiedcatalog.models.LineageObject
    :ivar type: Type of the data asset. Required. Azure SQL Table data asset type.
    :vartype type: str or ~purviewunifiedcatalog.models.AZURE_SQL_TABLE
    :ivar type_properties: Type properties of the Azure SQL table asset.
    :vartype type_properties: ~purviewunifiedcatalog.models.DataAssetAzureSqlTableTypeProperties
    """

    type: Literal[DataAssetType.AZURE_SQL_TABLE] = rest_discriminator(name="type", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Type of the data asset. Required. Azure SQL Table data asset type."""
    type_properties: Optional["_models.DataAssetAzureSqlTableTypeProperties"] = rest_field(
        name="typeProperties", visibility=["read", "create", "update", "delete", "query"]
    )
    """Type properties of the Azure SQL table asset."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        name: str,
        system_data: Optional["_models.DataAssetSystemData"] = None,
        description: Optional[str] = None,
        source: Optional["_models.CatalogModelDataAssetSource"] = None,
        contacts: Optional["_models.ContactsMap"] = None,
        classifications: Optional[list[str]] = None,
        schema: Optional[list["_models.CatalogModelDataAssetSchema"]] = None,
        open_in_url: Optional[str] = None,
        lineage: Optional["_models.LineageObject"] = None,
        type_properties: Optional["_models.DataAssetAzureSqlTableTypeProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.type = DataAssetType.AZURE_SQL_TABLE  # type: ignore


class DataAssetWithLineageGeneral(DataAssetWithLineage, discriminator="General"):
    """Data asset with lineage of type General.

    :ivar id: The data asset identifier. Required.
    :vartype id: str
    :ivar name: Name of the data asset. Required.
    :vartype name: str
    :ivar system_data: System data associated with the asset.
    :vartype system_data: ~purviewunifiedcatalog.models.DataAssetSystemData
    :ivar description: A description about the relationship.
    :vartype description: str
    :ivar source: Source of the asset.
    :vartype source: ~purviewunifiedcatalog.models.CatalogModelDataAssetSource
    :ivar contacts: Contacts associated with the asset.
    :vartype contacts: ~purviewunifiedcatalog.models.ContactsMap
    :ivar classifications: A list of classification labels.
    :vartype classifications: list[str]
    :ivar schema: Schema of the asset.
    :vartype schema: list[~purviewunifiedcatalog.models.CatalogModelDataAssetSchema]
    :ivar open_in_url: A redirection link.
    :vartype open_in_url: str
    :ivar lineage: Lineage information for the asset. See example responses for detailed structure.
    :vartype lineage: ~purviewunifiedcatalog.models.LineageObject
    :ivar type: Type of the data asset. Required. General data asset type.
    :vartype type: str or ~purviewunifiedcatalog.models.GENERAL
    """

    type: Literal[DataAssetType.GENERAL] = rest_discriminator(name="type", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Type of the data asset. Required. General data asset type."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        name: str,
        system_data: Optional["_models.DataAssetSystemData"] = None,
        description: Optional[str] = None,
        source: Optional["_models.CatalogModelDataAssetSource"] = None,
        contacts: Optional["_models.ContactsMap"] = None,
        classifications: Optional[list[str]] = None,
        schema: Optional[list["_models.CatalogModelDataAssetSchema"]] = None,
        open_in_url: Optional[str] = None,
        lineage: Optional["_models.LineageObject"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.type = DataAssetType.GENERAL  # type: ignore


class DataColumn(_Model):
    """Microsoft Purview Data Governance Catalog Model Data Column.

    :ivar id: The unique identifier of the data column. Required.
    :vartype id: str
    :ivar source: The unique identifier of the asset. Required.
    :vartype source: ~purviewunifiedcatalog.models.DataColumnSource
    :ivar column_details: Details about the column from Data Map (name, description, data type,
     qualified name). Requested by setting includeColumnDetails to true, but may be null or
     partially populated if enrichment fails.
    :vartype column_details: ~purviewunifiedcatalog.models.DataColumnDetails
    :ivar asset_details: Details about the parent Data Governance asset (DG asset id, name, FQN).
     Requested when includeAssetDetails is true, but may be null or partial if enrichment fails.
    :vartype asset_details: ~purviewunifiedcatalog.models.DataColumnAssetDetails
    """

    id: str = rest_field(visibility=["read"])
    """The unique identifier of the data column. Required."""
    source: "_models.DataColumnSource" = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the asset. Required."""
    column_details: Optional["_models.DataColumnDetails"] = rest_field(
        name="columnDetails", visibility=["read", "create", "update", "delete", "query"]
    )
    """Details about the column from Data Map (name, description, data type, qualified name).
     Requested by setting includeColumnDetails to true, but may be null or partially populated if
     enrichment fails."""
    asset_details: Optional["_models.DataColumnAssetDetails"] = rest_field(
        name="assetDetails", visibility=["read", "create", "update", "delete", "query"]
    )
    """Details about the parent Data Governance asset (DG asset id, name, FQN). Requested when
     includeAssetDetails is true, but may be null or partial if enrichment fails."""

    @overload
    def __init__(
        self,
        *,
        source: "_models.DataColumnSource",
        column_details: Optional["_models.DataColumnDetails"] = None,
        asset_details: Optional["_models.DataColumnAssetDetails"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataColumnAssetDetails(_Model):
    """Details about the parent Data Governance asset.

    :ivar asset_id: The Data Governance asset identifier, which may be absent if enrichment is not
     possible.
    :vartype asset_id: str
    :ivar name: The display name of the asset.
    :vartype name: str
    :ivar fqn: The fully qualified name of the asset.
    :vartype fqn: str
    """

    asset_id: Optional[str] = rest_field(name="assetId", visibility=["read", "create", "update", "delete", "query"])
    """The Data Governance asset identifier, which may be absent if enrichment is not possible."""
    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The display name of the asset."""
    fqn: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The fully qualified name of the asset."""

    @overload
    def __init__(
        self,
        *,
        asset_id: Optional[str] = None,
        name: Optional[str] = None,
        fqn: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataColumnCreateRelationshipRequest(_Model):
    """Request model for ingesting a data column.

    :ivar relationship_type: The type of relationship for the data column. Known values are:
     "Related", "Synonym", and "Parent".
    :vartype relationship_type: str or ~purviewunifiedcatalog.models.DataColumnRelationshipType
    :ivar entity_id: The unique identifier of the related entity.
    :vartype entity_id: str
    :ivar description: A description for the relationship.
    :vartype description: str
    """

    relationship_type: Optional[Union[str, "_models.DataColumnRelationshipType"]] = rest_field(
        name="relationshipType", visibility=["read", "create", "update", "delete", "query"]
    )
    """The type of relationship for the data column. Known values are: \"Related\", \"Synonym\", and
     \"Parent\"."""
    entity_id: Optional[str] = rest_field(name="entityId", visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the related entity."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """A description for the relationship."""

    @overload
    def __init__(
        self,
        *,
        relationship_type: Optional[Union[str, "_models.DataColumnRelationshipType"]] = None,
        entity_id: Optional[str] = None,
        description: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataColumnCreateRelationshipResponse(_Model):
    """Request model for ingesting a data column.

    :ivar relationship_type: The type of relationship for the data column. Known values are:
     "Related", "Synonym", and "Parent".
    :vartype relationship_type: str or ~purviewunifiedcatalog.models.DataColumnRelationshipType
    :ivar entity_id: The unique identifier of the related entity.
    :vartype entity_id: str
    :ivar description: A description for the relationship.
    :vartype description: str
    :ivar system_data: System metadata including creation and modification information.
    :vartype system_data: ~purviewunifiedcatalog.models.SystemData
    """

    relationship_type: Optional[Union[str, "_models.DataColumnRelationshipType"]] = rest_field(
        name="relationshipType", visibility=["read", "create", "update", "delete", "query"]
    )
    """The type of relationship for the data column. Known values are: \"Related\", \"Synonym\", and
     \"Parent\"."""
    entity_id: Optional[str] = rest_field(name="entityId", visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the related entity."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """A description for the relationship."""
    system_data: Optional["_models.SystemData"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """System metadata including creation and modification information."""

    @overload
    def __init__(
        self,
        *,
        relationship_type: Optional[Union[str, "_models.DataColumnRelationshipType"]] = None,
        entity_id: Optional[str] = None,
        description: Optional[str] = None,
        system_data: Optional["_models.SystemData"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataColumnDetails(_Model):
    """Details about the Data Map column entity..

    :ivar name: The display name of the column from Data Map.
    :vartype name: str
    :ivar description: The description of the column from Data Map.
    :vartype description: str
    :ivar data_type: The data type of the column from Data Map.
    :vartype data_type: str
    :ivar qualified_name: The fully qualified name of the column from Data Map.
    :vartype qualified_name: str
    """

    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The display name of the column from Data Map."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The description of the column from Data Map."""
    data_type: Optional[str] = rest_field(name="dataType", visibility=["read", "create", "update", "delete", "query"])
    """The data type of the column from Data Map."""
    qualified_name: Optional[str] = rest_field(
        name="qualifiedName", visibility=["read", "create", "update", "delete", "query"]
    )
    """The fully qualified name of the column from Data Map."""

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        data_type: Optional[str] = None,
        qualified_name: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataColumnFieldFilter(_Model):
    """Field-level filter with comparison operators for GUID values.

    :ivar eq: Equals (exact match).
    :vartype eq: str
    :ivar ne: Not equals.
    :vartype ne: str
    :ivar in_property: In list (matches any value).
    :vartype in_property: list[str]
    :ivar nin: Not in list (excludes all values).
    :vartype nin: list[str]
    """

    eq: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Equals (exact match)."""
    ne: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Not equals."""
    in_property: Optional[list[str]] = rest_field(name="in", visibility=["read", "create", "update", "delete", "query"])
    """In list (matches any value)."""
    nin: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Not in list (excludes all values)."""

    @overload
    def __init__(
        self,
        *,
        eq: Optional[str] = None,
        ne: Optional[str] = None,
        in_property: Optional[list[str]] = None,
        nin: Optional[list[str]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataColumnIngestResponse(_Model):
    """Microsoft Purview Data Governance Catalog Model Data Column.

    :ivar id: The unique identifier of the data column. Required.
    :vartype id: str
    :ivar source: The unique identifier of the asset. Required.
    :vartype source: ~purviewunifiedcatalog.models.DataColumnSource
    """

    id: str = rest_field(visibility=["read"])
    """The unique identifier of the data column. Required."""
    source: "_models.DataColumnSource" = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the asset. Required."""

    @overload
    def __init__(
        self,
        *,
        source: "_models.DataColumnSource",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataColumnQueryFilter(_Model):
    """Recursive filter with logical AND/OR operators and field conditions.

    :ivar and_property: Logical AND: All conditions must match.
    :vartype and_property: list[~purviewunifiedcatalog.models.DataColumnQueryFilter]
    :ivar or_property: Logical OR: Any condition can match.
    :vartype or_property: list[~purviewunifiedcatalog.models.DataColumnQueryFilter]
    :ivar id: Filter by data column ID.
    :vartype id: ~purviewunifiedcatalog.models.DataColumnFieldFilter
    :ivar source_asset_id: Filter by data column ID.
    :vartype source_asset_id: ~purviewunifiedcatalog.models.DataColumnFieldFilter
    :ivar source_column_id: Filter by data column ID.
    :vartype source_column_id: ~purviewunifiedcatalog.models.DataColumnFieldFilter
    """

    and_property: Optional[list["_models.DataColumnQueryFilter"]] = rest_field(
        name="and", visibility=["read", "create", "update", "delete", "query"]
    )
    """Logical AND: All conditions must match."""
    or_property: Optional[list["_models.DataColumnQueryFilter"]] = rest_field(
        name="or", visibility=["read", "create", "update", "delete", "query"]
    )
    """Logical OR: Any condition can match."""
    id: Optional["_models.DataColumnFieldFilter"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by data column ID."""
    source_asset_id: Optional["_models.DataColumnFieldFilter"] = rest_field(
        name="sourceAssetId", visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by data column ID."""
    source_column_id: Optional["_models.DataColumnFieldFilter"] = rest_field(
        name="sourceColumnId", visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by data column ID."""

    @overload
    def __init__(
        self,
        *,
        and_property: Optional[list["_models.DataColumnQueryFilter"]] = None,
        or_property: Optional[list["_models.DataColumnQueryFilter"]] = None,
        id: Optional["_models.DataColumnFieldFilter"] = None,  # pylint: disable=redefined-builtin
        source_asset_id: Optional["_models.DataColumnFieldFilter"] = None,
        source_column_id: Optional["_models.DataColumnFieldFilter"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataColumnQueryRequest(_Model):
    """Query request for filtering and paginating data columns.

    :ivar filter: Filter conditions with logical AND/OR combinations.
    :vartype filter: ~purviewunifiedcatalog.models.DataColumnQueryFilter
    :ivar skip: Number of items to skip (pagination offset).
    :vartype skip: int
    :ivar top: Maximum number of items to return (page size).
    :vartype top: int
    :ivar including_orphans: Include data columns without relationships (orphans). Required.
    :vartype including_orphans: bool
    :ivar include_column_details: Include enriched column metadata from Data Map.
    :vartype include_column_details: bool
    :ivar include_asset_details: Include parent asset details (DG asset id, name, FQN).
    :vartype include_asset_details: bool
    """

    filter: Optional["_models.DataColumnQueryFilter"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter conditions with logical AND/OR combinations."""
    skip: Optional[int] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Number of items to skip (pagination offset)."""
    top: Optional[int] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Maximum number of items to return (page size)."""
    including_orphans: bool = rest_field(
        name="includingOrphans", visibility=["read", "create", "update", "delete", "query"]
    )
    """Include data columns without relationships (orphans). Required."""
    include_column_details: Optional[bool] = rest_field(
        name="includeColumnDetails", visibility=["read", "create", "update", "delete", "query"]
    )
    """Include enriched column metadata from Data Map."""
    include_asset_details: Optional[bool] = rest_field(
        name="includeAssetDetails", visibility=["read", "create", "update", "delete", "query"]
    )
    """Include parent asset details (DG asset id, name, FQN)."""

    @overload
    def __init__(
        self,
        *,
        including_orphans: bool,
        filter: Optional["_models.DataColumnQueryFilter"] = None,  # pylint: disable=redefined-builtin
        skip: Optional[int] = None,
        top: Optional[int] = None,
        include_column_details: Optional[bool] = None,
        include_asset_details: Optional[bool] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataColumnRelationshipWrapper(_Model):
    """Request model for creating a relationship between data columns.

    :ivar relationship_type: The type of relationship for the data column. Known values are:
     "Related", "Synonym", and "Parent".
    :vartype relationship_type: str or ~purviewunifiedcatalog.models.DataColumnRelationshipType
    :ivar entity_id: The unique identifier of the related entity.
    :vartype entity_id: str
    """

    relationship_type: Optional[Union[str, "_models.DataColumnRelationshipType"]] = rest_field(
        name="relationshipType", visibility=["read", "create", "update", "delete", "query"]
    )
    """The type of relationship for the data column. Known values are: \"Related\", \"Synonym\", and
     \"Parent\"."""
    entity_id: Optional[str] = rest_field(name="entityId", visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the related entity."""

    @overload
    def __init__(
        self,
        *,
        relationship_type: Optional[Union[str, "_models.DataColumnRelationshipType"]] = None,
        entity_id: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataColumnSource(_Model):
    """DataColumnSource.

    :ivar type: The type of the entity. Required.
    :vartype type: str
    :ivar asset_id: The unique identifier of the asset. Required.
    :vartype asset_id: str
    :ivar column_id: The unique identifier of the Column. Required.
    :vartype column_id: str
    """

    type: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The type of the entity. Required."""
    asset_id: str = rest_field(name="assetId", visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the asset. Required."""
    column_id: str = rest_field(name="columnId", visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the Column. Required."""

    @overload
    def __init__(
        self,
        *,
        type: str,
        asset_id: str,
        column_id: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataElementProperties(_Model):
    """DataElementProperties.

    :ivar description: The first additional property.
    :vartype description: str
    :ivar entity_id: The second additional property.
    :vartype entity_id: str
    :ivar relationship_type: The third additional property.
    :vartype relationship_type: str
    """

    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The first additional property."""
    entity_id: Optional[str] = rest_field(name="entityId", visibility=["read", "create", "update", "delete", "query"])
    """The second additional property."""
    relationship_type: Optional[str] = rest_field(
        name="relationshipType", visibility=["read", "create", "update", "delete", "query"]
    )
    """The third additional property."""

    @overload
    def __init__(
        self,
        *,
        description: Optional[str] = None,
        entity_id: Optional[str] = None,
        relationship_type: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataProduct(_Model):
    """Microsoft Purview Data Governance Catalog Model Data Product.

    :ivar status: The status of the data product. Known values are: "DRAFT", "PUBLISHED", and
     "EXPIRED".
    :vartype status: str or ~purviewunifiedcatalog.models.CatalogModelStatus
    :ivar type: The type of the data product. Known values are: "Master", "Reference",
     "Analytical", "AI", "MasterDataAndReferenceData", "BusinessSystemOrApplication", "ModelTypes",
     "DashboardsOrReports", "Operational", "MLAITrainingDataSet", "MLAITestingDataSet",
     "TransactionalDataset", "AnalyticsModel", and "SemanticModel".
    :vartype type: str or ~purviewunifiedcatalog.models.CatalogModelDataProductTypeEnum
    :ivar update_frequency: The update frequency of the data product. Known values are: "Hourly",
     "Daily", "Weekly", "Monthly", "Quarterly", and "Yearly".
    :vartype update_frequency: str or ~purviewunifiedcatalog.models.UpdateFrequencyEnum
    :ivar managed_attributes: The managed attributes associated with the data product.
    :vartype managed_attributes: list[~purviewunifiedcatalog.models.CatalogModelManagedAttribute]
    :ivar id: The unique identifier of the data product. Required.
    :vartype id: str
    :ivar name: The name of the data product.
    :vartype name: str
    :ivar system_data: The system data of the data product.
    :vartype system_data: ~purviewunifiedcatalog.models.CatalogModelSystemDataWithExpired
    :ivar domain: The domain of the data product.
    :vartype domain: str
    :ivar description: The description of the data product.
    :vartype description: str
    :ivar business_use: The business use of the data product.
    :vartype business_use: str
    :ivar contacts: The contacts associated with the data product.
    :vartype contacts: ~purviewunifiedcatalog.models.ContactsMap
    :ivar terms_of_use: The terms of use for the data product.
    :vartype terms_of_use: list[~purviewunifiedcatalog.models.CatalogModelExternalLink]
    :ivar documentation: The documentation links for the data product.
    :vartype documentation: list[~purviewunifiedcatalog.models.CatalogModelExternalLink]
    :ivar sensitivity_label: The sensitivity label of the data product.
    :vartype sensitivity_label: str
    :ivar endorsed: Whether the data product is endorsed.
    :vartype endorsed: bool
    :ivar active_subscriber_count: The number of active subscribers.
    :vartype active_subscriber_count: int
    :ivar data_quality_score: The data quality score of the data product.
    :vartype data_quality_score: float
    :ivar audience: The target audience for the data product.
    :vartype audience: list[str or ~purviewunifiedcatalog.models.AudienceEnum]
    :ivar additional_properties: Additional properties of the data product.
    :vartype additional_properties:
     ~purviewunifiedcatalog.models.CatalogModelDataProductAllOfAdditionalProperties
    """

    status: Optional[Union[str, "_models.CatalogModelStatus"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The status of the data product. Known values are: \"DRAFT\", \"PUBLISHED\", and \"EXPIRED\"."""
    type: Optional[Union[str, "_models.CatalogModelDataProductTypeEnum"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The type of the data product. Known values are: \"Master\", \"Reference\", \"Analytical\",
     \"AI\", \"MasterDataAndReferenceData\", \"BusinessSystemOrApplication\", \"ModelTypes\",
     \"DashboardsOrReports\", \"Operational\", \"MLAITrainingDataSet\", \"MLAITestingDataSet\",
     \"TransactionalDataset\", \"AnalyticsModel\", and \"SemanticModel\"."""
    update_frequency: Optional[Union[str, "_models.UpdateFrequencyEnum"]] = rest_field(
        name="updateFrequency", visibility=["read", "create", "update", "delete", "query"]
    )
    """The update frequency of the data product. Known values are: \"Hourly\", \"Daily\", \"Weekly\",
     \"Monthly\", \"Quarterly\", and \"Yearly\"."""
    managed_attributes: Optional[list["_models.CatalogModelManagedAttribute"]] = rest_field(
        name="managedAttributes", visibility=["read", "create", "update", "delete", "query"]
    )
    """The managed attributes associated with the data product."""
    id: str = rest_field(visibility=["create"])
    """The unique identifier of the data product. Required."""
    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name of the data product."""
    system_data: Optional["_models.CatalogModelSystemDataWithExpired"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """The system data of the data product."""
    domain: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The domain of the data product."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The description of the data product."""
    business_use: Optional[str] = rest_field(
        name="businessUse", visibility=["read", "create", "update", "delete", "query"]
    )
    """The business use of the data product."""
    contacts: Optional["_models.ContactsMap"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The contacts associated with the data product."""
    terms_of_use: Optional[list["_models.CatalogModelExternalLink"]] = rest_field(
        name="termsOfUse", visibility=["read", "create", "update", "delete", "query"]
    )
    """The terms of use for the data product."""
    documentation: Optional[list["_models.CatalogModelExternalLink"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The documentation links for the data product."""
    sensitivity_label: Optional[str] = rest_field(
        name="sensitivityLabel", visibility=["read", "create", "update", "delete", "query"]
    )
    """The sensitivity label of the data product."""
    endorsed: Optional[bool] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Whether the data product is endorsed."""
    active_subscriber_count: Optional[int] = rest_field(
        name="activeSubscriberCount", visibility=["read", "create", "update", "delete", "query"]
    )
    """The number of active subscribers."""
    data_quality_score: Optional[float] = rest_field(
        name="dataQualityScore", visibility=["read", "create", "update", "delete", "query"]
    )
    """The data quality score of the data product."""
    audience: Optional[list[Union[str, "_models.AudienceEnum"]]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The target audience for the data product."""
    additional_properties: Optional["_models.CatalogModelDataProductAllOfAdditionalProperties"] = rest_field(
        name="additionalProperties", visibility=["read", "create", "update", "delete", "query"]
    )
    """Additional properties of the data product."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        status: Optional[Union[str, "_models.CatalogModelStatus"]] = None,
        type: Optional[Union[str, "_models.CatalogModelDataProductTypeEnum"]] = None,
        update_frequency: Optional[Union[str, "_models.UpdateFrequencyEnum"]] = None,
        managed_attributes: Optional[list["_models.CatalogModelManagedAttribute"]] = None,
        name: Optional[str] = None,
        system_data: Optional["_models.CatalogModelSystemDataWithExpired"] = None,
        domain: Optional[str] = None,
        description: Optional[str] = None,
        business_use: Optional[str] = None,
        contacts: Optional["_models.ContactsMap"] = None,
        terms_of_use: Optional[list["_models.CatalogModelExternalLink"]] = None,
        documentation: Optional[list["_models.CatalogModelExternalLink"]] = None,
        sensitivity_label: Optional[str] = None,
        endorsed: Optional[bool] = None,
        active_subscriber_count: Optional[int] = None,
        data_quality_score: Optional[float] = None,
        audience: Optional[list[Union[str, "_models.AudienceEnum"]]] = None,
        additional_properties: Optional["_models.CatalogModelDataProductAllOfAdditionalProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataProductFacetRequest(_Model):
    """DataProductFacetRequest.

    :ivar ids: To filter by Ids.
    :vartype ids: list[str]
    :ivar domain_ids: To filter by domain Ids.
    :vartype domain_ids: list[str]
    :ivar name_keyword: To filter by name keyword.
    :vartype name_keyword: str
    :ivar owners: To filter by owners.
    :vartype owners: list[str]
    :ivar status: To filter by status. Known values are: "Draft", "Published", and "Expired".
    :vartype status: str or ~purviewunifiedcatalog.models.SharedEntityStatus
    :ivar multi_status: To filter by multiple status.
    :vartype multi_status: list[str or ~purviewunifiedcatalog.models.SharedEntityStatus]
    :ivar type: To filter by type.
    :vartype type: str
    :ivar types: To filter by multiple types.
    :vartype types: list[str]
    :ivar facets: To filter by multiple facets.
    :vartype facets: list[~purviewunifiedcatalog.models.ModelsFacetRequestObject]
    """

    ids: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by Ids."""
    domain_ids: Optional[list[str]] = rest_field(
        name="domainIds", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by domain Ids."""
    name_keyword: Optional[str] = rest_field(
        name="nameKeyword", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by name keyword."""
    owners: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by owners."""
    status: Optional[Union[str, "_models.SharedEntityStatus"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by status. Known values are: \"Draft\", \"Published\", and \"Expired\"."""
    multi_status: Optional[list[Union[str, "_models.SharedEntityStatus"]]] = rest_field(
        name="multiStatus", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by multiple status."""
    type: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by type."""
    types: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by multiple types."""
    facets: Optional[list["_models.ModelsFacetRequestObject"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by multiple facets."""

    @overload
    def __init__(
        self,
        *,
        ids: Optional[list[str]] = None,
        domain_ids: Optional[list[str]] = None,
        name_keyword: Optional[str] = None,
        owners: Optional[list[str]] = None,
        status: Optional[Union[str, "_models.SharedEntityStatus"]] = None,
        multi_status: Optional[list[Union[str, "_models.SharedEntityStatus"]]] = None,
        type: Optional[str] = None,
        types: Optional[list[str]] = None,
        facets: Optional[list["_models.ModelsFacetRequestObject"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataProductQueryRequest(_Model):
    """DataProductQueryRequest.

    :ivar skip: Number of items to skip.
    :vartype skip: int
    :ivar top: Number of items to return.
    :vartype top: int
    :ivar orderby: To order the records.
    :vartype orderby: list[~purviewunifiedcatalog.models.CatalogApiServiceOrderBy]
    :ivar ids: To filter by Ids.
    :vartype ids: list[str]
    :ivar domain_ids: To filter by domain Ids.
    :vartype domain_ids: list[str]
    :ivar name_keyword: To filter by name keyword.
    :vartype name_keyword: str
    :ivar type: To filter by type.
    :vartype type: str
    :ivar types: To filter by multiple types.
    :vartype types: list[str]
    :ivar owners: To filter by owners.
    :vartype owners: list[str]
    :ivar status: To filter by status. Known values are: "Draft", "Published", and "Expired".
    :vartype status: str or ~purviewunifiedcatalog.models.SharedEntityStatus
    :ivar multi_status: To filter by multiple status.
    :vartype multi_status: list[str or ~purviewunifiedcatalog.models.SharedEntityStatus]
    :ivar managed_attributes: To filter by managed attributes.
    :vartype managed_attributes:
     list[~purviewunifiedcatalog.models.SharedSearchManageAttributeSearchFilter]
    """

    skip: Optional[int] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Number of items to skip."""
    top: Optional[int] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Number of items to return."""
    orderby: Optional[list["_models.CatalogApiServiceOrderBy"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """To order the records."""
    ids: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by Ids."""
    domain_ids: Optional[list[str]] = rest_field(
        name="domainIds", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by domain Ids."""
    name_keyword: Optional[str] = rest_field(
        name="nameKeyword", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by name keyword."""
    type: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by type."""
    types: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by multiple types."""
    owners: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by owners."""
    status: Optional[Union[str, "_models.SharedEntityStatus"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by status. Known values are: \"Draft\", \"Published\", and \"Expired\"."""
    multi_status: Optional[list[Union[str, "_models.SharedEntityStatus"]]] = rest_field(
        name="multiStatus", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by multiple status."""
    managed_attributes: Optional[list["_models.SharedSearchManageAttributeSearchFilter"]] = rest_field(
        name="managedAttributes", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by managed attributes."""

    @overload
    def __init__(
        self,
        *,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        orderby: Optional[list["_models.CatalogApiServiceOrderBy"]] = None,
        ids: Optional[list[str]] = None,
        domain_ids: Optional[list[str]] = None,
        name_keyword: Optional[str] = None,
        type: Optional[str] = None,
        types: Optional[list[str]] = None,
        owners: Optional[list[str]] = None,
        status: Optional[Union[str, "_models.SharedEntityStatus"]] = None,
        multi_status: Optional[list[Union[str, "_models.SharedEntityStatus"]]] = None,
        managed_attributes: Optional[list["_models.SharedSearchManageAttributeSearchFilter"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DataProductRelationship(_Model):
    """Relationship information between entities.

    :ivar system_data: System metadata for the relationship.
    :vartype system_data: ~purviewunifiedcatalog.models.SystemData
    :ivar description: Description of the relationship.
    :vartype description: str
    :ivar relationship_type: Type of the relationship.
    :vartype relationship_type: str
    :ivar entity_id: Unique identifier of the related entity. Required.
    :vartype entity_id: str
    """

    system_data: Optional["_models.SystemData"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """System metadata for the relationship."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Description of the relationship."""
    relationship_type: Optional[str] = rest_field(
        name="relationshipType", visibility=["read", "create", "update", "delete", "query"]
    )
    """Type of the relationship."""
    entity_id: str = rest_field(name="entityId", visibility=["create"])
    """Unique identifier of the related entity. Required."""

    @overload
    def __init__(
        self,
        *,
        entity_id: str,
        system_data: Optional["_models.SystemData"] = None,
        description: Optional[str] = None,
        relationship_type: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DecisionRule(_Model):
    """DecisionRule.

    :ivar kind: The kind of decision rule. Required.
    :vartype kind: str
    :ivar effect: The unique identifier of the decision rule. Required.
    :vartype effect: str
    :ivar dnf_condition: The name of the decision rule. Required.
    :vartype dnf_condition: list[list[~purviewunifiedcatalog.models.Condition]]
    """

    kind: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The kind of decision rule. Required."""
    effect: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the decision rule. Required."""
    dnf_condition: list[list["_models.Condition"]] = rest_field(
        name="dnfCondition", visibility=["read", "create", "update", "delete", "query"]
    )
    """The name of the decision rule. Required."""

    @overload
    def __init__(
        self,
        *,
        kind: str,
        effect: str,
        dnf_condition: list[list["_models.Condition"]],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Domain(_Model):
    """Catalog model domain.

    :ivar status: The status of the domain. Known values are: "DRAFT", "PUBLISHED", and "EXPIRED".
    :vartype status: str or ~purviewunifiedcatalog.models.CatalogModelStatus
    :ivar type: The type of the domain. Known values are: "FunctionalUnit", "LineOfBusiness",
     "DataDomain", "Regulatory", and "Project".
    :vartype type: str or ~purviewunifiedcatalog.models.CatalogModelDomainTypeEnum
    :ivar id: The unique identifier of the domain. Required.
    :vartype id: str
    :ivar name: The name of the domain.
    :vartype name: str
    :ivar is_restricted: Whether the domain is restricted.
    :vartype is_restricted: bool
    :ivar system_data: The system data of the domain. Required.
    :vartype system_data: ~purviewunifiedcatalog.models.CatalogModelSystemDataWithExpired
    :ivar description: The description of the domain.
    :vartype description: str
    :ivar parent_id: Identifier of the domain to retrieve. Required.
    :vartype parent_id: str
    :ivar thumbnail: The thumbnail properties of the domain. Required.
    :vartype thumbnail: ~purviewunifiedcatalog.models.CatalogModelDomainAllOfThumbnail
    :ivar domains: The list of platform domains. Required.
    :vartype domains: list[~purviewunifiedcatalog.models.CatalogModelPlatformDomain]
    :ivar managed_attributes: The managed attributes associated with the domain. Required.
    :vartype managed_attributes: list[~purviewunifiedcatalog.models.CatalogModelManagedAttribute]
    """

    status: Optional[Union[str, "_models.CatalogModelStatus"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The status of the domain. Known values are: \"DRAFT\", \"PUBLISHED\", and \"EXPIRED\"."""
    type: Optional[Union[str, "_models.CatalogModelDomainTypeEnum"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The type of the domain. Known values are: \"FunctionalUnit\", \"LineOfBusiness\",
     \"DataDomain\", \"Regulatory\", and \"Project\"."""
    id: str = rest_field(visibility=["create"])
    """The unique identifier of the domain. Required."""
    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name of the domain."""
    is_restricted: Optional[bool] = rest_field(
        name="isRestricted", visibility=["read", "create", "update", "delete", "query"]
    )
    """Whether the domain is restricted."""
    system_data: "_models.CatalogModelSystemDataWithExpired" = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """The system data of the domain. Required."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The description of the domain."""
    parent_id: str = rest_field(name="parentId", visibility=["read", "create", "update", "delete", "query"])
    """Identifier of the domain to retrieve. Required."""
    thumbnail: "_models.CatalogModelDomainAllOfThumbnail" = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The thumbnail properties of the domain. Required."""
    domains: list["_models.CatalogModelPlatformDomain"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The list of platform domains. Required."""
    managed_attributes: list["_models.CatalogModelManagedAttribute"] = rest_field(
        name="managedAttributes", visibility=["read", "create", "update", "delete", "query"]
    )
    """The managed attributes associated with the domain. Required."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        system_data: "_models.CatalogModelSystemDataWithExpired",
        parent_id: str,
        thumbnail: "_models.CatalogModelDomainAllOfThumbnail",
        domains: list["_models.CatalogModelPlatformDomain"],
        managed_attributes: list["_models.CatalogModelManagedAttribute"],
        status: Optional[Union[str, "_models.CatalogModelStatus"]] = None,
        type: Optional[Union[str, "_models.CatalogModelDomainTypeEnum"]] = None,
        name: Optional[str] = None,
        is_restricted: Optional[bool] = None,
        description: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DuplicateOkrQueryRequest(_Model):
    """Request model for querying duplicate objectives/OKRs.

    :ivar definition: The keyword to search for duplicate objectives/OKRs by name. Required.
    :vartype definition: str
    """

    definition: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The keyword to search for duplicate objectives/OKRs by name. Required."""

    @overload
    def __init__(
        self,
        *,
        definition: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DuplicateQueryRequest(_Model):
    """Request model for querying duplicate.

    :ivar name_keyword: The keyword to search for duplicate elements by name. Required.
    :vartype name_keyword: str
    """

    name_keyword: str = rest_field(name="nameKeyword", visibility=["read", "create", "update", "delete", "query"])
    """The keyword to search for duplicate elements by name. Required."""

    @overload
    def __init__(
        self,
        *,
        name_keyword: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class EntityCount(_Model):
    """Response model for duplicate critical data element query, containing the count of duplicate
    entities.

    :ivar count: Count of entities which exist. Required.
    :vartype count: int
    """

    count: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Count of entities which exist. Required."""

    @overload
    def __init__(
        self,
        *,
        count: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class EntityReference(_Model):
    """EntityReference.

    :ivar type: The type of the entity. Required.
    :vartype type: str
    :ivar reference_name: The reference name of the entity. Required.
    :vartype reference_name: str
    """

    type: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The type of the entity. Required."""
    reference_name: str = rest_field(name="referenceName", visibility=["read", "create", "update", "delete", "query"])
    """The reference name of the entity. Required."""

    @overload
    def __init__(
        self,
        *,
        type: str,
        reference_name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class FacetRequestObject(_Model):
    """Facet request object model.

    :ivar name: The name of the facet.
    :vartype name: str
    """

    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name of the facet."""

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class FacetsResponse(_Model):
    """FacetsResponse.

    :ivar facets: The list of facets. Required.
    :vartype facets: dict[str, list[~purviewunifiedcatalog.models.FacetValue]]
    """

    facets: dict[str, list["_models.FacetValue"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The list of facets. Required."""

    @overload
    def __init__(
        self,
        *,
        facets: dict[str, list["_models.FacetValue"]],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class FacetValue(_Model):
    """FacetValue.

    :ivar value: The value of the facet. Required.
    :vartype value: str
    :ivar count: The count of items in the facet. Required.
    :vartype count: str
    """

    value: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The value of the facet. Required."""
    count: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The count of items in the facet. Required."""

    @overload
    def __init__(
        self,
        *,
        value: str,
        count: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class IngestDataColumnBatchRequest(_Model):
    """Request model for ingesting a batch of data columns.

    :ivar requests: The list of data column ingestion requests.
    :vartype requests: list[~purviewunifiedcatalog.models.IngestDataColumnRequest]
    """

    requests: Optional[list["_models.IngestDataColumnRequest"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The list of data column ingestion requests."""

    @overload
    def __init__(
        self,
        *,
        requests: Optional[list["_models.IngestDataColumnRequest"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class IngestDataColumnRequest(_Model):
    """Request model for ingesting a data column.

    :ivar data_map_asset_id: AssetId from Datamap.
    :vartype data_map_asset_id: str
    :ivar data_map_column_id: ColumnId from Datamap.
    :vartype data_map_column_id: str
    """

    data_map_asset_id: Optional[str] = rest_field(
        name="dataMapAssetId", visibility=["read", "create", "update", "delete", "query"]
    )
    """AssetId from Datamap."""
    data_map_column_id: Optional[str] = rest_field(
        name="dataMapColumnId", visibility=["read", "create", "update", "delete", "query"]
    )
    """ColumnId from Datamap."""

    @overload
    def __init__(
        self,
        *,
        data_map_asset_id: Optional[str] = None,
        data_map_column_id: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class KeyResult(_Model):
    """Microsoft Purview Data Governance Catalog Key Result.

    :ivar status: The status of the key result. Required. Known values are: "NotTracked",
     "OnTrack", "Behind", and "AtRisk".
    :vartype status: str or ~purviewunifiedcatalog.models.OverallStatusEnum
    :ivar system_data: The system data associated with the key result.
    :vartype system_data: ~purviewunifiedcatalog.models.SystemData
    :ivar id: The unique identifier of the key result.
    :vartype id: str
    :ivar definition: The definition of the key result.
    :vartype definition: str
    :ivar domain_id: The unique identifier of the domain. Required.
    :vartype domain_id: str
    :ivar progress: The progress of the key result.
    :vartype progress: float
    :ivar goal: The goal value for the key result.
    :vartype goal: float
    :ivar max: The maximum value for the key result.
    :vartype max: float
    """

    status: Union[str, "_models.OverallStatusEnum"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The status of the key result. Required. Known values are: \"NotTracked\", \"OnTrack\",
     \"Behind\", and \"AtRisk\"."""
    system_data: Optional["_models.SystemData"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """The system data associated with the key result."""
    id: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the key result."""
    definition: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The definition of the key result."""
    domain_id: str = rest_field(name="domainId", visibility=["create"])
    """The unique identifier of the domain. Required."""
    progress: Optional[float] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The progress of the key result."""
    goal: Optional[float] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The goal value for the key result."""
    max: Optional[float] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The maximum value for the key result."""

    @overload
    def __init__(
        self,
        *,
        status: Union[str, "_models.OverallStatusEnum"],
        domain_id: str,
        system_data: Optional["_models.SystemData"] = None,
        id: Optional[str] = None,  # pylint: disable=redefined-builtin
        definition: Optional[str] = None,
        progress: Optional[float] = None,
        goal: Optional[float] = None,
        max: Optional[float] = None,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class LineageObject(_Model):
    """Lineage information object containing entity relationships and graph data."""


class ModelsFacetRequestObject(_Model):
    """ModelsFacetRequestObject.

    :ivar name: name.
    :vartype name: str
    """

    name: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """name."""

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ObjectiveAdditionalProperties(_Model):
    """Additional properties for objective model.

    :ivar overall_status: The overall status of the objective. Known values are: "NotTracked",
     "OnTrack", "Behind", and "AtRisk".
    :vartype overall_status: str or ~purviewunifiedcatalog.models.OverallStatusEnum
    :ivar overall_progress: The overall progress of the objective.
    :vartype overall_progress: float
    :ivar overall_goal: The overall goal value for the objective.
    :vartype overall_goal: float
    :ivar overall_max: The maximum value for the objective.
    :vartype overall_max: float
    :ivar key_results_count: The number of key results associated with the objective.
    :vartype key_results_count: int
    """

    overall_status: Optional[Union[str, "_models.OverallStatusEnum"]] = rest_field(
        name="overallStatus", visibility=["read", "create", "update", "delete", "query"]
    )
    """The overall status of the objective. Known values are: \"NotTracked\", \"OnTrack\", \"Behind\",
     and \"AtRisk\"."""
    overall_progress: Optional[float] = rest_field(
        name="overallProgress", visibility=["read", "create", "update", "delete", "query"]
    )
    """The overall progress of the objective."""
    overall_goal: Optional[float] = rest_field(
        name="overallGoal", visibility=["read", "create", "update", "delete", "query"]
    )
    """The overall goal value for the objective."""
    overall_max: Optional[float] = rest_field(
        name="overallMax", visibility=["read", "create", "update", "delete", "query"]
    )
    """The maximum value for the objective."""
    key_results_count: Optional[int] = rest_field(
        name="keyResultsCount", visibility=["read", "create", "update", "delete", "query"]
    )
    """The number of key results associated with the objective."""

    @overload
    def __init__(
        self,
        *,
        overall_status: Optional[Union[str, "_models.OverallStatusEnum"]] = None,
        overall_progress: Optional[float] = None,
        overall_goal: Optional[float] = None,
        overall_max: Optional[float] = None,
        key_results_count: Optional[int] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ObjectiveFacetRequest(_Model):
    """Objective facet request model.

    :ivar ids: Filter by objective IDs.
    :vartype ids: list[str]
    :ivar domain_ids: Filter by domain IDs.
    :vartype domain_ids: list[str]
    :ivar definition: Filter by objective definition.
    :vartype definition: str
    :ivar owners: Filter by objective owners.
    :vartype owners: list[str]
    :ivar status: Filter by objective status. Known values are: "Draft", "Published", and "Closed".
    :vartype status: str or ~purviewunifiedcatalog.models.OkrSharedEntityStatus
    :ivar multi_status: Filter by multiple objective statuses.
    :vartype multi_status: list[str or ~purviewunifiedcatalog.models.OkrSharedEntityStatus]
    :ivar facets: Filter by facet objects.
    :vartype facets: list[~purviewunifiedcatalog.models.FacetRequestObject]
    """

    ids: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Filter by objective IDs."""
    domain_ids: Optional[list[str]] = rest_field(
        name="domainIds", visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by domain IDs."""
    definition: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Filter by objective definition."""
    owners: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Filter by objective owners."""
    status: Optional[Union[str, "_models.OkrSharedEntityStatus"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by objective status. Known values are: \"Draft\", \"Published\", and \"Closed\"."""
    multi_status: Optional[list[Union[str, "_models.OkrSharedEntityStatus"]]] = rest_field(
        name="multiStatus", visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by multiple objective statuses."""
    facets: Optional[list["_models.FacetRequestObject"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by facet objects."""

    @overload
    def __init__(
        self,
        *,
        ids: Optional[list[str]] = None,
        domain_ids: Optional[list[str]] = None,
        definition: Optional[str] = None,
        owners: Optional[list[str]] = None,
        status: Optional[Union[str, "_models.OkrSharedEntityStatus"]] = None,
        multi_status: Optional[list[Union[str, "_models.OkrSharedEntityStatus"]]] = None,
        facets: Optional[list["_models.FacetRequestObject"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ObjectiveQueryAdditionalProperties(_Model):
    """Additional properties for objective query.

    :ivar status: The overall status of the objective. Known values are: "Draft", "Published", and
     "Closed".
    :vartype status: str or ~purviewunifiedcatalog.models.OkrSharedEntityStatus
    :ivar system_data: The system data associated with the objective.
    :vartype system_data: ~purviewunifiedcatalog.models.OkrSystemDataWithExpired
    :ivar id: The unique identifier of the objective.
    :vartype id: str
    :ivar definition: The definition of the objective.
    :vartype definition: str
    :ivar domain: The domain associated with the objective.
    :vartype domain: str
    :ivar target_date: The target date for the objective.
    :vartype target_date: ~datetime.datetime
    :ivar contacts: The contacts associated with the objective.
    :vartype contacts: ~purviewunifiedcatalog.models.ContactsMap
    :ivar additional_properties: Additional properties for objective query. Known values are:
     "NotTracked", "OnTrack", "Behind", and "AtRisk".
    :vartype additional_properties: str or ~purviewunifiedcatalog.models.OverallStatusEnum
    """

    status: Optional[Union[str, "_models.OkrSharedEntityStatus"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The overall status of the objective. Known values are: \"Draft\", \"Published\", and
     \"Closed\"."""
    system_data: Optional["_models.OkrSystemDataWithExpired"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """The system data associated with the objective."""
    id: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the objective."""
    definition: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The definition of the objective."""
    domain: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The domain associated with the objective."""
    target_date: Optional[datetime.datetime] = rest_field(
        name="targetDate", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The target date for the objective."""
    contacts: Optional["_models.ContactsMap"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The contacts associated with the objective."""
    additional_properties: Optional[Union[str, "_models.OverallStatusEnum"]] = rest_field(
        name="additionalProperties", visibility=["read", "create", "update", "delete", "query"]
    )
    """Additional properties for objective query. Known values are: \"NotTracked\", \"OnTrack\",
     \"Behind\", and \"AtRisk\"."""

    @overload
    def __init__(
        self,
        *,
        status: Optional[Union[str, "_models.OkrSharedEntityStatus"]] = None,
        system_data: Optional["_models.OkrSystemDataWithExpired"] = None,
        id: Optional[str] = None,  # pylint: disable=redefined-builtin
        definition: Optional[str] = None,
        domain: Optional[str] = None,
        target_date: Optional[datetime.datetime] = None,
        contacts: Optional["_models.ContactsMap"] = None,
        additional_properties: Optional[Union[str, "_models.OverallStatusEnum"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ObjectiveQueryRequest(_Model):
    """ObjectiveQueryRequest.

    :ivar skip: Number of items to skip.
    :vartype skip: int
    :ivar top: Number of items to return.
    :vartype top: int
    :ivar orderby: Order by specifications for the query.
    :vartype orderby: list[~purviewunifiedcatalog.models.CatalogApiServiceOrderBy]
    :ivar ids: Filter by objective IDs.
    :vartype ids: list[str]
    :ivar domain_ids: Filter by domain IDs.
    :vartype domain_ids: list[str]
    :ivar definition: Filter by objective definition.
    :vartype definition: str
    :ivar status: Filter by objective status. Known values are: "Draft", "Published", and "Closed".
    :vartype status: str or ~purviewunifiedcatalog.models.OkrSharedEntityStatus
    :ivar multi_status: Filter by multiple objective statuses.
    :vartype multi_status: list[str or ~purviewunifiedcatalog.models.OkrSharedEntityStatus]
    :ivar owners: Filter by objective owners.
    :vartype owners: list[str]
    :ivar managed_attributes: To filter by managed attributes.
    :vartype managed_attributes:
     list[~purviewunifiedcatalog.models.SharedSearchManageAttributeSearchFilter]
    """

    skip: Optional[int] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Number of items to skip."""
    top: Optional[int] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Number of items to return."""
    orderby: Optional[list["_models.CatalogApiServiceOrderBy"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Order by specifications for the query."""
    ids: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Filter by objective IDs."""
    domain_ids: Optional[list[str]] = rest_field(
        name="domainIds", visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by domain IDs."""
    definition: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Filter by objective definition."""
    status: Optional[Union[str, "_models.OkrSharedEntityStatus"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by objective status. Known values are: \"Draft\", \"Published\", and \"Closed\"."""
    multi_status: Optional[list[Union[str, "_models.OkrSharedEntityStatus"]]] = rest_field(
        name="multiStatus", visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by multiple objective statuses."""
    owners: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Filter by objective owners."""
    managed_attributes: Optional[list["_models.SharedSearchManageAttributeSearchFilter"]] = rest_field(
        name="managedAttributes", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by managed attributes."""

    @overload
    def __init__(
        self,
        *,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        orderby: Optional[list["_models.CatalogApiServiceOrderBy"]] = None,
        ids: Optional[list[str]] = None,
        domain_ids: Optional[list[str]] = None,
        definition: Optional[str] = None,
        status: Optional[Union[str, "_models.OkrSharedEntityStatus"]] = None,
        multi_status: Optional[list[Union[str, "_models.OkrSharedEntityStatus"]]] = None,
        owners: Optional[list[str]] = None,
        managed_attributes: Optional[list["_models.SharedSearchManageAttributeSearchFilter"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ObjectiveWithAdditionalProperties(_Model):
    """Objective with additional properties model.

    :ivar status: The status of the objective. Known values are: "Draft", "Published", and
     "Closed".
    :vartype status: str or ~purviewunifiedcatalog.models.OkrSharedEntityStatus
    :ivar system_data: The system data associated with the objective.
    :vartype system_data: ~purviewunifiedcatalog.models.OkrSystemDataWithExpired
    :ivar id: The unique identifier of the objective. Required.
    :vartype id: str
    :ivar definition: The definition of the objective. Required.
    :vartype definition: str
    :ivar domain: The domain associated with the objective.
    :vartype domain: str
    :ivar target_date: The target date for the objective.
    :vartype target_date: ~datetime.datetime
    :ivar contacts: The contacts associated with the objective.
    :vartype contacts: ~purviewunifiedcatalog.models.ContactsMap
    :ivar additional_properties: Additional properties for the objective.
    :vartype additional_properties: ~purviewunifiedcatalog.models.ObjectiveAdditionalProperties
    """

    status: Optional[Union[str, "_models.OkrSharedEntityStatus"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The status of the objective. Known values are: \"Draft\", \"Published\", and \"Closed\"."""
    system_data: Optional["_models.OkrSystemDataWithExpired"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """The system data associated with the objective."""
    id: str = rest_field(visibility=["create"])
    """The unique identifier of the objective. Required."""
    definition: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The definition of the objective. Required."""
    domain: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The domain associated with the objective."""
    target_date: Optional[datetime.datetime] = rest_field(
        name="targetDate", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The target date for the objective."""
    contacts: Optional["_models.ContactsMap"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The contacts associated with the objective."""
    additional_properties: Optional["_models.ObjectiveAdditionalProperties"] = rest_field(
        name="additionalProperties", visibility=["read", "create", "update", "delete", "query"]
    )
    """Additional properties for the objective."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        definition: str,
        status: Optional[Union[str, "_models.OkrSharedEntityStatus"]] = None,
        system_data: Optional["_models.OkrSystemDataWithExpired"] = None,
        domain: Optional[str] = None,
        target_date: Optional[datetime.datetime] = None,
        contacts: Optional["_models.ContactsMap"] = None,
        additional_properties: Optional["_models.ObjectiveAdditionalProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class OkrSystemDataWithExpired(_Model):
    """OkrSystemDataWithExpired.

    :ivar created_at: The created time of the record.
    :vartype created_at: ~datetime.datetime
    :ivar created_by: The user who created the record.
    :vartype created_by: str
    :ivar last_modified_at: The user who Last modified the record.
    :vartype last_modified_at: ~datetime.datetime
    :ivar last_modified_by: The user who last modified the record.
    :vartype last_modified_by: str
    :ivar closed_at: The time when the record was closed.
    :vartype closed_at: ~datetime.datetime
    :ivar closed_by: The user who closed the record.
    :vartype closed_by: str
    """

    created_at: Optional[datetime.datetime] = rest_field(
        name="createdAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The created time of the record."""
    created_by: Optional[str] = rest_field(name="createdBy", visibility=["read", "create", "update", "delete", "query"])
    """The user who created the record."""
    last_modified_at: Optional[datetime.datetime] = rest_field(
        name="lastModifiedAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The user who Last modified the record."""
    last_modified_by: Optional[str] = rest_field(
        name="lastModifiedBy", visibility=["read", "create", "update", "delete", "query"]
    )
    """The user who last modified the record."""
    closed_at: Optional[datetime.datetime] = rest_field(
        name="closedAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The time when the record was closed."""
    closed_by: Optional[str] = rest_field(name="closedBy", visibility=["read", "create", "update", "delete", "query"])
    """The user who closed the record."""

    @overload
    def __init__(
        self,
        *,
        created_at: Optional[datetime.datetime] = None,
        created_by: Optional[str] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        closed_at: Optional[datetime.datetime] = None,
        closed_by: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Relationship(_Model):
    """Relationship information between entities.

    :ivar system_data: System metadata for the relationship.
    :vartype system_data: ~purviewunifiedcatalog.models.SystemData
    :ivar description: Description of the relationship.
    :vartype description: str
    :ivar relationship_type: Type of the relationship.
    :vartype relationship_type: str
    :ivar entity_id: Unique identifier of the related entity. Required.
    :vartype entity_id: str
    """

    system_data: Optional["_models.SystemData"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """System metadata for the relationship."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Description of the relationship."""
    relationship_type: Optional[str] = rest_field(
        name="relationshipType", visibility=["read", "create", "update", "delete", "query"]
    )
    """Type of the relationship."""
    entity_id: str = rest_field(name="entityId", visibility=["create"])
    """Unique identifier of the related entity. Required."""

    @overload
    def __init__(
        self,
        *,
        entity_id: str,
        system_data: Optional["_models.SystemData"] = None,
        description: Optional[str] = None,
        relationship_type: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SharedSearchManageAttributeSearchFilter(_Model):
    """Filter configuration for searching managed attributes.

    :ivar field: The field name to filter on. Example: 'All Attributes Types.AttributeName'.
    :vartype field: str
    :ivar operator: The comparison operator to use for filtering. Example: 'ne' , 'eq' ,'gt' , 'ge'
     , 'lt' , 'le', 'contains' ,'notcontains', 'prefix','eq-any'.
    :vartype operator: str
    :ivar value: The value to compare against. Example: '2', 'LAST_24H',
     LAST_7D','LAST_30D',LAST_365D','MORE_THAN_365D'.
    :vartype value: str
    :ivar type: The data type of the filter value. Example:
     'int','date','double','float',richtext','short','string','boolean','multiChoice'.
    :vartype type: str
    """

    field: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The field name to filter on. Example: 'All Attributes Types.AttributeName'."""
    operator: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The comparison operator to use for filtering. Example: 'ne' , 'eq' ,'gt' , 'ge' , 'lt' , 'le',
     'contains' ,'notcontains', 'prefix','eq-any'."""
    value: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The value to compare against. Example: '2', 'LAST_24H',
     LAST_7D','LAST_30D',LAST_365D','MORE_THAN_365D'."""
    type: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The data type of the filter value. Example:
     'int','date','double','float',richtext','short','string','boolean','multiChoice'."""

    @overload
    def __init__(
        self,
        *,
        field: Optional[str] = None,
        operator: Optional[str] = None,
        value: Optional[str] = None,
        type: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SystemData(_Model):
    """System metadata for tracking entity lifecycle.

    :ivar last_modified_at: The timestamp when the entity was last modified.
    :vartype last_modified_at: ~datetime.datetime
    :ivar last_modified_by: The unique identifier of the user who last modified the entity.
    :vartype last_modified_by: str
    :ivar created_at: The timestamp when the entity was created.
    :vartype created_at: str
    :ivar created_by: The unique identifier of the user who created the entity.
    :vartype created_by: str
    """

    last_modified_at: Optional[datetime.datetime] = rest_field(
        name="lastModifiedAt", visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """The timestamp when the entity was last modified."""
    last_modified_by: Optional[str] = rest_field(
        name="lastModifiedBy", visibility=["read", "create", "update", "delete", "query"]
    )
    """The unique identifier of the user who last modified the entity."""
    created_at: Optional[str] = rest_field(name="createdAt", visibility=["read", "create", "update", "delete", "query"])
    """The timestamp when the entity was created."""
    created_by: Optional[str] = rest_field(name="createdBy", visibility=["read", "create", "update", "delete", "query"])
    """The unique identifier of the user who created the entity."""

    @overload
    def __init__(
        self,
        *,
        last_modified_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        created_at: Optional[str] = None,
        created_by: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Term(_Model):
    """Microsoft Purview Data Governance Catalog Model Term.

    :ivar status: The status of the term. Required. Known values are: "DRAFT", "PUBLISHED", and
     "EXPIRED".
    :vartype status: str or ~purviewunifiedcatalog.models.CatalogModelStatus
    :ivar id: The unique identifier of the term. Required.
    :vartype id: str
    :ivar name: The name of the term. Required.
    :vartype name: str
    :ivar system_data: The system data of the term.
    :vartype system_data: ~purviewunifiedcatalog.models.CatalogModelSystemDataWithExpired
    :ivar description: The description of the term.
    :vartype description: str
    :ivar contacts: The contacts associated with the term.
    :vartype contacts: ~purviewunifiedcatalog.models.ContactsMap
    :ivar domain: The domain associated with the term. Required.
    :vartype domain: str
    :ivar parent_id: The parent term identifier.
    :vartype parent_id: str
    :ivar acronyms: The list of acronyms for the term.
    :vartype acronyms: list[str]
    :ivar resources: The resources associated with the term.
    :vartype resources: list[~purviewunifiedcatalog.models.CatalogModelTermResource]
    :ivar is_leaf: Whether the term is a leaf node.
    :vartype is_leaf: bool
    :ivar managed_attributes: The managed attributes associated with the term.
    :vartype managed_attributes: list[~purviewunifiedcatalog.models.CatalogModelManagedAttribute]
    """

    status: Union[str, "_models.CatalogModelStatus"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The status of the term. Required. Known values are: \"DRAFT\", \"PUBLISHED\", and \"EXPIRED\"."""
    id: str = rest_field(visibility=["create"])
    """The unique identifier of the term. Required."""
    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name of the term. Required."""
    system_data: Optional["_models.CatalogModelSystemDataWithExpired"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """The system data of the term."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The description of the term."""
    contacts: Optional["_models.ContactsMap"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The contacts associated with the term."""
    domain: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The domain associated with the term. Required."""
    parent_id: Optional[str] = rest_field(name="parentId", visibility=["read", "create", "update", "delete", "query"])
    """The parent term identifier."""
    acronyms: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The list of acronyms for the term."""
    resources: Optional[list["_models.CatalogModelTermResource"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """The resources associated with the term."""
    is_leaf: Optional[bool] = rest_field(name="isLeaf", visibility=["read", "create", "update", "delete", "query"])
    """Whether the term is a leaf node."""
    managed_attributes: Optional[list["_models.CatalogModelManagedAttribute"]] = rest_field(
        name="managedAttributes", visibility=["read", "create", "update", "delete", "query"]
    )
    """The managed attributes associated with the term."""

    @overload
    def __init__(
        self,
        *,
        status: Union[str, "_models.CatalogModelStatus"],
        id: str,  # pylint: disable=redefined-builtin
        name: str,
        domain: str,
        system_data: Optional["_models.CatalogModelSystemDataWithExpired"] = None,
        description: Optional[str] = None,
        contacts: Optional["_models.ContactsMap"] = None,
        parent_id: Optional[str] = None,
        acronyms: Optional[list[str]] = None,
        resources: Optional[list["_models.CatalogModelTermResource"]] = None,
        is_leaf: Optional[bool] = None,
        managed_attributes: Optional[list["_models.CatalogModelManagedAttribute"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class TermFacetRequest(_Model):
    """TermFacetRequest.

    :ivar ids: To filter by Ids.
    :vartype ids: list[str]
    :ivar domain_ids: To filter by domain Ids.
    :vartype domain_ids: list[str]
    :ivar name_keyword: To filter by name keyword.
    :vartype name_keyword: str
    :ivar owners: To filter by owners.
    :vartype owners: list[str]
    :ivar acronyms: To filter by acronyms.
    :vartype acronyms: list[str]
    :ivar status: To filter by status. Known values are: "Draft", "Published", and "Expired".
    :vartype status: str or ~purviewunifiedcatalog.models.SharedEntityStatus
    :ivar multi_status: To filter by multiple status.
    :vartype multi_status: list[str or ~purviewunifiedcatalog.models.SharedEntityStatus]
    :ivar facets: To filter by multiple facets.
    :vartype facets: list[~purviewunifiedcatalog.models.ModelsFacetRequestObject]
    """

    ids: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by Ids."""
    domain_ids: Optional[list[str]] = rest_field(
        name="domainIds", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by domain Ids."""
    name_keyword: Optional[str] = rest_field(
        name="nameKeyword", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by name keyword."""
    owners: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by owners."""
    acronyms: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """To filter by acronyms."""
    status: Optional[Union[str, "_models.SharedEntityStatus"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by status. Known values are: \"Draft\", \"Published\", and \"Expired\"."""
    multi_status: Optional[list[Union[str, "_models.SharedEntityStatus"]]] = rest_field(
        name="multiStatus", visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by multiple status."""
    facets: Optional[list["_models.ModelsFacetRequestObject"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """To filter by multiple facets."""

    @overload
    def __init__(
        self,
        *,
        ids: Optional[list[str]] = None,
        domain_ids: Optional[list[str]] = None,
        name_keyword: Optional[str] = None,
        owners: Optional[list[str]] = None,
        acronyms: Optional[list[str]] = None,
        status: Optional[Union[str, "_models.SharedEntityStatus"]] = None,
        multi_status: Optional[list[Union[str, "_models.SharedEntityStatus"]]] = None,
        facets: Optional[list["_models.ModelsFacetRequestObject"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class TermQueryRequest(_Model):
    """Term query request model.

    :ivar skip: Number of items to skip.
    :vartype skip: int
    :ivar top: Number of items to return.
    :vartype top: int
    :ivar orderby: Order by specifications for the query.
    :vartype orderby: list[~purviewunifiedcatalog.models.CatalogApiServiceOrderBy]
    :ivar ids: Filter by term IDs.
    :vartype ids: list[str]
    :ivar domain_ids: Filter by domain IDs.
    :vartype domain_ids: list[str]
    :ivar name_keyword: Filter by name keyword.
    :vartype name_keyword: str
    :ivar status: Filter by term status. Known values are: "DRAFT", "PUBLISHED", and "EXPIRED".
    :vartype status: str or ~purviewunifiedcatalog.models.CatalogModelStatus
    :ivar multi_status: Filter by multiple term statuses.
    :vartype multi_status: list[str or ~purviewunifiedcatalog.models.CatalogModelStatus]
    :ivar owners: Filter by term owners.
    :vartype owners: list[str]
    :ivar acronyms: Filter by term acronyms.
    :vartype acronyms: list[str]
    :ivar managed_attributes: Filter by managed attributes.
    :vartype managed_attributes:
     list[~purviewunifiedcatalog.models.SharedSearchManageAttributeSearchFilter]
    """

    skip: Optional[int] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Number of items to skip."""
    top: Optional[int] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Number of items to return."""
    orderby: Optional[list["_models.CatalogApiServiceOrderBy"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Order by specifications for the query."""
    ids: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Filter by term IDs."""
    domain_ids: Optional[list[str]] = rest_field(
        name="domainIds", visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by domain IDs."""
    name_keyword: Optional[str] = rest_field(
        name="nameKeyword", visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by name keyword."""
    status: Optional[Union[str, "_models.CatalogModelStatus"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by term status. Known values are: \"DRAFT\", \"PUBLISHED\", and \"EXPIRED\"."""
    multi_status: Optional[list[Union[str, "_models.CatalogModelStatus"]]] = rest_field(
        name="multiStatus", visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by multiple term statuses."""
    owners: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Filter by term owners."""
    acronyms: Optional[list[str]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Filter by term acronyms."""
    managed_attributes: Optional[list["_models.SharedSearchManageAttributeSearchFilter"]] = rest_field(
        name="managedAttributes", visibility=["read", "create", "update", "delete", "query"]
    )
    """Filter by managed attributes."""

    @overload
    def __init__(
        self,
        *,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        orderby: Optional[list["_models.CatalogApiServiceOrderBy"]] = None,
        ids: Optional[list[str]] = None,
        domain_ids: Optional[list[str]] = None,
        name_keyword: Optional[str] = None,
        status: Optional[Union[str, "_models.CatalogModelStatus"]] = None,
        multi_status: Optional[list[Union[str, "_models.CatalogModelStatus"]]] = None,
        owners: Optional[list[str]] = None,
        acronyms: Optional[list[str]] = None,
        managed_attributes: Optional[list["_models.SharedSearchManageAttributeSearchFilter"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class TermRelationship(_Model):
    """TermRelationship.

    :ivar system_data: System metadata for the term relationship.
    :vartype system_data: ~purviewunifiedcatalog.models.SystemData
    :ivar description: description for the term relationship.
    :vartype description: str
    :ivar entity_id: The unique identifier of the entity. Required.
    :vartype entity_id: str
    :ivar relationship_type: The type of the term relationship. Known values are: "Related",
     "Synonym", and "Parent".
    :vartype relationship_type: str or ~purviewunifiedcatalog.models.TermRelationshipType
    """

    system_data: Optional["_models.SystemData"] = rest_field(
        name="systemData", visibility=["read", "create", "update", "delete", "query"]
    )
    """System metadata for the term relationship."""
    description: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """description for the term relationship."""
    entity_id: str = rest_field(name="entityId", visibility=["create"])
    """The unique identifier of the entity. Required."""
    relationship_type: Optional[Union[str, "_models.TermRelationshipType"]] = rest_field(
        name="relationshipType", visibility=["read", "create", "update", "delete", "query"]
    )
    """The type of the term relationship. Known values are: \"Related\", \"Synonym\", and \"Parent\"."""

    @overload
    def __init__(
        self,
        *,
        entity_id: str,
        system_data: Optional["_models.SystemData"] = None,
        description: Optional[str] = None,
        relationship_type: Optional[Union[str, "_models.TermRelationshipType"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
