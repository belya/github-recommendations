for DAY in `seq -w 30`
do
  wget http://data.githubarchive.org/2017-11-$DAY-{0..23}.json.gz &
done
