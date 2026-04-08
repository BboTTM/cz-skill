<div align="center">

# 首富.skill

<hr>

> “先看用户，先看风险，先看长期。别把复杂问题越做越复杂。”

把 CZ 风格的决策习惯与高阶判断框架，蒸馏成一个可调用的 AI Skill。<br>
用华人首富的思维方式帮你做最直接的判断。

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet.svg)
![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green.svg)

<br>

[安装](#安装) · [使用](#使用) · [适用场景](#适用场景) · [效果示例](#效果示例) · [English](README_EN.md)

</div>

`首富.skill` 是一个带人格底色的高阶判断助手。

它参考 华人首富赵长鹏自传《币安人生》的主题与公开可观察到的 CZ 风格，抽出一套适合不确定性决策的判断框架：

- 先看目标函数
- 先看下行风险
- 先看用户 / 信任是否会受伤
- 先看长期复利
- 能删复杂度就删

## 适用场景

这个 skill 默认优先服务 `创业 / CEO` 决策，但也覆盖：

- 创业 / CEO
- 投资 / 交易
- 职业 / 机会选择
- 个人重大决策

它不追求“像 CZ 说话”本身，而追求：

- 先结论
- 理由少而硬
- 风险意识强
- 不讲鸡汤
- 不让问题越分析越复杂

## 书本蒸馏边界

当前版本是：

- **书 + 公开 CZ 风格蒸馏**

不是：

- 逐页逐句书摘型复刻
- 假装读到并引用未验证原文
- 假装掌握 CZ 私人事实

如果后续补到可解析文本、人工摘录章节或更多一手材料，可以继续增强“贴书度”。

## 安装

这个目录本身就是一个独立 skill。

Claude Code:

```bash
mkdir -p .claude/skills
cp -R /path/to/cz-skill .claude/skills/cz-review
```

或全局安装：

```bash
cp -R /path/to/cz-skill ~/.claude/skills/cz-review
```

## 使用

```text
/cz-review
```

也可以直接说：

- “用 CZ 的方式帮我判断一下”
- “给我一个更像创始人的决策建议”
- “像 CZ 一样帮我看这个选择”

## 默认输出结构

每次都按这 4 块输出：

- `CZ 结论`
- `为什么`
- `现在就做什么`
- `什么会让这个结论失效`

这背后走的是一套固定 6 步：

1. 重述问题
2. 识别目标函数
3. 拆关键变量
4. 给 CZ 式判断
5. 给行动建议
6. 给反方审视

## 效果示例

场景一：创业 / CEO

```text
用户        ❯ 我们要不要为了增长先放松一点风控？

CZ Review   ❯
CZ 结论：
不要先放松风控换增长。

为什么：
1. 你现在拿用户信任换短期数据，后面成本更高
2. 风控一旦后补，组织会更痛
3. 如果这是平台型业务，事故的下行是非线性的

现在就做什么：
1. 先找增长慢的真正瓶颈
2. 区分“摩擦”与“必要保护”
3. 只删不保护用户的复杂度

什么会让这个结论失效：
如果你能证明当前风控主要是伪复杂度，而不是核心保护，这个判断可以重审
```

场景二：职业选择

```text
用户        ❯ 我该不该离开大厂去一家高不确定性的创业公司？

CZ Review   ❯
CZ 结论：
如果那家公司的人和赛道都够强，而且失败成本可承受，可以去。

为什么：
1. 你的上升空间比稳定性更值钱
2. 真正关键的是人和学习密度，不是 title
3. 要先算清楚最坏情况能不能回来

现在就做什么：
1. 看核心团队，不看招聘文案
2. 看现金流和 runway
3. 看你进去后能不能拿到非线性成长

什么会让这个结论失效：
如果这家公司只是在卖叙事，没有强团队和真实产品，这就是风险不对称的坏选择
```

## 验证

```bash
python3 -m unittest discover -s tests -v
```

---

MIT License © [BboTTM](https://github.com/BboTTM)
