# JunwuTeam

The inputs folder contains the metadata for the stream of ads and all the available moderators;

The are generated(and decoded) by the  MockAdvertisementBuilder and MockModeratorBuilder in the data/advertisement and data/moderator folders respectively.

Should be able to regenerate by running the generateInput.py file; can replace the builder with legit builder in the future.

The data package will automatically read, decode and generate advertisement and moderator manager objects.

I have also completed the simulator package, which is able to simulate the whole process of the system, and compute the totol loss and util rate.

todo: replace the mock builder with real builder, and replace the mock algo with real algo.