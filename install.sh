git pull origin master
python3 setup.py install --record install.txt
git add .
git commit -m "add new build"
git push origin master

