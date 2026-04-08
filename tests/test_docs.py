import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CzSkillDocsTest(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            ROOT / "SKILL.md",
            ROOT / "README.md",
            ROOT / "README_EN.md",
            ROOT / "INSTALL.md",
            ROOT / "agents" / "openai.yaml",
            ROOT / "prompts" / "cz_profile.md",
            ROOT / "prompts" / "decision_framework.md",
            ROOT / "prompts" / "scenario_templates.md",
        ]
        for path in required:
            self.assertTrue(path.exists(), msg=f"missing {path}")

    def test_skill_contains_required_sections_and_boundaries(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: cz-review", skill)
        self.assertIn("## 固定工作流", skill)
        self.assertIn("### CZ 结论", skill)
        self.assertIn("不伪装成 CZ 本人", skill)
        self.assertIn("不捏造书中原话", skill)

    def test_profile_and_framework_capture_expected_axes(self):
        profile = (ROOT / "prompts" / "cz_profile.md").read_text(encoding="utf-8")
        framework = (ROOT / "prompts" / "decision_framework.md").read_text(encoding="utf-8")
        scenarios = (ROOT / "prompts" / "scenario_templates.md").read_text(encoding="utf-8")
        self.assertIn("用户优先", profile)
        self.assertIn("长期主义", profile)
        self.assertIn("语言风格", profile)
        self.assertIn("重述问题", framework)
        self.assertIn("识别目标函数", framework)
        self.assertIn("给反方审视", framework)
        self.assertIn("创业 / CEO", scenarios)
        self.assertIn("投资 / 交易", scenarios)
        self.assertIn("职业 / 机会选择", scenarios)
        self.assertIn("个人重大决策", scenarios)


if __name__ == "__main__":
    unittest.main()
