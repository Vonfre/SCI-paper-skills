# SCI-paper-skills

[English](README.md) | [简体中文](README.zh-CN.md)

`SCI-paper-skills` 是一套面向目标期刊自适应的技能套件，用于把真实研究结果整理成逻辑清晰、证据边界明确的 SCI/SCIE 论文。

它面向已经拥有数据、图表、结论或初步想法的研究生和科研人员，帮助用户组织论文逻辑、用文献支撑论点、模仿目标期刊的写作模式，并逐步准备接近投稿状态的稿件。

## 入口

使用主控技能：

```text
$sci-paper-skills
```

第一次回复只应提出下一步最有用的问题：

1. 你希望投稿到哪个期刊？如果还没确定，请列出候选期刊或目标档次。
2. 你的研究主题、领域、研究对象/材料/体系，以及已知的文章类型是什么？
3. 你目前已经有什么：科学问题、结论、图表/数据、提纲、草稿、PDF/范文，或审稿意见？

如果用户已经提供了足够上下文，技能应直接推进，并用 `[NEED: ...]` 标记缺失信息。

## 核心流程

| 阶段 | 技能 | 任务 | 主要产物 |
|---:|---|---|---|
| 0 | `sci-stage-diagnosis` | 诊断论文项目卡在哪一步。 | 阶段诊断 |
| 1 | `sci-intake-router` | 收集期刊、主题、体系、材料并决定路线。 | 输入简报 |
| 2 | `sci-journal-landscape` | 分析目标期刊并寻找可比论文。 | 期刊画像 |
| 3 | `sci-literature-evidence` | 检查科学问题/结论是否被文献支持或挑战。 | 证据图谱 |
| 4 | `sci-result-to-claim` | 将结果和图表转换成可辩护的论点。 | 结果-论点矩阵 |
| 5 | `sci-core-story-finder` | 选择论文的中心科学故事。 | 故事决策备忘录 |
| 6 | `sci-figure-story-builder` | 将图表、表格和案例组织成读者逻辑。 | 图表故事图 |
| 7 | `sci-storyline-planner` | 设计论文结构和备选逻辑。 | 故事线方案 |
| 8 | `sci-reviewer-simulator` | 在投稿前预测编辑和审稿人的主要质疑。 | 审稿风险报告 |
| 9 | `sci-draft-mimic` | 模仿范文结构和修辞动作起草，而不是复制文字。 | 初稿包 |
| 10 | `sci-paragraph-coach` | 教学并撰写段落级内容。 | 段落辅导块 |
| 11 | `sci-language-polisher` | 在保留含义和证据边界的前提下润色表达。 | 润色报告 |
| 12 | `sci-citation-control` | 检查论点、证据和参考文献之间的一致性及格式。 | 引用审计 |
| 13 | `sci-submission-revision` | 准备投稿文件或返修回应材料。 | 投稿/返修包 |

## 套件如何自适应

- 如果用户已有目标期刊，先建立期刊画像，并搜索同刊相似论文。
- 如果目标期刊没有足够相似论文，则搜索同层级或相邻期刊论文，并说明可比原因。
- 如果用户已有结论，则搜索文献来支持、挑战或弱化这些结论。
- 如果用户还没有结论，则基于近期文献提出可能的研究方向。
- 如果用户已有写作逻辑，则改进现有逻辑。
- 如果用户还没有写作逻辑，则根据可比文献和用户证据推导多个可能的论文结构。
- 如果用户提供 PDF 或范文，则提取结构、修辞动作、图表引用方式、补充材料风格和论点强度，再进行结构性模仿，避免复制语言。
- 如果用户没有论文写作经验，则给出一个具体的下一步任务，而不是一长串抽象清单。

## 活跃技能

- `sci-paper-skills`：主控技能和完整工作流控制器。
- `sci-stage-diagnosis`：阶段诊断和下一步选择。
- `sci-intake-router`：第一步问题收集和路线分配。
- `sci-journal-landscape`：期刊画像和可比论文扫描。
- `sci-literature-evidence`：文献支持、冲突和方向映射。
- `sci-result-to-claim`：结果到论点的转换与证据缺口控制。
- `sci-core-story-finder`：中心故事选择。
- `sci-figure-story-builder`：图表和案例叙事构建。
- `sci-storyline-planner`：论文逻辑规划。
- `sci-reviewer-simulator`：投稿前审稿风险模拟。
- `sci-draft-mimic`：基于范文的初稿生成。
- `sci-paragraph-coach`：段落级写作辅导。
- `sci-language-polisher`：最终科学语言润色。
- `sci-citation-control`：引用和证据控制。
- `sci-submission-revision`：投稿和返修支持。

## 项目脚手架

主控技能包含一个辅助脚本：

```bash
python sci-paper-skills/scripts/init_journal_project.py   --journal "The Plant Cell"   --topic "ABA stomatal closure"   --out ./journal-projects
```

生成的项目文件夹是本地工作产物，并已被 Git 忽略。

## 质量规则

- 不编造数据、参考文献、统计结果、伦理/审批信息、登录号、方法、发现或期刊要求。
- 对期刊事实、文章列表、指标、开放获取/APC、政策和近期文献使用当前网络研究。
- 区分用户数据、文献支持、解释、推测和缺乏支持的论断。
- 让论点强度匹配证据：观察、关联、调控、机制、因果、验证和应用是不同层级。
- 只有在期刊适配、文献支持、结果-论点映射、中心故事、图表逻辑和引用需求足够清晰后才开始起草。
- 每个阶段都应生成可交接给下一阶段的产物，以保持过程可追溯。

## 打包说明

- 生成的 `journal-projects/` 文件夹是本地工作产物，并已被 Git 忽略。
- 最终工作流使用当前活跃的 14 阶段模块集；已移除的旧模块不应作为工作阶段重新引入。
- 每个活跃模块保持简短的 `SKILL.md`，并链接到一级 `references/` 文件中的模板和质量规则。

## 验证

每个技能都是标准 Codex skill 文件夹，包含：

```text
SKILL.md
agents/openai.yaml
references/
```

发布更改前，使用 skill creator 的 `quick_validate.py` 工具验证每个技能。如果内置运行时缺少 PyYAML，请使用已安装 `yaml` 的系统 `python3`。
