
# get scripts directory
CDIR=`dirname $0`

if [ $CDIR = "." ]; then
   CDIR=`pwd` 
fi

REPO=$1
REPO_NAME=`basename $1`


LOGS_DIR=$CDIR/git_logs/$REPO_NAME
mkdir -p $LOGS_DIR

# go to repo dir
cd $REPO

$CDIR/git_stats.sh '--author="jiat0218@gmail.com"' > $LOGS_DIR/jiat.csv
$CDIR/git_stats.sh '--author="lasse.collin@tukaani.org"' > $LOGS_DIR/lasse.csv

$CDIR/git_stats.sh '--author="jiat0218@gmail.com" -i --grep="Lasse" ' > $LOGS_DIR/jiat_thanks_lasse.csv
$CDIR/git_stats.sh '--author="lasse.collin@tukaani.org" -i --grep="Thanks.*Jia Tan" ' > $LOGS_DIR/lasse_thanks_jiat.csv
$CDIR/git_stats.sh  > $LOGS_DIR/all.csv
