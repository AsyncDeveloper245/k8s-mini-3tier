terraform {

  required_providers {

    azurerm = {
      source = "hashicorp/azurerm"
      version = "2.10.0"
    }
  }
}

locals {
  resource_name = "${var.resource_group_name}-${var.location}-${var.country_code}"
}


resource "azurerm_resource_group" {
    name = "RG-${local.resource_name}"
    location = var.location
    tags = {
      ENV = var.environment
    }
}





