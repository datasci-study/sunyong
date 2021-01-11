'''
V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.

주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.

예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.

노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000

테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.

E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.

입력
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9'''
    #BFS 함수
def bfs(queue):
    count = 1
    #큐가 빌때까지 반복
    while queue:
        #2개의 큐가 필요하므로 한개더 생성한다.
        s_queue = []
        #큐가 빌때까지 반복한다.
        while queue:
            #원소를 꺼내서
            index = queue.pop()
            #연결되어 있는 부분들을 확인한다.
            for i in node[index]:
                #이미 방문했다면 다른 index 확인한다
                if visited[i]: continue
                #도착지와 일치한다면 이동거리를 반환한다.
                if i == end: return count
                #위의 조건에 걸리지 않는다면 두번재 큐에 추가한다.
                s_queue.append(i)
                #방문처리를 한다.
                visited[i] = 1
        #모든 큐가 비었다면 카운트를 증가시킨다.
        count += 1
        #큐를 교체한다.
        queue = s_queue
    #여기까지 왔다면 목적지까지 도착할 수 없다.
    return 0
T=int(input())
for test_case in range(1,T+1):
    #V개의 노드, E개의 간선
    V, E = map(int, input().split())
    #리스트를 이용한 간선 표시
    node = [[] for _ in range(V+1)]
    #방문여부
    visited = [0 for _ in range(V+1)]
    #데이터 편집
    for i in range(E):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    #시작노드와 끝나는 노드 저장
    start, end = map(int, input().split())
    #시작노드 방문처리
    visited[start] = 1
    #bfs 돌리기
    print('#{} {}'.format(T, bfs([start])))