#!/bin/bash

mkdir -p data/raw
cd data/raw

rm -r lumi-*
curl -LO "https://github.com/Lumi-supercomputer/LUMI-training-materials/` \
    `archive/refs/heads/main.zip"
unzip -q main.zip
rm main.zip

cd LUMI-training-materials-main/docs
dirnames=$(ls | egrep "[12]day-202[34][0-9]*")
for dirname in $dirnames; do
    cp -r $dirname ../../"lumi-${dirname}"
done

cd ../..
rm -rf LUMI-training-materials-main
