FILES="./*.png"

for f in $FILES
do
	echo "${f:2:2}"
	mkdir ${f:2:2}
	mv $f ${f:2:2}
done
