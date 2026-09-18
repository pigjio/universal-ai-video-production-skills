# 计时验收：无需包外脚本

本流程用于逐镜修订、Animatic 排时、编号/总时长回归。人工可使用纸笔与计算器；Agent 必须调用可用算术工具（例如 Python、计算器或电子表格）计算，不凭心算声称精确。这里不依赖任何随包计时脚本，也不声称自动解析任意 Markdown。

## 输入表

从当前权威逐镜稿摘录 CSV 或表格：`scene_id,shot_id,start,end,duration,beat_id`。时间统一为秒或整数帧，起止采用半开区间 `[start,end)`。声明时间基准、目标/是否暂不锁时、容差、哪些轨道允许重叠。帧制须声明 fps；秒转帧如不能整除，先约定取整策略并回查误差。

规范有效输入（秒制、连续画面轨道、目标 5 秒、无容差）：

```csv
scene_id,shot_id,start,end,duration,beat_id
A,A-01,0,1.2,1.2,B1
A,A-02,1.2,3,1.8,B1
A,A-03,3,5,2,B2
```

## 验收步骤

1. 回读原稿核每行真实镜头，排除目录、模板或历史镜号；记录原文件及版本，不只验摘录表。
2. 列全部 ID，检查非空、唯一及引用能找到。默认按显式 shot_order 判断顺序；项目若要求连续编号再查缺号，稳定 ID 有意留号不算错误。
3. 用工具逐行算 `end-start`，与 duration 比较；duration 必须大于零。缺值、单位混用或负时长先停止合计并报行。
4. 连续画面轨道逐对算 `next.start-current.end`：零为连续，正为空档，负为重叠。只有显式叠化/并行轨道方案可接受重叠，并说明时间并集如何计算。声音 J/L-cut 不等于画面时长重复相加。
5. 对每 Scene 汇总 duration 并核起止跨度；连续无重叠时两者相等。再汇总全片、镜数、均值并比较声明目标。没有目标时报告实际估算，不编目标；完整演绎稿允许超预算但标暂不锁时。
6. 比较时间表与当前正文动作负载、标题、Shot List 的映射。并行故事事件不把双方准备时长相加，镜头呈现时长和故事经过时间分账。
7. 逐镜播放 Animatic（有文件时），检验读取、接触、结果、反应与声音，不以算术正确证明表演可读。无 Animatic 标未测试。
8. 修正后重做该 Scene、相邻接口、全片合计及旧引用搜索。只同步实际存在且授权管理的输出；汇总版允许合并，但须有子镜 ID 映射，不强求全文一样。

## 可选工具算术示例（直接运行，不需安装依赖）

以下代码仅算示例表，不读取项目文件。真实任务先替换 rows 与 target，并记录替换后的输入。

```python
from decimal import Decimal as D
rows = [('A-01','0','1.2','1.2'), ('A-02','1.2','3','1.8'), ('A-03','3','5','2')]
assert len({r[0] for r in rows}) == len(rows)
previous = None
total = D('0')
for shot, start, end, duration in rows:
    start, end, duration = map(D, (start, end, duration))
    assert duration > 0 and end-start == duration, shot
    assert previous is None or start == previous, shot
    previous = end
    total += duration
assert total == D('5')
print('count=', len(rows), 'total_seconds=', total)
```

有效输出：`count= 3 total_seconds= 5.0`；这只证明示例算术与连续区间，不是项目验收。

无效输入示例：A-02 的 end 改为 2.9，其他不变。期望报告“A-02 区间长度 1.7 与申报 1.8 不符；到 A-03 有 0.1 秒空档”，而不是自动把片长改掉。若 ID 改成 A-01，另报重复 ID。需要人工裁决的是留空、叠化还是修正时间码，不可默默抹平。

## 交付记录

使用正文公共头，payload 记录输入版本、时间单位、算法/工具或人工方法、逐行差异、Scene/全片合计、目标差额、编号/映射问题、动作负载复核、Animatic 观察范围、未验证项。区分“算术通过”“文本接口通过”“Animatic 通过”，不混称完整生成验证。
