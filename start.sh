if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/orgservice/BestFilterBot.git /BestFilterBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /BestFilterBot
fi
cd /BestFilterBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
