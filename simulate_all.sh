SCRIPT="test.py"

# Iterate over combinations of parameters
for dist in even uneven; do
    for vol in 0.5 1 1.5; do
        for punish in 1 2 3; do
            for src in raw synthetic; do
                for algo in random greedy_idle greedy; do
                    FILENAME="result_${dist}_${vol}_${punish}_${src}_${algo}.json"
                    echo "Running for distribution: $dist, volume: $vol, punishment_factor: $punish, source: $src, algorithm: $algo"
                    python $SCRIPT -d $dist -v $vol -p $punish -s $src -a $algo -f $FILENAME
                done
            done
        done
    done
done

echo "All simulations completed."