terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

resource "local_file" "example" {
  filename = "${path.module}/example.txt"
  content  = "Terraform successfully updated this file!"
}
