SCRIPT="test.py"
FILENAME="result_even_1_1_synthetic_greedy_farseeing.json"
echo "Running baseline simulation..."
python $SCRIPT -d even -v 1 -p 1 -s synthetic -a greedy_farseeing -f $FILENAME
echo "SOTA simulation completed."