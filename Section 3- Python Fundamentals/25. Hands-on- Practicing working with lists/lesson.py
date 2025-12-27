# List Exercise: Practicing Indexing, Appending, and Assignment

# Step 1: Create the Initial List
deployment_targets = ["us-east-1", "eu-west-1", "ap-southeast-1"]

# Step 2: Print the First Deployment Target
print(deployment_targets[0])
# Output: "us-east-1"

# Step 3: Append a New Region
deployment_targets.append("us-west-2")

# Step 4: Print the Updated List
print(deployment_targets)
# Output: ['us-east-1', 'eu-west-1', 'ap-southeast-1', 'us-west-2']

# Step 5: Modify the Second Region
deployment_targets[1] = "eu-central-1"

# Step 6: Final Print
print(deployment_targets)
# Output: ['us-east-1', 'eu-central-1', 'ap-southeast-1', 'us-west-2']

