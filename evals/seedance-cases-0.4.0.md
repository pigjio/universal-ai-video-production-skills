# 0.4.0 Seedance 文本工作流验证

> 验证类型：真实 Agent 读取当前 Skill 与条件 references 后完成文本任务。未调用 Seedance、未上传、未付费、未观看真实媒体；不代表平台生成质量或人工艺术认可。

## 用例与结果

| 用例 | 目标能力 | 结果 | 可核验输出 |
|---|---|---|---|
| 1. 三镜正式请求 | 正式 DO、素材职责、逐镜五字段、未知能力与授权边界 | 通过；Agent 还识别出“放入盒内但盒子保持关闭”的输入物理冲突并阻断放行 | `runs/seedance-0.4.0/case-1-formal-request/output.md` |
| 2. 四镜生产分组 | shot/production_group/request/edit_unit、任务合同、长短/桥接候选、四时长 | 通过；当前能力保持 unknown，生产状态 planned，没有虚构提交或输出 | `runs/seedance-0.4.0/case-2-grouping/output.md` |
| 3. 证据不足的视频评审 | 十维评审、症状≠根因、尾帧禁传、修复层级、最小试验 | 通过；不支持直接重做角色母版，声音/动作连续性标不可确认，截图不可直接续接，试验 not_run、人工 pending | `runs/seedance-0.4.0/case-3-review/output.md` |

## 程序化关键词检查

三份输出均存在，且命中各自必要结构：

- Case 1：`planned`、三镜 ID、主体边界、参考职责、镜头任务、构图动作、摄影机、声音、未授权与冲突；
- Case 2：四层单位、四种时长、unknown、planned、await_user_authorization；
- Case 3：十维名称、unconfirmable、pending、not_run、角色母版证据限制与尾帧阻断。

Case 3 没有机械使用“不得直接”四字，但明确写出“不得把该截图上传为下一段参考”，语义门成立。

## 限制

- 每个用例只运行一次，不能得出统计稳定性；
- 没有 baseline 对照，不能宣称比 0.3.0 有量化提升；
- 没有真实平台能力复核，不确认当前时长、槽位、音频或字符上限；
- 没有真实媒体，因此 Case 3 只验证证据边界和诊断路由；
- 尚未获得外部创作者的人类使用反馈。
