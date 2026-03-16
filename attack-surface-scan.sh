#!/bin/bash

echo "======================================"
echo "     LINUX ATTACK SURFACE SCANNER"
echo "======================================"

echo ""
echo "[1] Open Network Ports"
ss -tuln

echo ""
echo "[2] Running Services"
systemctl list-units --type=service --state=running

echo ""
echo "[3] Users with sudo privileges"
grep 'sudo' /etc/group

echo ""
echo "[4] Failed SSH login attempts"
grep "Failed password" /var/log/auth.log 2>/dev/null | tail

echo ""
echo "[5] Firewall Status"
sudo ufw status

echo ""
echo "[6] Listening Processes"
lsof -i -P -n | grep LISTEN

echo ""
echo "[7] Last Login Activity"
last -n 5

echo ""
echo "SCAN COMPLETE"
