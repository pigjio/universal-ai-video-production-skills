# 续接、剪辑采用与输出验证

## 1. 续接来源

```yaml
continuation_interface:
  source: real_tail_frame | textual_reconstruction | independent_restart | verified_context | none
  source_artifact: null
  source_timecode: null
  observed_interval: null
  extracted_file: null
  upload_receipt: null
  known_state: {}
  unknowns: []
  eligible_for_reuse: false
  blocked_by: []
  next_request_obligations: []
```

真实尾帧必须连续观看邻近区间；单帧可判形态，不能证明速度、动作顺序和声音。身份、空间、刚性几何、方向、关键道具或动作相位错误时 `eligible_for_reuse: false`。

文字重建列明位置、朝向、支撑、持有物、动作相位、环境、光色、声音尾音及未知项；不得称像素级连续。下一请求第一镜建立既成状态并禁止重演已完成动作。

## 2. 长窗合并和桥接

合并相邻生产组进行长窗试验时：

1. 新建独立 `generation_request`，不覆盖接受基线；
2. 将旧边界改写为组内连续运动，不简单粘接 Prompt；
3. 重算镜头节点与请求窗口；
4. 记录合并风险、接口减少收益和失败回退；
5. 真实结果必须重新评审，不能因请求成功自动晋级。

只有接口失败而主体段通过时，优先短桥接、pickup 或调整合法切点；不能用剪辑隐藏必须可见的接触、Reaction 或结果。

## 3. 剪辑采用记录

```yaml
edit_delivery:
  sequence_id: SEQ-example
  edit_units:
    - edit_unit_id: EDIT-example
      source_request_id: REQ-example
      source_output_id: null
      track: V1
      planned_in_out: null
      actual_in_out: null
      transition_in: cut
      transition_out: cut
      audio_bridge: null
      replacement_for: null
  export:
    output_file: null
    actual_duration: null
    aspect_ratio_verified: false
    playback_verified: false
    audio_tracks_verified: false
    subtitles_verified: false
    watermark_verified: false
```

未拿到结果时只能填 `planned_in_out`；未实际裁切时 `actual_in_out` 保持空。没有剪辑工具就交 EDL/决策表，不宣称成片已导出。

## 4. 输出验证

最终交付必须追溯：

- 每个采用段的源 output/resource ID；
- 实际 in/out、变速、镜像、替换和转场；
- 声音来源、同步、混音和桥接；
- 最终采用版本与被替换版本；
- 文件真实存在、可播放、时长、画幅和音轨；
- 字幕、水印和导出编码是否符合交付要求。

未执行的检查明确标未验证。
