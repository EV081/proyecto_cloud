variable "region" {
  type    = string
  default = "us-east-1"
}

variable "account_id" {
  type    = string
  default = "222967562420" // id de la cuenta personal de aws
}

variable "ecr_repo_name" {
  type    = string
  default = "proyecto" //nombre del repositorio donde tenemos nuestra imagen
}

variable "container_port" {
  type    = number
  default = 8000 // en el puerto 8000 porque en ese puerto tenemos nuestra imagen
}

