# Foundation Block - VPC

Here you'll find a setup guide for a VPC that the main samples will be built on top of. You'll also find a cloudformation template in case you just want to fire & forget setting up the VPC, and you're not interested in an explanation of any of the settings, as well as a bunch of CLI commands you can use to set up the VPC if you're that way inclined.

### Assumptions;

- Basic understanding of AWS & it's terminology
- Basic understanding of networking concepts

### AWS Pre-requisites

- None!


### Let's begin!


First thing we need to do is log in to our AWS account and navigate over to the VPC service. Once we're there, we can click "Create VPC".

#### VPC Settings

Here we see the following settings;

- Name tag: Pretty self explanatory, it's the name you'd like to give your VPC.
- IPv4 CIDR block: This one is the only mandatory setting. You need to associate an IPv4 block wth your VPC. The only major limitation on this is that it needs to be at it's largest a /16 block of addresses, and at it's smallest a /28 block. I'm going to use "13.37.0.0/16".
- IPv6 CIDR block: You can decide if you want to associate an IPv6 CIDR block with your VPC. The options here are for Amazon to provide you with an IPv6 block (you don't get to choose what it is), or to associate a an IPv6 block you own, which is a bit of a mission, and something we'll just pretend doesn't exist for now.
- Tenancy: By choosing dedicated, this ensures all the EC2 instances you launch inside your VPC will run on hardware that is dedicated to you and no one else. This isn't really necessary for most use cases, so like the IPv6 setting, we'll just ignore this and leave it as "Default" as well.
- Click Create!

#### Bonus Settings!

There are a couple of extra settings that we're just going to confirm are switched on before we finish up. From the VPC menu, we can access these by selecting the blue check box next to our newly created VPC and then clicking the "Actions" drop down menu.

- DNS Resolution: We want this to be enabled. When this is enabled, it allows queries to the Amazon DNS servers to perform DNS lookups, which is a useful thing to have unless we plan on providing our own DNS servers.
- DNS Hostnames: We also want this to be true! When this is selected, this allows instances in our VPC to be assigned assigned public DNS hostnames, but it also needs DNS resolution to be enabled.


### Subnet Set up


Now we are going to set up four subnets, we're going to have two private and two public ones. This will come in handy later on when we want to deploy Lambda functions, or Load Balancers and other services that generally like to be deployed in multiple AZs at once.

####  Subnet Settings

- Name tag: Once again, whatever you feel like, I like to keep things simple and will be using "Public Subnet 1" & "Public Subnet 2", and "Private Subnet 1" & "Private Subnet 2" for my private subnets.
- VPC: You choose what VPC you want the subnets to be associated with. In this case, the VPC we just created.
- Availability Zone: If you have a preference as to which AZ this subnet is deployed in, you can choose that here, otherwise leave it as default.
- IPv4 CIDR block: Here you get to choose the IP block the subnet will use, similar to when we chose for a VPC. For simplicity's sake I'm going to use "13.37.1.0/24" & "13.37.2.0/24" for my Public Subnets, and "13.37.3.0/24" & "13.37.4.0/24" for my Private subnets.

#### Internet Gateway

Now, before we getting on to routing tables, we need to create ourselves an interet gateway that we can attach to our VPC. So from the VPC service menu, on the left hand side, we're going to skip "Route Tables" for the moment and click on "Internet Gateways".

- Click Create internet gateway
- Name it something and click "Create internet gateway"
- Now on the top right you should see "Attach to VPC" click that
- If you don't, you can click Actions -> Attach to VPC
- Choose our VPC from the drop down menu
- Attach internet gateway

#### NAT Gateways

Now we have an internet gateway all set up, we also need to create at least one NAT gateway for our VPC. Since we have two public subnets, if we wanted to go down the road of create highly available infrastructure, we would create one NAT gateway for each subnet, but for this example, we're just going to use the one. So, from the side bar, click "NAT Gateways"

- Create NAT Gateway
- Name it if you fancy
- !! Choose a subnet !! This part is important, we need to make sure that the NAT gateway is associated with one of our public subnets so we can have internet access from our private ones.
- Allocate Elastic IP: An elastic IP is just a cool way of saying static IP address for our use case.
- Create NAT Gateway

#### Route tables

Now we have a VPC, subnets, an internet gateway and a NAT gateway setup, it's time to put in place what mkes our private subnets private, and our public subnets public... routing tables! Left hand menu, up to "Route Tables".

- Create route table
- Name it
- Select our VPC
- Create!

Done! Right? Wrong! Once we're back in the route tables menu, with the blue box next to our new route table selected the screen should divide in two, then we click the "Routes" tab.

- Edit routes
- 
>For our Public Subnets
- Add route
- For our "Destination" enter "0.0.0.0/0", this means for everything that isn't "local traffic", as in traffic that needs to leave our VPC.
- For "Target" begin to type "igw" and our internet gateway should show up.
- Save routes
Now over to the "Subnet Associations" tab.
- Edit subnet associations
- Select our two public subnets
- Save!

Now our public subnet has access to the internet!

>For our Private subnets
- Repate previous steps to create a new routing table all the way up to "Edit routes"
- We're going to enter "0.0.0.0/0" again for our detsination.
- For our "Target" this time we're going to begin typing "nat" and ou NAT gateway should pop up
- Save routes
Now over to the "Subnet Associations" tab.
- Edit subnet associations
- Select our two private subnets
- Save!

Now our private subnets can also access the internet with outbound traffic, but you can't connect to them from outside the VPC!

### That's it!

Except for Security Groups which we'll cover as necessary or I might update this later on to include, this will get us set up with a basic VPC that we can then use to build all our other cool stuff on top of!


# Command Line VPC Setup

This will be a list of commands that does exactly what we did in through the console, but through the AWS CLI instead!

- First we create the VPC

```
aws ec2 create-vpc \
--cidr-block 13.37.0.0/16 \
--no-amazon-provided-ipv6-cidr-block \
--instance-tenancy default \
--tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=Example-VPC}]' \
--region us-east-1
```

-- UPDATE DNS CHECK

- Now we create the subnets

We can run this command four times, changing the names and the CIDR blocks so we have four subnets

```
aws ec2 create-subnet \
--cidr-block 13.37.1.0/24 \
--vpc-id <VPC-ID-HERE> \
--tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=Public-Subnet 1}]' \
--region us-east-1
```

- Now we create an internet gateway

```
aws ec2 create-internet-gateway \
--region us-east-1
```

Take note of the internet gateway ID, we'll need it to attach it to our VPC, as well as for our route tables

- Attach the IGW to our VPC

```
aws ec2 attach-internet-gateway \
--internet-gateway-id <IGW-ID-HERE> \
--vpc-id <VPC-ID-HERE>
```

- Now we do the same process but with a NAT gateway as well. Firstly we need an elastic IP address for our NAT gateway

```
aws ec2 allocate-address \
--domain vpc
```

Taking note of the allocation ID returned. We then associate it with one of our public subnets.

```
aws ec2 create-nat-gateway \
--allocation-id <ALLOCATION-ID-HERE> \
--subnet-id subnet-xxxxxxxx
```

- Now all that's left to do is create our Route tables and associate them with our subnets!

First we create the route table. Remember, we'll need two, one for our public subnets and one for our private subnets

```
aws ec2 create-route-table \
--vpc-id vpc-xxxxxxxxxxxxx \
--tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=Public-Subnet RT}]' 
```

Take note of the route table ID returned in the response, as well as the default route that exists, we'll need to remove those first.
Once we have our two route tables, we need to add some routes to them.

As I mentioned, first we need to remove the default routes for both public and private tables;

```
aws ec2 delete-route \
--route-table-id rtb-xxxxxxxx \
--destination-cidr-block 0.0.0.0/0
```

For the public route table;

```
aws ec2 create-route \
--route-table-id rtb-xxxxxxxx \
--destination-cidr-block 0.0.0.0/0 \
--gateway-id <IGW-ID-HERE>
```

For th private route table;

```
aws ec2 create-route \
--route-table-id rtb-xxxxxxxx \
--destination-cidr-block 0.0.0.0/0 \
--nat-gateway-id <NAT-GATEWAY-ID>
```

Then we associate them. Make sure you associate your private routes with your private subnets and your public routes with your public subnets!

```
aws ec2 associate-route-table \
--route-table-id rtb-xxxxxxxx \
--subnet-id subnet-xxxxxxxx

```

All done! 










