SCRIPT="test.py"
for punish in 1 2 3; do
    FILENAME="result_even_1_${punish}_synthetic_greedy_farseeing.json"
    echo "Running with punishment factor: $punish..."
    python $SCRIPT -d even -v 1 -p $punish -s synthetic -a greedy_farseeing -f $FILENAME
done
echo "Punishment factor comparison completed."