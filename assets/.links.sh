for d in $(find . -maxdepth 1 -type f)
do
  d=$(basename -- "$d")
  e=${d%.*}
  e=$(echo ${e//-/ })
  e=$(echo ${e//.jpg/ })
  e=$(echo ${e//.png/ })
  e=$(echo ${e//.jpeg/ })
  e=$(echo ${e//large/ })
  e=$(echo ${e//francesca kee/ })
  e=$(echo ${e//.\// })
  e=$(echo $e | awk '{for(j=1;j<=NF;j++){ $j=toupper(substr($j,1,1)) substr($j,2) }}1' )
  #d=$(echo ${d//.// })
  # echo $d $e
  echo -n '<a href="/assets/images/'
  echo -n $d 
  echo -n '" title="'
  echo -n $e
  echo '" data-gallery>'
  echo -n '     <img src="/assets/images/thumb/'
  echo -n $d
  echo -n '" alt="'
  echo -n $e
  echo '">'
  echo '</a>'
done  >.links.html

