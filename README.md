password: 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




Initialize Git Repository
git init
git status

Create .gitignore
Add:
myvenv/
__pycache__/
*.pyc
db.sqlite3

git config --global user.name "YourName"
git config --global user.email yourgithubemail@gmail.com
git add .
git commit -m "Initial Django Starter Project"

Repository name:
“Pro”

git remote add origin https://github.com/YOUR_USERNAME/pro.git
git branch -M main
git push -u origin main
