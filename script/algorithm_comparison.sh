SCRIPT="test.py"
for algo in random greedy_idle greedy greedy_farseeing; do
    FILENAME="result_even_1_1_raw_${algo}.json"
    echo "Running with algorithm: $algo..."
    python $SCRIPT -d even -v 1 -p 1 -s raw -a $algo -f $FILENAME
done
echo "Algorithm comparison completed."