variable "profile" {
  type    = string
  default = "default"
}

variable "region-master" {
  type    = string
  default = "us-east-1"
}

variable "region-worker" {
  type    = string
  default = "us-east-2"
}


variable "external-ip" {
  type    = string
  default = "0.0.0.0/0"
}

variable "workers-count" {
  type    = number
  default = 1
}
variable "instance-type" {
  type    = string
  default = "t2.micro"
}

variable "webserver-port" {
  type    = number
  default = 8080
}