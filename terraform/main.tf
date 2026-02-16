provider "aws" {
  region = "us-east-1"
}


resource "aws_instance" "my_instance" {
    ami                                  = "ami-0b6c6ebed2801a5cb"
    instance_type                        = "t3.micro"
    key_name                             = "web-api"
    region                               = "us-east-1"
    security_groups                      = [
        "launch-wizard-3",
    ]
    subnet_id                            = "subnet-099ae98a514d34d5f"
    tags                                 = {
        "Name" = "my-webapi-instance"
    }
    vpc_security_group_ids               = [
        "sg-05cd4e131921a2aa9",
    ]
   
}

resource "aws_s3_bucket" "s3_bucket" {
  bucket= "brajesh-tf-s3-bucket"
}
