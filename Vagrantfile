# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<-SCRIPT
# Install direnv
curl -sfL https://direnv.net/install.sh | bash
echo 'eval "$(direnv hook bash)"' >> /home/vagrant/.bashrc

# Install Nix
curl -L https://nixos.org/nix/install | sudo sh -s -- --daemon --yes
grep 'experimental-features' /etc/nix/nix.conf || (echo 'experimental-features = nix-command flakes' | sudo tee -a /etc/nix/nix.conf)
SCRIPT

Vagrant.configure('2') do |config|
  (1..1).each do |i|
  config.vm.define "ubuntu" do |machine|
    machine.vm.box = 'roboxes-x64/ubuntu2310'
    machine.vm.hostname = "ubuntu"
    config.vm.synced_folder "../CADLibrary", "/home/vagrant/CADLibrary", type: "rsync", rsync__auto: true, rsync__exclude: ['./git*','.direnv*', '.venv*', '.vagrant*']
    config.vm.provision "shell", inline: $script
    machine.vm.provider "qemu" do |vb|
      vb.name = "ubuntu-#{i}"
      vb.cpus = '2'
      vb.memory = '2048'
    end
  end
  end
end
