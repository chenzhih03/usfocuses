for Zcom in  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
do
    sed -e "s/KKK/$Zcom/g" scrapy_general.py > scrapy-$Zcom.py
    python scrapy-$Zcom.py &
done
