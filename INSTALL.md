# 安装说明

## Claude Code

在仓库外安装：

```bash
mkdir -p ~/.claude/skills
cp -R /path/to/cz-skill ~/.claude/skills/cz-review
```

在项目内安装：

```bash
mkdir -p .claude/skills
cp -R /path/to/cz-skill .claude/skills/cz-review
```

## 调用

```text
/cz-review
```

也可以直接自然语言触发：

- “用 CZ 的方式帮我判断一下”
- “给我一个 CZ 风格的 CEO 决策建议”

## 结构

- `SKILL.md`：主 skill 行为定义
- `prompts/cz_profile.md`：CZ 蒸馏卡
- `prompts/decision_framework.md`：固定决策流程
- `prompts/scenario_templates.md`：四类场景模板
- `tests/`：结构与约束测试
