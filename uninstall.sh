pip3 uninstall xdict
git rm -r dist
git rm -r build
git rm -r xdict.egg-info
rm -r dist
rm -r build
rm -r xdict.egg-info
git add .
git commit -m "remove old build"
#git push origin master
