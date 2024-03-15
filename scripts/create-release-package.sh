#!/bin/bash

echo "Creating release package" >&2

# Add db-init
echo "Copying db-init to projects directory" >&2
cp -r ./db-init/db-setup ./projects/database
cp -r ./db-init/tables ./projects/database
cp -r ./db-init/seed-data ./projects/database

# Add Installation Guide
echo "Copying Installation Guide to projects directory" >&2
cp docs/resource-installation.md ./projects/README.md

# Add project backups
echo "Creating project backups" >&2
mkdir -p ./projects/projectBackups
zip -rq ./projects/projectBackups/WaterTreatment.zip ./gw-projects/WaterTreatment

# Zip project contents into a dedicated package
echo "Zipping project contents" >&2
cd ./projects && zip -rq ../resource.zip ./*

# resource.zip will be added to the release from the workflow

echo "Release package creation completed" >&2
