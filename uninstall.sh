python3 setup.py install --record install.txt
cat install.txt | xargs rm -rf
git rm -r dist
git rm -r build
git rm -r xdict.egg-info
git add .
git commit -m "remove old build"
