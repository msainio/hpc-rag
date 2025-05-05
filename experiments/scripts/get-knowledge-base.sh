#!/bin/bash

rm -rf data/knowledge-base
mkdir data/knowledge-base
cd data/knowledge-base

# csc-env-eff
curl -L "https://github.com/csc-training/csc-env-eff/` \
    `archive/refs/heads/master.tar.gz" -O
tar -xzf master.tar.gz
rm master.tar.gz 
mv csc-env-eff-master csc-env-eff

cd csc-env-eff
for file in $(ls -A); do
    if ! [[ $file =~ ^(_slides|part-1|part-2)$ ]]; then
    rm -r $file
    fi
done
rm  -r _slides/SRT*
cd ..

# csc-user-guide
curl -L "https://github.com/CSCfi/csc-user-guide/` \
    `archive/refs/heads/master.tar.gz" -O
tar -xzf master.tar.gz
rm master.tar.gz
mv csc-user-guide-master csc-user-guide

cd csc-user-guide
for file in $(ls -A); do
    if [[ $file != docs ]]; then
        rm -r $file
    fi
done
rm -r docs/img
cd ..

# lumi-easybuild-docs
for repo in "LUMI-EasyBuild-containers" "LUMI-EasyBuild-contrib" \
    "LUMI-EasyBuild-docs" "LUMI-SoftwareStack"; do
    curl -L "https://github.com/Lumi-supercomputer/${repo}/` \
        `archive/refs/heads/main.tar.gz" -O
    tar -xzf main.tar.gz
    rm main.tar.gz
    mv ${repo}-main $repo
done
curl -L "https://github.com/Lumi-supercomputer/LUMI-EasyBuild-docs/` \
    `archive/refs/heads/gh-pages.tar.gz" -O
tar -xzf gh-pages.tar.gz
rm gh-pages.tar.gz
mv LUMI-EasyBuild-docs-gh-pages LUMI-EasyBuild-docs/gh-pages

cd LUMI-EasyBuild-docs
bash scripts/build_docs.sh
cd docs-generated
for file in $(ls -A); do
    if ! [[ $file = docs ]];
    then rm -r $file
    fi
done
cd ..
mv docs/known_issues.md docs-generated/docs/known_issues.md
mv docs/whats_new.md docs-generated/docs/whats_new.md
for file in $(ls -A); do
    if ! [[ $file =~ (docs-generated|gh-pages) ]];
    then rm -r $file
    fi
done
cd ..
for file in $(ls -A); do
    if [[ $file =~ (containers|contrib|SoftwareStack)$ ]]; then
        rm -r $file
    fi
done

# lumi-userguide
curl -L "https://github.com/Lumi-supercomputer/lumi-userguide/` \
    `archive/refs/heads/production.tar.gz" -O
tar -xzf production.tar.gz
rm production.tar.gz
mv lumi-userguide-production lumi-userguide

cd lumi-userguide
for file in $(ls -A); do
    if ! [[ $file = docs ]]; then
        rm -r $file
    fi
done
rm -r docs/assets
