#!/bin/bash

apt update
apt install nfs-kernel-server

mkdir -p /mnt/nfs_share

chown -R nobody:nogroup /mnt/nfs_share

chmod 777 /mnt/nfs_share/

mkdir /mnt/nfs_share/mysql

ROLE="/mnt/nfs_share  192.168.1.0/24(rw,sync,no_root_squash,no_subtree_check)"

echo $ROLE >> /etc/exports

exportfs -a

systemctl restart nfs-kernel-server.service

echo "Well Done! Good Bye :))"
