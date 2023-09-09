SCRIPT="test.py"
for src in raw synthetic; do
    FILENAME="result_even_1_1_${src}_greedy_farseeing.json"
    echo "Running for source: $src..."
    python $SCRIPT -d even -v 1 -p 1 -s $src -a greedy_farseeing -f $FILENAME
done
echo "Source comparison completed."