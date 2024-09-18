import pandas as pd

# Load excel
data_excel = 'data.xlsx'
df = pd.read_excel(data_excel, sheet_name=0)

Following = []
Followers = []
Mutual = []
NoMatching = []

# Create new file called results.txt
with open('results.txt', 'w') as file:
    
    # Verifies in each row if the "profile picture" text exists
    for index, row in df.iterrows():
        if "profile picture" in str(row['FOLLOWING']).lower():
            Following.append(row['FOLLOWING'])
        if "profile picture" in str(row['FOLLOWERS']).lower():
            Followers.append(row['FOLLOWERS'])
    
    # Writes info on the results.txt
    file.write(f'Users you Follow: {len(Following)}\n')
    file.write(f'Users Following you: {len(Followers)}\n')
    
    # Obtains Mutual and No Corresponding
    for i in range(len(Following)):
        if Following[i] not in Followers:
            NoMatching.append(Following[i])
        for j in range(len(Followers)):
            if Following[i] == Followers[j]:
                Mutual.append(Followers[j])
                break
    
    file.write(f'Mutual Followers: {len(Mutual)}\n')
    file.write('No Corresponding Followers:\n')
    
    # Cleans the "'s profile picture" text in each
    Usernames = [user.replace("'s profile picture", "") for user in NoMatching]

    for k, user in enumerate(Usernames):
        file.write(f"{k + 1}. {user}\n")