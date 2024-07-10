# shift 

CMD=`git log --date=format:'%Y-%m' --pretty=format:'%ad' --numstat "$@"`

echo "Date;  Commits;  Added lines; Removed lines; Total changes;"
echo "$CMD" | awk '
{
    if ($1 ~ /^[0-9]{4}-[0-9]{2}$/) {
        date = $1
        commit_count[date]++
    } else if (NF == 3) {
        added[date] += $1
        removed[date] += $2
    }
}
END {
    for (date in added) {
        printf ("%s; %d; %d; %d; %d;\n", date, commit_count[date], added[date], removed[date], added[date] + removed[date])
    }
}'|sort
