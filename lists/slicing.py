players = ['charles', 'martina', 'michael', 'eli', 'florence']

print('Here are the first three players of my team:')
for player in players[:3]:
    print(player.title())

print('Here are the middle three players of my team:')
for player in players[1:4]:
    print(player.title())

# Copy the players list
other_players = players[:]
print(other_players)

# Add a value to the copied players list
other_players.append('aaron')

print('Here are some additional players:')
for player in other_players[3:]:
    print(player.title())