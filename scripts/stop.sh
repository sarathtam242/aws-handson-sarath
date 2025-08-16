#!/bin/bash
echo "Stopping existing application (if any)"
sudo systemctl stop httpd || true
