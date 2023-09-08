# TikTok Hackathon: Optimize Advertisement Moderation

Welcome to our project for the TikTok Hackathon! Our aim is to optimize advertisement moderation with the use of a stochastic optimization model, with specific focus on dynamically scoring and prioritizing social media advertisements for review, and ensuring these reviews are matched with the best-fitting moderator.

## Background

Digital platforms like TikTok rely heavily on advertisement reviews to ensure safe and appropriate content delivery. The aim of our project is to:

- Prioritize ad review processes based on the value and riskiness of the advertisements.
- Assign the most suitable moderator for a particular ad review, considering factors such as language fit and industry expertise.

## Project Structure

### 1. `data_builders` Package:

**Components**:

- `AdvertisementProducer`: Reads and synthesizes advertisements from raw data.
- `ModeratorProducer`: Reads and generates synthetic moderator data.
- `AdvertisementBuilder` and `ModeratorBuilder`: These classes generate advertisement and moderator streams respectively, which are structured as 2D arrays where the first dimension represents time units, and the second dimension represents ads or moderators.

### 2. `managers` Package:

**Components**:

- `AdvertisementManager`: Manages advertisement data for simulations.
- `ModeratorManager`: Manages moderator data for simulations.

Both of these managers work as the primary drivers for the simulation, interacting with the `algoObject` to produce results like utilization rate and pairing loss.

## Current Progress

At the moment, we're in the process of testing and refining algorithms to allocate ads to moderators. We've implemented two naive, greedy-based algorithms and are researching the application of queueing theory to develop more efficient solutions.

## Updates as of 22:30, Sep 8: New Features and Progress

**1. Simple Testing Updates**:
- We've successfully enabled the functionality for `simple_test()`. Please note that filtering moderators by country is yet to be implemented.

**2. Loss Estimation**:
- A significant addition has been made with the introduction of `ModeratorUnitTimeValueEstimator`. This helps in estimating the loss due to inaccurate moderation.
- This estimated value contributes to the total loss calculation.
- The allocator has been designed to store this loss information, especially since it's aware of which advertisement job has been assigned to which moderator.

### Challenges Faced

Due to the ambiguous nature of the provided data and problem statement, we faced a few challenges:

- Lack of simulation environment: There is no environment provided. We are setting our own environment for this project.
- Potential discrepancies in data, such as the inconsistency between `p_date` and `start_time`.
- Lack of interpretability for the data and lack of data in general: For example, we don't know whether a specific ads in the data is harmful or not. This makes calculating revenue of a simulation run imfessible.
- Undefined Scoring Function: We are asked to build a scoring function, but there is no label for that. We attempted to optimize it end-to-end by optimising revenue, yet we don't know how revenue is calculated.

## How to Run

Please refer to `test.py` on how to run the simulation with our algorithm.
 
## Future Scope

Our next steps include:

- Deploying more advanced ads allocation algorithm.
- Provide quick start code or shell script.
- Data visualization for the end result.

## Team

- *Wang Junwu*: member of technical team
- *Wang Yiwen*: member of technical team
- *Wang Ziwen*: member of technical team
- *Xu Shuyao*: member of technical team
- *Xie Zebang*: member of technical team

Feel free to explore our repository and share your feedback. Let's make the digital advertising space a safer and more efficient platform for all users!