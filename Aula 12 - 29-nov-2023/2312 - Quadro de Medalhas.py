def orderly_medal_board(country_medals):
    name, gold, silver, bronze = country_medals
    return [-gold, -silver, -bronze, name]


def main():
    n = int(input())
    medal_board = list()

    for _ in range(n):
        country_medals = list(input().split())
        for i in range(1, 4):
            country_medals[i] = int(country_medals[i])
        medal_board.append(country_medals)

    medal_board.sort(key=orderly_medal_board)

    for i in range(n):
        print(f'{medal_board[i][0]} {medal_board[i][1]} {medal_board[i][2]} {medal_board[i][3]}')


if __name__ == '__main__':
    main()
