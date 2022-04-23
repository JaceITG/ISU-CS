#!/bin/sh
rm results.txt
for i in {1..9}
do
    echo running $i
    echo -n "0$i. " >> results.txt
    python3 0$i.py >> results.txt
done

for i in {10..17}
do
    echo running $i
    echo -n "$i. " >> results.txt
    python3 $i.py >> results.txt
done
