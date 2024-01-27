class Soldier:
    def __init__(self, id, health, x, y):
        self.id = id
        self.health = health
        self.x = x
        self.y = y

class Melee(Soldier):
    def __init__(self, id, health, x, y):
        super().__init__(id, health, x, y)

class Archer(Soldier):
    def __init__(self, id, health, x, y):
        super().__init__(id, health, x, y)

def main():
    n = int(input())
    g = [[None for _ in range(n + 1)] for _ in range(2)]
    turn = 0

    while True:
        ins = input().split()
        
        if ins[0] == "new":
            s_type, id, x, y = ins[1], int(ins[2]), int(ins[3]), int(ins[4])
            if g[turn][id] is note None:
                print("duplicate tag")
            else:
                if s_type == "archer":
                    g[turn][id] = Archer(id, 100, x, y)
                else:
                    g[turn][id] = Melee(id, 100, x, y)
                turn = 1 - turn

        elif ins[0] == "move":
            id, direction = int(ins[1]), ins[2]
            sides = ['left', 'right', 'up', 'down']
            sizes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            index = sides.index(direction)
            x, y = sizes[index]
            if 0 <= g[turn][id].x + x < n and 0 <= g[turn][id].y + y < n:
                g[turn][id].x += x
                g[turn][id].y += y
                turn = 1 - turn
            else:
                print('out of bounds')

        elif ins[0] == "attack":
            attacker_id, target_id = int(ins[1]), int(ins[2])
            distance = abs(g[turn][attacker_id].x - g[1 - turn][target_id].x) + abs(g[turn][attacker_id].y - g[1 - turn][target_id].y)
            if isinstance(g[turn][attacker_id], Archer):
                if distance <= 2:
                    g[1 - turn][target_id].health -= 10
                    if g[1 - turn][target_id].health <= 0:
                        g[1 - turn][target_id] = None
                        print('target eliminated')
                    turn = 1 - turn
                else:
                    print('the target is too far')

            else:
                if distance <= 1:
                    g[1 - turn][target_id].health -= 20
                    if g[1 - turn][target_id].health <= 0:
                        g[1 - turn][target_id] = None
                        print('target eliminated')
                    turn = 1 - turn
                else:
                    print('the target is too far')

        elif ins[0] == "info":
            id = int(ins[1])
            if g[turn][id] is None:
                print('soldier does not exist')
            else:
                print('health: ', g[turn][id].health)
                print('location: ', g[turn][id].x, ' ', g[turn][id].y)
                turn = 1 - turn

        elif ins[0] == "who":
            h0 = 0
            h1 = 0

            for i in range(n + 1):
                if g[0][i] is not None:
                    h0 += g[0][i].health

            for i in range(n + 1):
                if g[1][i] is not None:
                    h1 += g[1][i].health

            if h0 > h1:
                print('player  1')
            elif h1 > h0:
                print('player  2')
            else:
                print('draw')

        elif ins[0] == 'end':
            break

if __name__ == '__main__':
    main()
