provider "google" {
  project = "sound-datum-292611"
  region  = "asia-northeast1"
  zone    = "asia-northeast1-b"
}

module "gce" {
  source = "./modules/gce"
}

output "network_ip" {
  value = module.gce.instance_ip
}
