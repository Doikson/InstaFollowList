import pandas as pd

# Load excel
data_excel = 'data.xlsx'
df = pd.read_excel(data_excel, sheet_name=0)

following = []
followers = []
mutual = []
no_matching = []

# Create new file called results.txt
with open('results.txt', 'w') as file:
    
    # Verifies in each row if the "profile picture" text exists
    for index, row in df.iterrows():
        if "profile picture" in str(row['FOLLOWING']).lower():
            following.append(row['FOLLOWING'])
        if "profile picture" in str(row['FOLLOWERS']).lower():
            followers.append(row['FOLLOWERS'])
    
    # Writes info on the results.txt
    file.write(f'Users you Follow: {len(following)}\n')
    file.write(f'Users Following you: {len(followers)}\n')
    
    # Obtains mutual and No Corresponding
    for i in range(len(following)):
        if following[i] not in followers:
            no_matching.append(following[i])
        for j in range(len(followers)):
            if following[i] == followers[j]:
                mutual.append(followers[j])
                break
    
    file.write(f'mutual followers: {len(mutual)}\n')
    file.write('No Corresponding Followers:\n')
    
    # Cleans the "'s profile picture" text in each
    Usernames = [user.replace("'s profile picture", "") for user in no_matching]

    for k, user in enumerate(Usernames):
        file.write(f"{k + 1}. {user}\n")