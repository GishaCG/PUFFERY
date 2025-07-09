import pandas as pd

# File paths
input_file = '/content/HCMI_OneMillionChallenges.csv'        # 64-column binary challenges (with -1s for 0)
response_file = '/content/HCMI_OneMillionResponses.csv'       # 1-bit binary responses
final_output_file = '/content/final_outputHCMI.csv'        # Final output file

# Step 1: Load and process the challenge file
df_challenges = pd.read_csv(input_file, header=None)

# Ensure there are exactly 64 columns
if df_challenges.shape[1] != 64:
    raise ValueError("The input CSV must contain exactly 64 columns.")

# Replace -1 with 0
df_challenges = df_challenges.replace(-1, 0)

# Combine 64 binary columns into a single binary string per row
df_challenges['challenge'] = df_challenges.astype(str).agg(''.join, axis=1)

# Step 2: Load response file
df_responses = pd.read_csv(response_file, header=None, dtype=str)

# Ensure the number of rows match
if len(df_challenges) != len(df_responses):
    raise ValueError("Number of rows in challenge and response files must match.")

# Step 3: Combine into a single DataFrame
final_df = pd.DataFrame({
    'challenge': df_challenges['challenge'],
    'response': df_responses[0]
})

# Step 4: Save to final CSV
final_df.to_csv(final_output_file, index=False)

print(f"Final file saved as '{final_output_file}' with columns 'challenge' and 'response'.")
