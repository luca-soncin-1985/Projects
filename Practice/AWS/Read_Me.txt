youtube-trend project:

1. Download data from source: https://www.kaggle.com/datasets/datasnaek/youtube-new?resource=download
2. Load data into S3 Bucket "youtube-analysis-postlupy" via AWS CLI:
    - # To copy all JSON Reference data to same location:
        aws s3 cp . s3://youtube-analysis-postlupy/youtube/raw_statistics_reference_data/ --recursive --exclude "*" --include "*.json"
    - # To copy all data files to its own location, following Hive-style patterns:
        aws s3 cp CAvideos.csv s3://youtube-analysis-postlupy/youtube/raw_statistics/region=ca/
        aws s3 cp DEvideos.csv s3://youtube-analysis-postlupy/youtube/raw_statistics/region=de/
        aws s3 cp FRvideos.csv s3://youtube-analysis-postlupy/youtube/raw_statistics/region=fr/
        aws s3 cp GBvideos.csv s3://youtube-analysis-postlupy/youtube/raw_statistics/region=gb/
        aws s3 cp INvideos.csv s3://youtube-analysis-postlupy/youtube/raw_statistics/region=in/
        aws s3 cp JPvideos.csv s3://youtube-analysis-postlupy/youtube/raw_statistics/region=jp/
        aws s3 cp KRvideos.csv s3://youtube-analysis-postlupy/youtube/raw_statistics/region=kr/
        aws s3 cp MXvideos.csv s3://youtube-analysis-postlupy/youtube/raw_statistics/region=mx/
        aws s3 cp RUvideos.csv s3://youtube-analysis-postlupy/youtube/raw_statistics/region=ru/
        aws s3 cp USvideos.csv s3://youtube-analysis-postlupy/youtube/raw_statistics/region=us/
3. Create a Glue catalogue with the help of a Crawler
4. Query data with Athena
