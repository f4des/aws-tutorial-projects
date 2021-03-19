IOT Custom Authoriser Walkthrough

Latency based routing for API Gateway

HTTP API Gateway ALB Integration

Docker Greengrass

ec2 ssh script



docker run --rm --init -it --name aws-iot-greengrass \
--entrypoint /greengrass-entrypoint.sh \
-v ./certs:/greengrass/certs \
-v ./config:/greengrass/config \

-p 8883:8883 \
216483018798.dkr.ecr.us-west-2.amazonaws.com/aws-iot-greengrass:latestaws ecr get-login-password --region  us-west-2 | docker login --username AWS --password-stdin https://216483018798.dkr.ecr.us-west-2.amazonaws.com

sudo docker run --rm --init -it --name aws-iot-greengrass \
 --entrypoint /greengrass-entrypoint.sh \
 -v $PWD/certs:/greengrass/certs \
 -v $PWD/config:/greengrass/config \
 -v $PWD/log:/greengrass/log
 -p 8883:8883 \
 amazon/aws-iot-greengrass


docker run --rm --init -it --name aws-iot-greengrass --entrypoint /greengrass-entrypoint.sh -v $PWD/certs:/greengrass/certs -v $PWD/log:/greengrass/ggc/log -v $PWD/config:/greengrass/config -p 8883:8883 amazon/aws-iot-greengrass

iot QoS demonstration
Amazon Acronym Service
GG Device trigger lambda publish to IoT Cloud
synchronous SF / API Gateway
IoT websocket Step Function
HTTP -> GGC -> Lamp/TV
Lambda Auth API GAteway
mTLS explanation for APIGW
Lambda OCI
kafka walkthrough
