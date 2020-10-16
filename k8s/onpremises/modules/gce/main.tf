resource "google_compute_network" "kubeadm" {
  name                    = "kubeadm-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "kubeadm" {
  name          = "kubeadm-subnetwork"
  ip_cidr_range = "10.0.0.0/24"
  region        = "asia-northeast1"
  network       = google_compute_network.kubeadm.id
  secondary_ip_range {
    range_name    = "kubeadm-secondary-range"
    ip_cidr_range = "192.168.10.0/24"
  }
}

resource "google_compute_firewall" "ssh" {
  name    = "kubeadm-ssh-firewall"
  network = google_compute_network.kubeadm.name

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }
}

resource "google_compute_instance" "kubeadm" {
  name         = "kubeadm-test"
  machine_type = "e2-standard-2"

  zone = "asia-northeast1-b"

  boot_disk {
    initialize_params {
      image = "ubuntu-1804-lts"
      size  = 100
      type  = "pd-ssd"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.kubeadm.id

    access_config {}
    alias_ip_range {
      ip_cidr_range         = "192.168.10.0/24"
      subnetwork_range_name = "kubeadm-secondary-range"
    }
  }

  service_account {
    scopes = ["userinfo-email", "compute-ro", "storage-ro"]
  }
}

resource "google_compute_network_endpoint_group" "kubeadm" {
  name         = "kubeadm-neg"
  network      = google_compute_network.kubeadm.id
  subnetwork   = google_compute_subnetwork.kubeadm.id
  default_port = "90"
  zone         = "asia-northeast1-b"
}

resource "google_compute_network_endpoint" "kubeadm" {
  network_endpoint_group = google_compute_network_endpoint_group.kubeadm.name

  instance   = google_compute_instance.kubeadm.name
  port       = google_compute_network_endpoint_group.kubeadm.default_port
  ip_address = google_compute_instance.kubeadm.network_interface[0].network_ip
}
