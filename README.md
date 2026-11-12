# Research Writing Skills

本仓库主要面向**航空航天任务规划与卫星观测调度**研究，提供科研阅读、期刊论文写作、学位论文组织和科研图设计四套 AI 技能。技能使用 `SKILL.md`、参考协议、输出模板和完整提示词组织工作，主要语言为中文，每项重要主张保留来源、页码与证据状态。

## 适用研究方向

| 主要研究方向 | 适合处理的研究问题与材料 |
|---|---|
| 对地观测卫星任务规划 | 观测窗口、姿态切换、资源约束、任务排序、观测与下传协同，以及计划可行性和收益评价 |
| 多星与星座协同调度 | 多星任务分配、协同观测、资源匹配、冲突处理、集中式与分布式规划、滚动重规划和自主任务管理 |
| 移动、机动与时敏目标监测 | 轨迹预测、不确定位置表示、捕获与重访、持续监视与跟踪，以及预测信息与观测决策的接口 |
| 空间碎片与空间目标观测 | 空间态势感知、空间目标协同观测、双星或立体观测任务组织、重访需求与观测资源调度 |
| 观测几何与共享视场方法 | 视线与视场覆盖、预测包络、共同观测可行性、多目标聚合或动态聚类、簇维护及风险约束的建模与验证 |
| 组合优化、启发式与智能调度 | 启发式规则、元启发式、进化算法、遗传规划与超启发式、强化学习辅助决策、多目标优化及算法实验设计 |

四套技能的材料与范例主要来自卫星任务规划、移动目标监测、空间碎片观测和启发式调度文献。期刊与学位论文技能适合组织上述方向的问题模型、方法和实验证据，图形技能适合几何示意、方法框架、调度时序与算法结果图，研究思路技能适合逐篇审读、机制对比和创新核查。

制造调度、物流配送、能源管理、无人系统协同等相邻研究可复用证据记录、优化方法写作和图表设计流程。迁移时需要提供本领域文献、变量与约束定义、评价指标和真实实验资料，并重新核对领域假设。跨学科使用时，依据目标领域的专业规范调整模板和术语。

使用时请注明具体研究方向、研究对象及工作状态，例如“空间碎片多星协同观测，已有调度模型与仿真数据，需修改期刊论文方法节”。涉及不同目标速度、传感器或平台的研究，按各自的动力学、观测模型和时效要求检查适用条件。新增包络、聚类或风险模型的性能与性质需要相应推导和实验支持。

## 四套技能

| 技能 | 适用任务 | 主要产物 | 入口 |
|---|---|---|---|
| `journal-paper-writing` | 期刊论文新写、改写、结构重构、创新审计、实验规划和审稿回复 | 证据矩阵、贡献审计、章节提纲、正文与实验计划 | [技能说明](skills/journal-paper-writing/SKILL.md) · [完整提示词](skills/journal-paper-writing/references/full-prompt.md) |
| `degree-thesis-writing` | 学位论文总论证链、章节设计、小论文整合和符号一致性 | 子问题与章节矩阵、详细目录、章节正文、接口与符号检查表 | [技能说明](skills/degree-thesis-writing/SKILL.md) · [完整提示词](skills/degree-thesis-writing/references/full-prompt.md) |
| `scientific-figure-design` | 参考图分析、科研图风格比较、方法框架与可编辑图稿设计 | 逐图视觉卡、风格来源、绘图规格、SVG/PNG 图稿和图注 | [技能说明](skills/scientific-figure-design/SKILL.md) · [完整提示词](skills/scientific-figure-design/references/full-prompt.md) |
| `research-idea-organizer` | 单篇或批量论文审读、机制对比、创新核查和研究思路整理 | 文献清单、单篇报告、对比矩阵、研究缺口和可检验思路卡 | [技能说明](skills/research-idea-organizer/SKILL.md) · [完整提示词](skills/research-idea-organizer/references/full-prompt.md) |

## 快速使用

克隆本仓库后，选择与你当前任务对应的完整技能目录，按照所用 AI 工具的技能加载方式配置。保留目录中的 `references/` 和 `scripts/`，使相对资源引用有效。

```bash
git clone https://github.com/nuaazxx/research-writing-skills.git
cd research-writing-skills
```

也可以打开表中的“完整提示词”，填写研究问题、输入材料、输出位置和格式要求后直接使用。各套技能提供独立 ZIP，解压后即可获得完整技能目录。

| 技能包 | 下载 |
|---|---|
| 期刊论文写作 | [journal-paper-writing.zip](packages/journal-paper-writing.zip) |
| 学位论文写作 | [degree-thesis-writing.zip](packages/degree-thesis-writing.zip) |
| 科研图设计 | [scientific-figure-design.zip](packages/scientific-figure-design.zip) |
| 研究思路整理 | [research-idea-organizer.zip](packages/research-idea-organizer.zip) |

文献研究可以先使用 `research-idea-organizer` 建立证据记录，再使用期刊或学位论文技能组织论证，并通过 `scientific-figure-design` 制定图表规格。已有明确任务时可以直接使用对应技能。

## 任务示例

### 期刊论文

```text
使用 journal-paper-writing。
根据我提供的研究方案、指定文献和真实实验记录，整理贡献证据矩阵，
撰写引言、问题描述和方法章节。每个新公式后用“式中”解释符号和单位，
使用普通变量。请明确列出尚需实验支持的主张，并保存到指定目录。
```

