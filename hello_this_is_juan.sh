#!/bin/sh

GREEN='\033[0;32m'
ORANGE='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "============================================="
echo "${ORANGE}[Juan] ${NC} Starting staging install ..."
if [ -d "tmp" ] 
then
	echo "${ORANGE}[Juan] ${NC} Removing active service ..."
	docker-compose  \
	-f tmp/homework_wink/docker-compose.yml \
	down -v
	# docker image prune -f
	rm -rf ./tmp/
	echo "${ORANGE}[Juan] ${GREEN} Done!"
fi
echo "${ORANGE}[Juan] ${NC} downloading components ..."
mkdir tmp
git clone https://github.com/TheMemeProject tmp --branch amogus
echo "${ORANGE}[Juan] ${GREEN} done"
echo "${ORANGE}[Juan] ${NC} starting docker components..."
docker-compose \
	-f tmp/homework_wink/docker-compose.yml \
	up --build -d
echo "${ORANGE}[Juan] ${GREEN} done"
echo "${NC} ============================================="
echo "${NC}> ${ORANGE}Juan ${GREEN} solved our ${RED} problems ${NC} <"