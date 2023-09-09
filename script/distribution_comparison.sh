SCRIPT="test.py"
for dist in even uneven; do
    FILENAME="result_${dist}_1_1_raw_greedy.json"
    echo "Running for distribution: $dist..."
    python $SCRIPT -d $dist -v 1 -p 1 -s raw -a greedy -f $FILENAME
done
echo "Distribution comparison completed."