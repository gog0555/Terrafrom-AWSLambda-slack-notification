module "lambda" {
  source = "../../modules/lambda"

  env  = var.env
  name = var.name
}