from aws_cdk import Duration, Stack
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_rds as rds
from constructs import Construct

class CdkRdsStack(Stack):

    def __init__(self, scope: Construct, id: str, vpc, asg_security_groups, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Ceate Aurora Cluster with 2 instances with CDK High Level API
        # Secrets Manager auto generate and keep the password, don't put password in cdk code directly
        # db_Aurora_cluster = rds.DatabaseCluster(self, "MyAurora",
        #                                         default_database_name="MyAurora",
        #                                         engine=rds.DatabaseClusterEngine.arora_mysql(
        #                                             version=rds.AuroraMysqlEngineVersion.VER_5_7_12
        #                                         )
        #                                         instance_props=rds.InstanceProps(
        #                                             vpc=vpc,
        #                                             vpc_subnets=ec2.SubnetSelection(subnet_group_name="DB"),
        #                                             instance_type=ec2.InstanceType(instance_type_identifier="t2.small")
        #                                         ),
        #                                         instances=2,
        #                                         parameter_group=rds.ClusterParameterGroup.from_parameter_group_name(
        #                                             self, "para-group-aurora",
        #                                             parameter_group_name="default.aurora-mysql5.7"
        #                                         ),
        #                                         )
        # for asg_sg in asg_security_groups:
        #     db_Aurora_cluster.connections.allow_default_port_from(asg_sg, "EC2 Autoscaling Group access Aurora")

        # Alternatively, create MySQL RDS with CDK High Level API
        db_postgres = rds.DatabaseInstance(self, "qwarkedb",
                                             engine=rds.DatabaseInstanceEngine.postgres(
                                                 version=rds.PostgresEngineVersion.VER_14_3
                                             ),
                                             instance_type=ec2.InstanceType.of(
                                                 ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
                                             vpc=vpc,
                                             vpc_subnets=ec2.SubnetSelection(subnet_group_name="DB"),
                                             multi_az=True,
                                             allocated_storage=100,
                                             storage_type=rds.StorageType.GP2,
                                             
                                             deletion_protection=False,
                                             delete_automated_backups=False,
                                             backup_retention=Duration.days(7),cloudwatch_logs_exports=["postgresql", "upgrade"],
                                             parameter_group=rds.ParameterGroup.from_parameter_group_name(
                                                 self, "para-group-psql",
                                                 parameter_group_name="default.postgres14"
                                             )
                                             )
        for asg_sg in asg_security_groups:
            db_postgres.connections.allow_default_port_from(asg_sg, "EC2 Autoscaling Group access PSQL")
