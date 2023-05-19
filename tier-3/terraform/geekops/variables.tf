variable "resource_group_name" {
  description = "The name of the resource group"
}

variable "location" {
  description = "The location of the resource"
  default = "West Europe"

}

variable "environment" {
    description = "The environment of the resource"
}

variable "service_plan_name" {
    description = "The name of the service plan"
}

