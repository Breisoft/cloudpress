'''
# AWS::CodeTest Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_codetest as codetest
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for CodeTest construct libraries](https://constructs.dev/search?q=codetest)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::CodeTest resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeTest.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::CodeTest](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeTest.html).

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
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnPersistentConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codetest.CfnPersistentConfiguration",
):
    '''Resource Type definition for AWS::CodeTest::PersistentConfiguration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-persistentconfiguration.html
    :cloudformationResource: AWS::CodeTest::PersistentConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codetest as codetest
        
        cfn_persistent_configuration = codetest.CfnPersistentConfiguration(self, "MyCfnPersistentConfiguration",
            results_role_arn="resultsRoleArn",
        
            # the properties below are optional
            name="name",
            version="version",
            vpc_config=codetest.CfnPersistentConfiguration.VpcConfigProperty(
                security_group_ids=["securityGroupIds"],
                subnets=["subnets"]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        results_role_arn: builtins.str,
        name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPersistentConfiguration.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param results_role_arn: 
        :param name: 
        :param version: 
        :param vpc_config: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cad5062810de71ae8e1fd28a416600ec6510615d6b89a8d3c12546f78634c0f9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPersistentConfigurationProps(
            results_role_arn=results_role_arn,
            name=name,
            version=version,
            vpc_config=vpc_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccd63e91af2eb8ebdfbacb79be24ff2221c0e7c102d0ebda08998057777ead4a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e6872a5580c0d64dce57e87557a4a6aedf0685637c9e531de4f9a9a212b6187)
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
    @jsii.member(jsii_name="resultsRoleArn")
    def results_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resultsRoleArn"))

    @results_role_arn.setter
    def results_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43f2305422477b4f72b47deeae6b64a04845eb14e7af66b2c5189a4cc39e0632)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resultsRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d19a205d82a49a3a035ea67f1dfb0eb88334cccba78bb5a10c3e59c0f517fc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "version"))

    @version.setter
    def version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76be25692bf189a6b695397e4dfd18053d79a944f6fba0dcd10ca7e6809750a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPersistentConfiguration.VpcConfigProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPersistentConfiguration.VpcConfigProperty"]], jsii.get(self, "vpcConfig"))

    @vpc_config.setter
    def vpc_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPersistentConfiguration.VpcConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff2888dfb5c60e8b8dbc3cb51b50d77e4b11854e00ac8be4a3bafd46b683b75f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codetest.CfnPersistentConfiguration.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param security_group_ids: 
            :param subnets: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codetest-persistentconfiguration-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codetest as codetest
                
                vpc_config_property = codetest.CfnPersistentConfiguration.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7b9392979d202e89e968931f5bb84134d33c7c81e72d6dc3fc4a8c4a8dd380a4)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnets is not None:
                self._values["subnets"] = subnets

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codetest-persistentconfiguration-vpcconfig.html#cfn-codetest-persistentconfiguration-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnets(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codetest-persistentconfiguration-vpcconfig.html#cfn-codetest-persistentconfiguration-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codetest.CfnPersistentConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "results_role_arn": "resultsRoleArn",
        "name": "name",
        "version": "version",
        "vpc_config": "vpcConfig",
    },
)
class CfnPersistentConfigurationProps:
    def __init__(
        self,
        *,
        results_role_arn: builtins.str,
        name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPersistentConfiguration.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPersistentConfiguration``.

        :param results_role_arn: 
        :param name: 
        :param version: 
        :param vpc_config: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-persistentconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codetest as codetest
            
            cfn_persistent_configuration_props = codetest.CfnPersistentConfigurationProps(
                results_role_arn="resultsRoleArn",
            
                # the properties below are optional
                name="name",
                version="version",
                vpc_config=codetest.CfnPersistentConfiguration.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnets=["subnets"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59d7b9f3b3c14b07cacea97cc2e09f95e72302d9c0b5ea71bd70aa198d383f0e)
            check_type(argname="argument results_role_arn", value=results_role_arn, expected_type=type_hints["results_role_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "results_role_arn": results_role_arn,
        }
        if name is not None:
            self._values["name"] = name
        if version is not None:
            self._values["version"] = version
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def results_role_arn(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-persistentconfiguration.html#cfn-codetest-persistentconfiguration-resultsrolearn
        '''
        result = self._values.get("results_role_arn")
        assert result is not None, "Required property 'results_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-persistentconfiguration.html#cfn-codetest-persistentconfiguration-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-persistentconfiguration.html#cfn-codetest-persistentconfiguration-version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPersistentConfiguration.VpcConfigProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-persistentconfiguration.html#cfn-codetest-persistentconfiguration-vpcconfig
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPersistentConfiguration.VpcConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPersistentConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSeries(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codetest.CfnSeries",
):
    '''Resource Type definition for AWS::CodeTest::Series.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-series.html
    :cloudformationResource: AWS::CodeTest::Series
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codetest as codetest
        
        # run_definition: Any
        
        cfn_series = codetest.CfnSeries(self, "MyCfnSeries",
            persistent_configuration_id="persistentConfigurationId",
            run_definition=run_definition,
            state="state",
        
            # the properties below are optional
            name="name"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        persistent_configuration_id: builtins.str,
        run_definition: typing.Any,
        state: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param persistent_configuration_id: 
        :param run_definition: 
        :param state: 
        :param name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e4c4a515f26312f3844834ada5021cdfd58ee8b7e773009cdfa635f52bb0549)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSeriesProps(
            persistent_configuration_id=persistent_configuration_id,
            run_definition=run_definition,
            state=state,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df00296f4abcafee1091a3472368de0801c4d104aaf0da5e91cec2c3674736bb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__95350aa4223a7e92142bcb8aa09cdb0b1b40cdb5e2f22685972bf728d7ac7cf4)
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
    @jsii.member(jsii_name="persistentConfigurationId")
    def persistent_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "persistentConfigurationId"))

    @persistent_configuration_id.setter
    def persistent_configuration_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fca40f592ca3b3af2ad5c90e19eb2218b0ae92c82fa27320ba4db0826bae1417)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "persistentConfigurationId", value)

    @builtins.property
    @jsii.member(jsii_name="runDefinition")
    def run_definition(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "runDefinition"))

    @run_definition.setter
    def run_definition(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a882de0fa21a24de52f7e8b057cc371e8fd3acdb17fd65ebf14ff225b6136200)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runDefinition", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1c4eb51de7e6e78957a12840bfb13a8af10e08cfecf981c75ad28354600a36b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59d4e290104f4dde73c3b122ba4e00181988662058825d26c58b358e28873346)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codetest.CfnSeriesProps",
    jsii_struct_bases=[],
    name_mapping={
        "persistent_configuration_id": "persistentConfigurationId",
        "run_definition": "runDefinition",
        "state": "state",
        "name": "name",
    },
)
class CfnSeriesProps:
    def __init__(
        self,
        *,
        persistent_configuration_id: builtins.str,
        run_definition: typing.Any,
        state: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSeries``.

        :param persistent_configuration_id: 
        :param run_definition: 
        :param state: 
        :param name: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-series.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codetest as codetest
            
            # run_definition: Any
            
            cfn_series_props = codetest.CfnSeriesProps(
                persistent_configuration_id="persistentConfigurationId",
                run_definition=run_definition,
                state="state",
            
                # the properties below are optional
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c906d8031c767851bc9b6793505f5b198029d76cfbf56fd0d45a04acae867176)
            check_type(argname="argument persistent_configuration_id", value=persistent_configuration_id, expected_type=type_hints["persistent_configuration_id"])
            check_type(argname="argument run_definition", value=run_definition, expected_type=type_hints["run_definition"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "persistent_configuration_id": persistent_configuration_id,
            "run_definition": run_definition,
            "state": state,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def persistent_configuration_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-series.html#cfn-codetest-series-persistentconfigurationid
        '''
        result = self._values.get("persistent_configuration_id")
        assert result is not None, "Required property 'persistent_configuration_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_definition(self) -> typing.Any:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-series.html#cfn-codetest-series-rundefinition
        '''
        result = self._values.get("run_definition")
        assert result is not None, "Required property 'run_definition' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def state(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-series.html#cfn-codetest-series-state
        '''
        result = self._values.get("state")
        assert result is not None, "Required property 'state' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codetest-series.html#cfn-codetest-series-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSeriesProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnPersistentConfiguration",
    "CfnPersistentConfigurationProps",
    "CfnSeries",
    "CfnSeriesProps",
]

publication.publish()

def _typecheckingstub__cad5062810de71ae8e1fd28a416600ec6510615d6b89a8d3c12546f78634c0f9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    results_role_arn: builtins.str,
    name: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPersistentConfiguration.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccd63e91af2eb8ebdfbacb79be24ff2221c0e7c102d0ebda08998057777ead4a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e6872a5580c0d64dce57e87557a4a6aedf0685637c9e531de4f9a9a212b6187(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43f2305422477b4f72b47deeae6b64a04845eb14e7af66b2c5189a4cc39e0632(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d19a205d82a49a3a035ea67f1dfb0eb88334cccba78bb5a10c3e59c0f517fc6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76be25692bf189a6b695397e4dfd18053d79a944f6fba0dcd10ca7e6809750a1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff2888dfb5c60e8b8dbc3cb51b50d77e4b11854e00ac8be4a3bafd46b683b75f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPersistentConfiguration.VpcConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b9392979d202e89e968931f5bb84134d33c7c81e72d6dc3fc4a8c4a8dd380a4(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59d7b9f3b3c14b07cacea97cc2e09f95e72302d9c0b5ea71bd70aa198d383f0e(
    *,
    results_role_arn: builtins.str,
    name: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPersistentConfiguration.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e4c4a515f26312f3844834ada5021cdfd58ee8b7e773009cdfa635f52bb0549(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    persistent_configuration_id: builtins.str,
    run_definition: typing.Any,
    state: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df00296f4abcafee1091a3472368de0801c4d104aaf0da5e91cec2c3674736bb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95350aa4223a7e92142bcb8aa09cdb0b1b40cdb5e2f22685972bf728d7ac7cf4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fca40f592ca3b3af2ad5c90e19eb2218b0ae92c82fa27320ba4db0826bae1417(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a882de0fa21a24de52f7e8b057cc371e8fd3acdb17fd65ebf14ff225b6136200(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1c4eb51de7e6e78957a12840bfb13a8af10e08cfecf981c75ad28354600a36b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59d4e290104f4dde73c3b122ba4e00181988662058825d26c58b358e28873346(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c906d8031c767851bc9b6793505f5b198029d76cfbf56fd0d45a04acae867176(
    *,
    persistent_configuration_id: builtins.str,
    run_definition: typing.Any,
    state: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
