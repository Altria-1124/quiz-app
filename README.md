# 📝 刷题软件

一个功能全面的 Web 刷题应用，支持选择题、判断题、填空题、简答题，提供顺序/随机/错题重练/模拟考试四种模式，附带成绩统计。

## 🚀 快速开始

直接双击打开 `index.html` 即可使用（需浏览器支持，建议 Chrome / Edge / Firefox）。

> **在线使用：** 部署到 GitHub Pages 后，任何人在浏览器打开链接就能用。

## 📚 题库格式

题库文件位于 `data/questions.json`，按以下格式添加题目：

### 选择题 (choice)
```json
{
  "id": 1,
  "type": "choice",
  "category": "JavaScript 基础",
  "difficulty": "easy",
  "question": "JavaScript 中，typeof null 的结果是什么？",
  "options": ["null", "undefined", "object", "boolean"],
  "answer": 2,
  "explanation": "typeof null 返回 'object'，这是 JavaScript 的一个历史遗留 bug。"
}
```
- `answer`: 正确选项的索引（从 0 开始）

### 判断题 (truefalse)
```json
{
  "id": 4,
  "type": "truefalse",
  "category": "JavaScript 基础",
  "difficulty": "easy",
  "question": "JavaScript 是一种强类型语言。",
  "answer": false,
  "explanation": "JavaScript 是弱类型（动态类型）语言。"
}
```
- `answer`: `true` 或 `false`

### 填空题 (fillblank)
```json
{
  "id": 6,
  "type": "fillblank",
  "category": "JavaScript 基础",
  "difficulty": "easy",
  "question": "声明常量的关键字是 ______。",
  "answer": "const",
  "alternatives": ["const"],
  "explanation": "const 关键字用于声明常量。"
}
```
- `answer`: 标准答案
- `alternatives`: 可接受的其他答案（可选）
- 判题时忽略大小写

### 简答题 (shortanswer)
```json
{
  "id": 8,
  "type": "shortanswer",
  "category": "JavaScript 基础",
  "difficulty": "medium",
  "question": "请简述 let、const 和 var 的区别。",
  "answer": ["块级作用域", "不可重新赋值", "函数级作用域", "变量提升"],
  "explanation": "var：函数作用域，有变量提升..."
}
```
- `answer`: **字符串数组**，每个元素是一个关键词。用户答案包含 60% 以上关键词即判为正确。

### 通用字段说明

| 字段 | 必填 | 说明 |
|------|------|------|
| `id` | 是 | 唯一标识，数字 |
| `type` | 是 | `choice` / `truefalse` / `fillblank` / `shortanswer` |
| `category` | 是 | 分类名称，用于筛选和统计 |
| `difficulty` | 是 | `easy` / `medium` / `hard` |
| `question` | 是 | 题目内容 |
| `answer` | 是 | 正确答案 |
| `explanation` | 否 | 答案解析 |
| `options` | 仅选择题 | 选项数组 |

## 🌐 部署到免费托管平台

### 方案一：GitHub Pages（推荐）

1. 在 GitHub 创建一个新仓库（如 `quiz-app`）
2. 将整个 `quiz-app` 文件夹推送到仓库：

```bash
cd e:/quiz-app
git init
git add .
git commit -m "初始化刷题软件"
git branch -M main
git remote add origin https://github.com/你的用户名/quiz-app.git
git push -u origin main
```

3. 在仓库 Settings → Pages → Source 选择 `main` 分支，保存
4. 几分钟后访问 `https://你的用户名.github.io/quiz-app/` 即可

### 方案二：Vercel

1. 注册 [vercel.com](https://vercel.com)（用 GitHub 账号登录）
2. 导入 GitHub 仓库，一键部署
3. 获得 `https://你的项目.vercel.app` 链接

### 方案三：Cloudflare Pages

1. 注册 Cloudflare，进入 Pages
2. 连接 GitHub 仓库
3. 构建命令留空，输出目录留空（纯静态）
4. 部署后获得 `https://你的项目.pages.dev` 链接

## 🔧 功能说明

| 功能 | 说明 |
|------|------|
| 顺序刷题 | 按题库顺序逐题练习 |
| 随机抽题 | 打乱顺序随机练习 |
| 错题重练 | 仅复习之前做错的题目 |
| 模拟考试 | 设置题目数量和时间限制，提交后统一判分 |
| 分类筛选 | 按知识分类过滤题目 |
| 难度筛选 | 按简单/中等/困难过滤 |
| 题型筛选 | 按题型过滤 |
| 成绩统计 | 记录总答题数、正确率、分类正确率、错题列表 |
| 数据存储 | 使用 localStorage 保存在浏览器本地 |

## ⚠️ 注意事项

- 统计数据存储在浏览器 localStorage 中，清除浏览器数据会导致统计丢失
- 题库更新后，部署的版本自动同步；本地使用需自行替换 `questions.json`
- 建议 ID 从 1 开始连续递增，方便管理

## 📄 许可

MIT License - 自由使用和修改