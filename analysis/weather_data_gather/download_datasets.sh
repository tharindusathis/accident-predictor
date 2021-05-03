## scrape datasets urls
# python3 get_datasets_urls.py

## download datasets 
# while read line; do
#     filename=${line##*midas-open_uk-hourly-weather-obs_dv-201908_}
#     echo $filename

#     curl --cert $PWD/creds.pem -L -c /dev/null $line -o ./DATASETS/$filename
# done < ./weather_data_urls.txt


cd  ./DATASETS

## minimalizing the filenames of datasets
for filename in *.csv
do
    arrIN=(${filename//_/ }) # split by underscore

    filename2="${arrIN[0]}_${arrIN[2]}_${arrIN[4]}"
    
    echo $filename2
    mv "$filename" "$filename2"
done

## extract weather station names and their coordinates
echo "name,lat,log" >> ../stations.csv

for filename in *.csv
do  
    # lat,lon are at line 14 in each file
    line=$(sed '14q;d' $filename)
    arr=(${line//,/ })        # e.g.: location,G,56.879,-3.421
    arrF=(${filename//_/ })   # e.g.: aberdeenshire_30138_leith-hall-no-2_qcv-1_2005

    station="$filename,${arr[2]},${arr[3]}" 
    echo $station >> ../stations.csv 
done




