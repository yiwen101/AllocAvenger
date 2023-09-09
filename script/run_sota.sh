SCRIPT="test.py"
FILENAME="result_even_1_1_synthetic_greedy_farseeing.json"
echo "Running SOTA simulation..."
python $SCRIPT -d even -v 1.5 -p 1 -s raw -a greedy_farseeing -f $FILENAME
echo "SOTA simulation completed."