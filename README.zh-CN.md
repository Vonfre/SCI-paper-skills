# SCI-paper-skills

[English](README.md) | [简体中文](README.zh-CN.md)

`SCI-paper-skills` 是一套面向目标期刊自适应的 Codex 技能套件，用于把真实研究结果整理成逻辑清晰、证据边界明确的 SCI/SCIE 论文。

它面向已经拥有数据、图表、结论、初步想法、草稿、范文或审稿意见的研究生和科研人员，帮助用户组织论文逻辑、控制论点强度、寻找文献证据、模仿目标期刊结构、润色语言，并准备投稿或返修材料。

## 快速安装

克隆仓库后，将所有技能文件夹同步到本地 Codex skills 目录：

```bash
git clone https://github.com/Vonfre/SCI-paper-skills.git
cd SCI-paper-skills
bash scripts/sync_codex_skills.sh
```

脚本默认安装到 `~/.codex/skills`。如果要安装到其他目录：

```bash
CODEX_SKILLS_DIR=/path/to/skills bash scripts/sync_codex_skills.sh
```

安装后调用主控技能：

```text
$sci-paper-skills
```

第一次回复只应提出下一步最有用的问题：

1. 你希望投稿到哪个期刊？如果还没确定，请列出候选期刊或目标档次。
2. 你的研究主题、领域、研究对象/材料/体系，以及已知的文章类型是什么？
3. 你目前已经有什么：科学问题、结论、图表/数据、提纲、草稿、PDF/范文，或审稿意见？

如果用户已经提供了足够上下文，技能应直接推进，并用 `[NEED: ...]` 标记缺失信息。

## 技能索引

| 状态 | 阶段 | 技能 | 触发场景 | 主要产物 |
|---|---:|---|---|---|
| 稳定 | 0 | `sci-stage-diagnosis` | 不知道论文项目卡在哪一步 | 阶段诊断 |
| 稳定 | 1 | `sci-intake-router` | 新项目或上下文不足 | 输入简报 |
| 稳定 | 2 | `sci-journal-landscape` | 有目标期刊、候选期刊或期刊适配问题 | 期刊画像 |
| 稳定 | 3 | `sci-literature-evidence` | 需要支持、冲突、缺口、新颖性或方向证据 | 证据图谱 |
| 稳定 | 4 | `sci-result-to-claim` | 有结果/图表但论点不清楚 | 结果-论点矩阵 |
| 稳定 | 5 | `sci-core-story-finder` | 有多个可能结论或中心信息不明确 | 故事决策备忘录 |
| 稳定 | 6 | `sci-figure-story-builder` | 图表/表格/案例需要排序和主文-补充材料取舍 | 图表故事图 |
| 稳定 | 7 | `sci-storyline-planner` | 需要论文结构或备选写作逻辑 | 故事线方案 |
| 稳定 | 8 | `sci-reviewer-simulator` | 投稿前想预判编辑/审稿人风险 | 审稿风险报告 |
| 稳定 | 9 | `sci-draft-mimic` | 基于范文起草，但不复制原文表达 | 初稿包 |
| 稳定 | 10 | `sci-paragraph-coach` | 需要段落级写作辅导 | 段落辅导块 |
| 稳定 | 11 | `sci-language-polisher` | 含义已稳定，需要表达润色 | 润色报告 |
| 稳定 | 12 | `sci-citation-control` | 需要引用位置、证据审计或参考文献格式 | 引用审计 |
| 稳定 | 13 | `sci-submission-revision` | 投稿文件、投稿信、审稿回复或返修计划 | 投稿/返修包 |

更详细的触发和交接关系见 [docs/skill-index.md](docs/skill-index.md)。

## 工作流

```text
诊断 -> 输入收集 -> 期刊画像 -> 文献证据 -> 结果到论点
-> 中心故事 -> 图表故事 -> 论文结构 -> 审稿模拟
-> 范文模仿起草 -> 段落辅导 -> 语言润色 -> 引用控制
-> 投稿或返修
```

除非用户明确指定某个模块，主控技能会按阶段顺序推进。

## 设计原则

- 先诊断，再起草。
- 将期刊适配、文献证据、论点强度和图表逻辑作为不同关卡处理。
- 每个阶段都生成一个有名称的交接产物。
- 对复杂写作任务使用可复用的 prompt card 和有来源支撑的提纲。
- 对文献、引用、新颖性和矛盾证据检查维护来源台账（source ledger）。
- 用 `[NEED: ...]` 明确标记缺失事实。
- 用 `[CITE: ...]` 明确标记未核验的引用需求。
- 只模仿范文的结构和修辞功能，不模仿有辨识度的原文表达。
- 对期刊事实、政策、指标、APC/OA 和近期文献使用当前网络研究。
- 不编造数据、参考文献、审批信息、登录号、方法、发现、统计结果或期刊要求。

共享运行标准见 [docs/design-principles.md](docs/design-principles.md)。
外部高星项目的可迁移模式见 [docs/inspiration-high-star-writing-research-projects.md](docs/inspiration-high-star-writing-research-projects.md)。

## 仓库结构

```text
README.md
README.zh-CN.md
manifest.yaml
docs/
scripts/
sci-paper-skills/
sci-stage-diagnosis/
sci-intake-router/
...
```

每个技能文件夹都遵循标准 Codex skill 结构：

```text
SKILL.md
agents/openai.yaml
references/
```

根目录下的技能文件夹刻意保持扁平结构，方便直接复制到 Codex skills 目录。

## 项目脚手架

主控技能包含一个辅助脚本：

```bash
python sci-paper-skills/scripts/init_journal_project.py \
  --journal "The Plant Cell" \
  --topic "ABA stomatal closure" \
  --out ./journal-projects
```

生成的 `journal-projects/` 文件夹是本地工作产物，并已被 Git 忽略。

## 验证

运行本地技能包检查：

```bash
bash scripts/validate_skill_pack.sh
```

发布较大的技能改动前，也应使用 skill creator 的 `quick_validate.py` 工具验证每个技能。如果内置运行时缺少 PyYAML，请使用已安装 `yaml` 的系统 `python3`。

## 新增技能规范

新增模块应包含：

- 带有 `name` 和 `description` frontmatter 的 `SKILL.md`。
- `agents/openai.yaml`。
- 如果需要模板或质量规则，至少提供一个聚焦的 `references/` 文件。
- 在 `manifest.yaml` 中新增一行。
- 在 [docs/skill-index.md](docs/skill-index.md) 中新增一行。
- 明确的阶段交接产物，能够供其他阶段继续使用。
