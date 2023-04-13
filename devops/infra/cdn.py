from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_route53 as route53,
    aws_cloudfront_origins as origins,
    aws_certificatemanager as acm,
    aws_route53_targets as targets,
)
from constructs import Construct

class CdnStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, agv_bucket: s3.IBucket, hosted_zone: route53.PublicHostedZone, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        build_dns_name = "www.agv.gg"

        cert = acm.DnsValidatedCertificate(self, build_dns_name + "-cert",
            domain_name=build_dns_name,
            hosted_zone=hosted_zone
        )

        agv_cdn = cloudfront.Distribution(self, build_dns_name + "-cdn",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(agv_bucket),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.HTTPS_ONLY,
                cache_policy=cloudfront.CachePolicy.CACHING_OPTIMIZED,
                allowed_methods=cloudfront.AllowedMethods.ALLOW_GET_HEAD
            ),
            price_class=cloudfront.PriceClass.PRICE_CLASS_100,
            domain_names=[build_dns_name],
            default_root_object="index.html",
            certificate=cert
        )

        route53.ARecord( self, "cdn-agv-pointer",
            zone=hosted_zone,
            target=route53.RecordTarget.from_alias(targets.CloudFrontTarget(agv_cdn) )
        )