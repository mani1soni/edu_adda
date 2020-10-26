output "Jenkins-Main-Node-Public_IP" {
  value = aws_instance.jenkins-master.public_ip
}

output "Jenkins-Worker-Public-IPs" {
  value = {
    for instance in aws_instance.jenkins-worker-oregon :
    instance.id => instance.public_ip
  }
}


#Add LB DNS name to outputs
output "LB-DNS-NAME" {
  value = aws_lb.application-lb.dns_name
}