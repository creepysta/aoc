day=$1

if [[ -d $day ]];
then
    echo "Day=$day already setup."
    exit 0
fi

echo "Setting up day=$day"
mkdir $day
pushd $day
echo "Initialising go mod"
go mod init aoc/$day
popd
