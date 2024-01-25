'''
# AMZN::SDC Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.amzn_sdc as amzn_sdc
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SDC construct libraries](https://constructs.dev/search?q=sdc)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AMZN::SDC resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AMZN_SDC.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AMZN::SDC](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AMZN_SDC.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    IInspectable as _IInspectable_c2943556,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnDeployment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.amzn_sdc.CfnDeployment",
):
    '''Resource Type definition for AMZN::SDC::Deployment.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html
    :cloudformationResource: AMZN::SDC::Deployment
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import amzn_sdc
        
        cfn_deployment = amzn_sdc.CfnDeployment(self, "MyCfnDeployment",
            config_name="configName",
            dimension="dimension",
            s3_bucket="s3Bucket",
            s3_key="s3Key",
            stage="stage",
        
            # the properties below are optional
            pipeline_id="pipelineId",
            target_region_override="targetRegionOverride"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        config_name: builtins.str,
        dimension: builtins.str,
        s3_bucket: builtins.str,
        s3_key: builtins.str,
        stage: builtins.str,
        pipeline_id: typing.Optional[builtins.str] = None,
        target_region_override: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param config_name: 
        :param dimension: 
        :param s3_bucket: 
        :param s3_key: 
        :param stage: 
        :param pipeline_id: 
        :param target_region_override: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ed15b27cd3bac1ff152e013e411c40e85c5a4e1b47f1191bffac4eb1dc00a7a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeploymentProps(
            config_name=config_name,
            dimension=dimension,
            s3_bucket=s3_bucket,
            s3_key=s3_key,
            stage=stage,
            pipeline_id=pipeline_id,
            target_region_override=target_region_override,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7480e3be8419f3add77cdc75e148f12141663545557935b5702edf0033ce3059)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68739bd722c642a322bc1ee03008e34395f2d2eefba71a0ecd1597de9c029383)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="configName")
    def config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configName"))

    @config_name.setter
    def config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba645b17830c504393df49766927a379567d35b7e181282dfb05d29e1da7787f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configName", value)

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dimension"))

    @dimension.setter
    def dimension(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbc2024d8801bfb0886e2954e85af0ac50d0c16248ca97e9bd5d56a758f40fc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimension", value)

    @builtins.property
    @jsii.member(jsii_name="s3Bucket")
    def s3_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Bucket"))

    @s3_bucket.setter
    def s3_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1247316131c5cfc2ee92db06405e0aff51e01239f3819dad5be15d04f81cf520)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="s3Key")
    def s3_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3Key"))

    @s3_key.setter
    def s3_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35c498ce0cf6e4d4103dac38a6e391c411c29f967e52192fd964864de37eeb01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Key", value)

    @builtins.property
    @jsii.member(jsii_name="stage")
    def stage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stage"))

    @stage.setter
    def stage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a7eeb65d39ba2be20dec1ee8a811e2f705a31963d5896ed1a01df932eed01cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stage", value)

    @builtins.property
    @jsii.member(jsii_name="pipelineId")
    def pipeline_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pipelineId"))

    @pipeline_id.setter
    def pipeline_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3ee1598ada7912fd052405dbfc217aac7c7ec00606b5dd1db8764919f278ed0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineId", value)

    @builtins.property
    @jsii.member(jsii_name="targetRegionOverride")
    def target_region_override(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetRegionOverride"))

    @target_region_override.setter
    def target_region_override(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39df44d1a6e2a49cec602a2465ea56ec01690262a80f9ddd1050849c6567fcd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetRegionOverride", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.amzn_sdc.CfnDeploymentProps",
    jsii_struct_bases=[],
    name_mapping={
        "config_name": "configName",
        "dimension": "dimension",
        "s3_bucket": "s3Bucket",
        "s3_key": "s3Key",
        "stage": "stage",
        "pipeline_id": "pipelineId",
        "target_region_override": "targetRegionOverride",
    },
)
class CfnDeploymentProps:
    def __init__(
        self,
        *,
        config_name: builtins.str,
        dimension: builtins.str,
        s3_bucket: builtins.str,
        s3_key: builtins.str,
        stage: builtins.str,
        pipeline_id: typing.Optional[builtins.str] = None,
        target_region_override: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeployment``.

        :param config_name: 
        :param dimension: 
        :param s3_bucket: 
        :param s3_key: 
        :param stage: 
        :param pipeline_id: 
        :param target_region_override: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import amzn_sdc
            
            cfn_deployment_props = amzn_sdc.CfnDeploymentProps(
                config_name="configName",
                dimension="dimension",
                s3_bucket="s3Bucket",
                s3_key="s3Key",
                stage="stage",
            
                # the properties below are optional
                pipeline_id="pipelineId",
                target_region_override="targetRegionOverride"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e0c030e7b5941ee63d7c357bf46f61b61dbf211781b51cc262493b9077421f4)
            check_type(argname="argument config_name", value=config_name, expected_type=type_hints["config_name"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
            check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
            check_type(argname="argument pipeline_id", value=pipeline_id, expected_type=type_hints["pipeline_id"])
            check_type(argname="argument target_region_override", value=target_region_override, expected_type=type_hints["target_region_override"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_name": config_name,
            "dimension": dimension,
            "s3_bucket": s3_bucket,
            "s3_key": s3_key,
            "stage": stage,
        }
        if pipeline_id is not None:
            self._values["pipeline_id"] = pipeline_id
        if target_region_override is not None:
            self._values["target_region_override"] = target_region_override

    @builtins.property
    def config_name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html#cfn-sdc-deployment-configname
        '''
        result = self._values.get("config_name")
        assert result is not None, "Required property 'config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimension(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html#cfn-sdc-deployment-dimension
        '''
        result = self._values.get("dimension")
        assert result is not None, "Required property 'dimension' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_bucket(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html#cfn-sdc-deployment-s3bucket
        '''
        result = self._values.get("s3_bucket")
        assert result is not None, "Required property 's3_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_key(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html#cfn-sdc-deployment-s3key
        '''
        result = self._values.get("s3_key")
        assert result is not None, "Required property 's3_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stage(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html#cfn-sdc-deployment-stage
        '''
        result = self._values.get("stage")
        assert result is not None, "Required property 'stage' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pipeline_id(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html#cfn-sdc-deployment-pipelineid
        '''
        result = self._values.get("pipeline_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_region_override(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sdc-deployment.html#cfn-sdc-deployment-targetregionoverride
        '''
        result = self._values.get("target_region_override")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeploymentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDeployment",
    "CfnDeploymentProps",
]

publication.publish()

def _typecheckingstub__4ed15b27cd3bac1ff152e013e411c40e85c5a4e1b47f1191bffac4eb1dc00a7a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    config_name: builtins.str,
    dimension: builtins.str,
    s3_bucket: builtins.str,
    s3_key: builtins.str,
    stage: builtins.str,
    pipeline_id: typing.Optional[builtins.str] = None,
    target_region_override: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7480e3be8419f3add77cdc75e148f12141663545557935b5702edf0033ce3059(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68739bd722c642a322bc1ee03008e34395f2d2eefba71a0ecd1597de9c029383(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba645b17830c504393df49766927a379567d35b7e181282dfb05d29e1da7787f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbc2024d8801bfb0886e2954e85af0ac50d0c16248ca97e9bd5d56a758f40fc5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1247316131c5cfc2ee92db06405e0aff51e01239f3819dad5be15d04f81cf520(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35c498ce0cf6e4d4103dac38a6e391c411c29f967e52192fd964864de37eeb01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a7eeb65d39ba2be20dec1ee8a811e2f705a31963d5896ed1a01df932eed01cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3ee1598ada7912fd052405dbfc217aac7c7ec00606b5dd1db8764919f278ed0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39df44d1a6e2a49cec602a2465ea56ec01690262a80f9ddd1050849c6567fcd9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e0c030e7b5941ee63d7c357bf46f61b61dbf211781b51cc262493b9077421f4(
    *,
    config_name: builtins.str,
    dimension: builtins.str,
    s3_bucket: builtins.str,
    s3_key: builtins.str,
    stage: builtins.str,
    pipeline_id: typing.Optional[builtins.str] = None,
    target_region_override: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
