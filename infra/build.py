from aws_cdk import core
from aws_cdk import aws_ecr as ecr
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_ecs_patterns as ecs_patterns


class DjangoEcsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # ECR Repository
        django_ecr_repo = ecr.Repository(self, "DjangoEcrRepo")

        # ECS Cluster
        ecs_cluster = ecs.Cluster(self, "DjangoEcsCluster")

        # Fargate Task Definition
        fargate_task_definition = ecs.FargateTaskDefinition(
            self, "DjangoTaskDef")
        container = fargate_task_definition.add_container(
            "DjangoContainer",
            image=ecs.ContainerImage.from_ecr_repository(django_ecr_repo),
            memory_limit_mib=512,
            cpu=256
        )
        container.add_port_mappings(ecs.PortMapping(container_port=8000))

        # Fargate Service
        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "DjangoService",
            cluster=ecs_cluster,
            task_definition=fargate_task_definition,
            public_load_balancer=True
        )


app = core.App()
DjangoEcsStack(app, "DjangoEcsStack")
app.synth()
