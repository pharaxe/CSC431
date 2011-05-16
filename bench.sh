#!/bin/bash

ECC="gcc -mcpu=v9"
comp="./ecc"

echo "---- Benchmarks"
select dir in `ls benchmarks`; do
   echo "${dir}: "
   FILES=`ls benchmarks/${dir}/${dir}.ev`
   for ev in $FILES; do
      $comp $ev
      s=`echo $ev | sed 's/\.ev/\.s/'`
      $ECC $s
      benchmarks/${dir}/a.out < benchmarks/${dir}/input > benchmarks/${dir}/output.ev
      diff -wb output.ev output >& /dev/null
      echo " -- returns: $?"
   done

   exit 0
done
