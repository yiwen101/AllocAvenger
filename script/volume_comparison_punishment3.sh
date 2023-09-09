SCRIPT="test.py"
for vol in 0.5 1 1.5; do
    FILENAME="result_even_${vol}_1_raw_greedy_farseeing.json"
    echo "Running for volume: $vol..."
    python $SCRIPT -d even -v $vol -p 3 -s raw -a greedy_farseeing -f $FILENAME
done
echo "Volume comparison completed."