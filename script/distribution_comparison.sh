SCRIPT="test.py"
for dist in even uneven; do
    FILENAME="result_${dist}_1_1_synthetic_greedy_farseeing.json"
    echo "Running for distribution: $dist..."
    python $SCRIPT -d $dist -v 1 -p 1 -s synthetic -a greedy_farseeing -f $FILENAME
done
echo "Distribution comparison completed."