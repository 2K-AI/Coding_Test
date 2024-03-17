def solution(bridge_length, weight, truck_weights):
    from collections import deque
    tw = deque(truck_weights)
    bridge = deque([0]* bridge_length)
    bridge_weight = 0
    t = 0 # time
    while len(tw)>0 :
        gone = bridge.popleft()
        bridge_weight-= gone
        if bridge_weight+tw[0] <= weight :
            temp = tw.popleft()

            bridge_weight += temp
            bridge.append(temp)
        else :
            bridge.append(0)

        t+=1 
    return t+bridge_length
