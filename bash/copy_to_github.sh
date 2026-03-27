function copy_to_github(){
  echo "Syncing $1"
  rsync --recursive --delete ado/$1 github --exclude '.git' --exclude 'node_modules' --exclude 'tmp' --exclude '.venv' # Syncs files recursively, deletes extra files at destination, excludes specified patterns
 
  cd github/$1
  git add .
  git status
  git commit -m "Update on $(date +'%Y-%m-%d')"
  git push
}

clear
# copy_to_github template
# copy_to_github lab
# copy_to_github crowdilm
echo "Done..."
# sleep 3

