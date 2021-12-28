problemname=$1
testdir=test/$problemname
baseurl=${problemname::-2}

# make test directory
if [ ! -e $testdir ]; then
  oj dl -d $testdir https://atcoder.jp/contests/$baseurl/tasks/$problemname
fi

oj test -c "python src/$problemname.py" -d $testdir