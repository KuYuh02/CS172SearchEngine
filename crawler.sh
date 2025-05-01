#!/bin/bash
SEED_FILE=$1
NUM_PAGES=$2
HOPS=$3
OUTPUT_DIR=$4

python3 reddit_crawler.py --seed $SEED_FILE --pages $NUM_PAGES --hops $HOPS --output $OUTPUT_DIR
