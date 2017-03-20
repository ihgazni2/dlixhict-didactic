git pull origin master
python3 setup.py install --record install.txt
cat install.txt | xargs rm -rf
rm -r dist
rm -r build
rm -r xdict.egg-info
git rm -r dist
git rm -r build
git rm -r xdict.egg-info
git add .
git commit -m "remove old build"
git push origin master
