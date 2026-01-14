// Last updated: 1/14/2026, 1:25:20 AM
1class MyCalendar {
2    
3    // TreeMap存储已预订的时间段，key=开始时间，value=结束时间
4    private TreeMap<Integer, Integer> calendar;
5
6    public MyCalendar() {
7        calendar = new TreeMap<>();
8    }
9
10    public boolean book(int startTime, int endTime) {
11        // 找到开始时间<=startTime的最近事件（左边相邻）
12        Integer prev = calendar.floorKey(startTime);
13        
14        // 找到开始时间>=startTime的最近事件（右边相邻）
15        Integer next = calendar.ceilingKey(startTime);
16
17        // 检查与左边事件冲突：左边事件的结束时间 > 新事件开始时间
18        // 检查与右边事件冲突：新事件的结束时间 > 右边事件开始时间
19        if ((prev != null && calendar.get(prev) > startTime) ||
20            (next != null && endTime > next)) {
21            return false;
22        }
23
24        // 无冲突，插入新事件
25        calendar.put(startTime, endTime);
26        return true;
27    }
28}
29
30/**
31 * Time Complexity: O(N log N) - N次book()调用，每次O(log N)查找和插入
32 * Space Complexity: O(N) - 存储最多N个事件
33 */