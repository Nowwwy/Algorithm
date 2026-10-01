T = int(input())

# 분할
def merge(start, end):
    # 미리 변수 끌어오기
    global cnt
    # 분할 완료시 반환
    if start == end:
        return
    # 기준점 설정
    mid = (start + end + 1) // 2

    # 왼쪽
    merge(start, mid-1)
    # 오른쪽
    merge(mid, end)

    # 왼쪽 마지막 숫자가 오른쪽 마지막 숫자보다 클 시에 카운트 증가
    if ai[mid - 1] > ai[end]:
        cnt += 1

    # 병합 빈껍데기 생성    
    sorted_ai = []

    # i는 왼쪽 인덱스 시작 j는 오른쪽 인덱스 시작
    i = start
    j = mid

    # 왼쪽 리스트와 오른쪽 리스트 의 종료 조건 설정
    # 작은 수 부터 오름차순으로 빈껍데기에 추가
    while i <= mid-1 and j <= end:
        if ai[i] <= ai[j]:
            sorted_ai.append(ai[i])
            i += 1
        else:
            sorted_ai.append(ai[j])
            j += 1
    
    # 남아 있는 것들 병합에 붙이기
    while i <= mid-1:
        sorted_ai.append(ai[i])
        i += 1
    while j <= end:
        sorted_ai.append(ai[j])
        j += 1

    # 변수 b를 할당하여 ai안에 병합이 완료된 리스트를 추가
    b = 0
    for a in range(start, end+1):
        ai[a] = sorted_ai[b]
        b += 1


for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    cnt = 0

    # 전체 범위 돌리기
    merge(0, N-1)

    print(f'#{tc} {ai[N//2]} {cnt}')