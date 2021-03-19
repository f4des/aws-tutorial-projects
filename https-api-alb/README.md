#HTTP API Gateway Integrated with an internal ALB using a HTTPS listener 

Have you ever wanted to point your API Gateway to an internal ALB, but as soon as you try to point it towards a listener on 443 you start getting 5xx errors, and the idea of having the traffic give up TLS even inside your network is something that makes your security folks explode? Well I'm here to show you how to set up your HTTP API Gateway so that you can route traffic the whole way through your network under the warm embrace of TLS.

This set up will generally be focused around the setting up of the API Gateway and the Application Load Balancer. To get there I'll cover VPC setup and configuration, I'll include a part about how to install your SSL certificates on an EC2 backend as an example.

###Things we'll cover;

- Application Load Balancer setup
- Route53 configuration
- API Gateway creation

### Knowledge Assumptions;

- Basic understanding of AWS & it's terminology


### AWS Pre-requisites
- Security Certificate [Creation](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html) with ACM 
- VPC & Subnet setup and configuration (Foundation Block available)
- A [Route53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingHostedZone.html) hosted zone


### Later on down the road when I've got time;
- Cloudformation templates
- CLI-based instructions
- Maybe swagger templates too

### Let's begin!


