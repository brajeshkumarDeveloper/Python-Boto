# # state.tf
terraform {
  backend "s3" {
    bucket = "brajesh-tf-s3-bucket" 
    key    = "brajesh/terraform.tfstate"
    region = "us-east-1"
    dynamodb_table = "terraform-lock-table"
    encrypt        = true
  }
}