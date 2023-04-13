from aws_cdk import (
    Stack,
    aws_route53 as route53
)
from constructs import Construct

class R53Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        build_dns_name = "www.agv.gg"

        hosted_zone = route53.PublicHostedZone(self, build_dns_name,
            zone_name=build_dns_name
        )

        self.hosted_zone = hosted_zone