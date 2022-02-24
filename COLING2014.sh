prefix=C14
dir=../COLING2014
min=1001
max=1221
for i in `seq -w $min $max`
do
    wget https://aclanthology.org/$prefix-$i.pdf -O $dir/$prefix-$i.pdf
    pdftotext -f 1 -l 1 $dir/$prefix-$i.pdf $dir/$prefix-$i.txt
done
cd $dir/
perl -e 'for $a(glob("*.txt")){open F, $a;$f=1;while(<F>){$f=0 if $_=~/Creative Commons/}print $a, "\n" if $f}'