echo "---" > .index.html
echo "layout: default" >> .index.html
echo "title: Francesca Kee Fine Art" >> .index.html
echo "permalink: \"/\" " >> .index.html
echo "thumbs:" >> .index.html

for d in $(find . -maxdepth 1 -type f)
do
  d=$(basename -- "$d")
  d=${d%.*}
  echo "   -\"$d\""
done  >>.index.html
echo "" >> .index.html
echo "carousel:" >> .index.html
for d in $(find . -maxdepth 1 -type f)
do
  d=$(basename -- "$d")
  d=${d%.*}
  echo "   -\"$d\""
done  >>.index.html

echo "" >> .index.html
echo "---" >> .index.html
echo "" >> .index.html
echo "{% include gallery.html %}" >> .index.html

