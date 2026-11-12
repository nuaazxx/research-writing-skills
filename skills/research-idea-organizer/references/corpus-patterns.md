# 有限语料中的可迁移研究操作

本文件是操作范例，不是完整领域结论。每篇仍保持独立机制；用户限定材料时不要加载本文件。页码仅对应本批PDF版本。

1. **按真实决策对象分层。** P002从位置样本得到条带捕获概率，再构建跨圈调度；P005优化每星每目标连续ΔV；P003优化离散时刻的一对一指派。统一称“任务规划”并不能允许共用一个解编码。[P002, PDF p.3–8, Sec.3–4]; [P005, PDF p.3–4, Sec.II]; [P003, PDF p.2–5, Sec.III–IV]
2. **将候选表示与减少候选分开。** P029统一网格后按平台方向/位置展开元任务；P017形成复合元任务；P027检查现有任务可共享的视场与时间区间。可以迁移“先定义候选语义，再报告规模变化”，不能把三者统称同一种聚类。[P029, PDF p.38–45, Sec.3.1]; [P017, PDF p.43–44, Sec.4.2.2]; [P027, PDF p.47–50, Sec.3.4]
3. **寻找反馈发生的位置。** P017的合成收益反馈分配；P022下游收益指导离线规则演化、另有在线拒绝重试；P018真实量测与虚拟更新承担不同延时职责。新研究应写清反馈对象、触发与循环终止，不能声称这些文献均为无反馈串行流程。[P017, PDF p.38, Fig.4.1]; [P022, PDF p.128/162, Figs.5.8/6.9]; [P018, PDF p.111–114, Figs.4.5–4.6]
4. **同时追踪收益、成本与保证。** P005多指标解体现权衡；P029缓存评价的O(1)限单次变更；P003近似界含收益前提。研究增量必须配套适用条件、总开销和反例场景。[P005, PDF p.7, Tables5–7]; [P029, PDF p.59–62, Sec.4.3]; [P003, PDF p.3/5, TheoremsIII.3/IV.1]
5. **以组件证据而非命名证明创新。** P004有重启开关及参数实验，P029有邻域消融，P027有聚合开关。可迁移“每项贡献对应一个能否定它的对照”，但这些实验的完整度与适用范围不同，不能合并成通用性能证明。[P004, PDF p.7–10, Sec.IV–VI]; [P029, PDF p.65–67, Sec.4.4.3–4.4.4]; [P027, PDF p.68–71, Sec.4.2.5]

来源：P002 Han等《Continuous monitoring scheduling for moving targets by Earth observation satellites》(2023)；P003 Holder等《Centralized and Distributed Strategies for Handover-Aware Task Allocation in Satellite Constellations》(2025)；P004 Liu等《A Novel Spaceborne SAR Constellation Scheduling Algorithm for Sea Surface Moving Target Search Tasks》(2024)；P005 Morgan等《Optimization of Multispacecraft Maneuvers for Mobile Target Tracking from Low Earth Orbit》(2023)；P017《对地观测卫星任务规划方法研究》(封面2023)；P018《天基海洋移动目标监视的联合调度问题研究》(2011)；P022《面向移动目标跟踪的多星协同规划与自主调度研究》(封面2021)；P027《面向空间移动目标跟踪的中低轨卫星星座自主协同调度方法研究》(封面2022)；P029《面向海上目标搜索的多平台联合任务规划方法研究》(2020)。
