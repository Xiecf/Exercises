players = ['xiechaofan','gaojinlei','lidong','yujianwei']
print(players[0:2])
print(players[1:3])
print(players[1:-1])
print(players[1:len(players)])
print(players[1:])
for play in players[:3]:
    print(play)
print('ok')

players2 = players[:]
print(players2)
players2.append('liuhoutian')
print(players)
print(players2)
for play2 in players2[:]:
    print(play2)
for play in players[:]:
    print(play)
print('ok')
