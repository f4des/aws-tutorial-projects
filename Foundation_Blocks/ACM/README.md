##Security Certificate Creation with ACM 

The first thing we're going to need before we begin is to have a valid security certificate that we can hand out to our ALB, API Gateway, and EC2 instance. There can also be a bit of a wait time for the provisioning of this, so that's why we're tackling it first.

We're going to use an Amazon Issued certificate for this to make our lives easy.

1. Navigate to AWS Certificate Manger
2. Click "Request a certificate"
3. Click "Request a public certificate"
4. Now we get to choose a domain name. I like to use a wildcard here so you only have to create one certificate, but however you decide to allocate your certificates is up to you.
5. We're going to use DNS validation for this.
6. Review, confirm and request.

-- Image Goes here --

TODO
```If my Route53 Hosted zone was "allmydomains.com." this would be created a certificate that would be usable for every subdomain that I wanted to use in this hosted zone ```

This might take a little bit of time for the records to be updated & added to your Route53 hosted zone, and you may need to click the "Create record in Route 53" in the domain sub-menu like in the screenshot below.

--- Imge Goes Here ---