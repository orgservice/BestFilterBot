if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/orgservice/primefilterbot.git /primefilterbot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /primefilterbot
fi
cd /primefilterbot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
