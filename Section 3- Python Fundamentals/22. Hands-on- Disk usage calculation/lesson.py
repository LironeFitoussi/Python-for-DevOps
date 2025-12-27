# Exercise Recap: Calculating and Formatting Disk Usage in Python

# Step 1: Define the Inputs
server_name = "dev-server-01"
cpu_cores = 8
memory_gb = 32
disk_used_gb = 350
disk_total_gb = 500

# Step 2: Calculate Disk Usage Percentage
disk_usage_percentage = disk_used_gb / disk_total_gb
print(disk_usage_percentage)  # Output: 0.7

# Step 3: Build a Human-Readable Summary
summary = (
    f"Server '{server_name.upper()}' "
    f"({cpu_cores} CPU cores, {memory_gb}GB RAM): "
    f"Disk usage = {disk_usage_percentage}"
)
print(summary)

# Step 4: Add Float Formatting
# Format with One Decimal Place
summary_formatted = (
    f"Server '{server_name.upper()}' "
    f"({cpu_cores} CPU cores, {memory_gb}GB RAM): "
    f"Disk usage = {disk_usage_percentage:.1f}"
)
print(summary_formatted)

# Format as a Percentage
summary_percentage = (
    f"Server '{server_name.upper()}' "
    f"({cpu_cores} CPU cores, {memory_gb}GB RAM): "
    f"Disk usage = {disk_usage_percentage:.1%}"
)
print(summary_percentage)

