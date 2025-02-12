set -e
# set -x

echo "\$0 = $0, $1"

for i in "$@";
do
    echo "hi $i"
done

if [[ "${1}" > "$2" ]];
then
    echo "$1 > $2"
elif [[ "${1}" == "${2}" ]]; 
then
    echo "$1 == $2"
else
    echo "${1} < ${2}"
fi

sed -ibak "s/is/his/g" "/home/g/Documents/devops/bash/simple.txt"

while IFS= read -r line; do
    echo "Processing: $line"
done < /home/g/Documents/devops/bash/simple.txt