### 学位论文

```text
使用 degree-thesis-writing。
根据总研究问题、已有目录和各章材料，建立子问题与章节矩阵，
检查时间尺度、坐标系、符号、假设和实验条件，形成详细目录与章节修改稿。
请标明章间接口的实现状态，并保存一致性检查表。
```

### 科研图

```text
使用 scientific-figure-design。
读取指定论文的完整图页，记录可见元素、布局、箭头语义、配色和图注，
为我的方法框架制定绘图规格，生成可编辑 SVG 和 PNG。
请提供各项参考属性的来源，并查看实际导出文件后交付。
```

### 文献与研究思路

```text
使用 research-idea-organizer，MODE=FULL。
非递归读取我明确提供的 PDF 目录，每篇独立分析并核验关键原页，
质检后进行跨论文机制对比，整理当前语料支持的研究缺口与可检验思路卡。
请保存清单、逐篇报告、图卡、综合矩阵和质量记录。
```

## 目录结构

```text
research-writing-skills/
├── README.md
├── skills/
│   ├── journal-paper-writing/
│   ├── degree-thesis-writing/
│   ├── scientific-figure-design/
│   └── research-idea-organizer/
└── packages/
    ├── journal-paper-writing.zip
    ├── degree-thesis-writing.zip
    ├── scientific-figure-design.zip
    └── research-idea-organizer.zip
```

每套技能包含 7 个文件。

| 文件 | 用途 |
|---|---|
| `SKILL.md` | 触发场景、输入要求、执行过程和质量检查 |
| `references/evidence-protocol.md` | 来源、页码、证据状态和材料隔离规则 |
| `references/output-templates.md` | 可直接填写的输出结构 |
| `references/full-prompt.md` | 完整可复制任务提示词 |
| `references/corpus-patterns.md` | 有来源的阅读、写作或图形操作范例 |
| `references/tool-usage.md` | PDF 清单工具的参数和使用方法 |
| `scripts/pdf_batch_manifest.py` | PDF 盘点、SHA-256、页数、重复与阻塞记录 |

`corpus-patterns.md` 中的论文编号与 DOI 用于定位范例，物理页码依对应 PDF 版本。处理用户限定的单篇或材料集合时，按技能说明加载指定资料与必要协议。原始论文需要由使用者提供。

## 来源与证据记录

| 状态 | 含义 |
|---|---|
| `SUPPORTED` | 来源明确陈述，附页码和定位 |
| `INFERENCE` | 分析推断或新设计，附依据和适用范围 |
| `NOT_REPORTED` | 已检查相关范围后确认缺少报告项，注明检查范围 |
| `UNKNOWN` | 输入、定义或证据不足，列出待确认材料 |
| `EXTRACTION_UNCERTAIN` | 乱码、公式错序、图像模糊等提取问题，记录复核动作 |

四套技能均要求重要公式、关键数值、表头和方法图回到完整原页核验。实验比较保留场景、指标、数据、硬件、预算和统计口径。新稿公式使用普通变量，并在公式后用“式中”说明符号。

## PDF 清单工具

阅读技能和使用提示词可以直接从文档开始。运行附带的 PDF 盘点脚本需要 Python 3.11+ 和 PyMuPDF，批次验证使用 PyMuPDF 1.25.2。

```powershell
python -m pip install "PyMuPDF==1.25.2"
python skills/research-idea-organizer/scripts/pdf_batch_manifest.py "D:\papers" --output "D:\research-output\manifest.json"
```

脚本接受多个明确目录或 PDF，默认只读取目录中的直接文件。需要递归时添加 `--recursive`。运行后生成 JSON 和 CSV，记录文件路径、SHA-256、文件大小、页数、重复关系和损坏或加密阻塞。已有输出文件会触发退出，请选择新的输出位置。

## 已执行的验证

四套技能已完成 YAML 与必要内容检查、资源引用检查，以及 ZIP 成员、CRC、哈希和文件字节一致性检查。行为验收于 2026-11-12 批次完成。

| 技能 | 实际验收范围 |
|---|---|
| 期刊论文写作 | 单篇限定材料的贡献与正文审查、来源归属、缺实验处理。初测发现范例污染后修订，并在新上下文重测通过 |
| 学位论文写作 | 两份冻结摘要的章节映射、拟议接口及符号一致性 |
| 科研图设计 | 完整原页与缺图场景的处理，SVG/PNG 概念图生成及彩色、灰度查看 |
| 研究思路整理 | 两篇相近文献的机制隔离、证据边界和待验证思路卡 |

PDF 盘点工具也检查了默认非递归、显式递归、大写扩展名、重复路径、相同内容、有效页数、损坏 PDF 和缺路径处理。上述验收覆盖有限样例。使用新领域、不同工具或投稿模板时，需要结合实际任务继续检查，算法复现和科研性能结论由相应原始材料与实验支持。

2026-11-12 补充研究方向说明后，已核对 README、四套技能入口描述与四份完整提示词的领域表述，并检查重新打包的 ZIP 与技能源文件逐字节一致。本次检查针对适用范围与文档一致性，既有工作流程的行为验收范围见上表。
