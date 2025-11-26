# URL 去重工具

这个 Python 脚本可以处理一组 URL，将它们标准化并去除冗余部分，确保去掉重复、不相关的 URL，并将它们转换为一致的格式。该工具旨在简化 URL 分析和去重工作。

---

## 功能

- **协议标准化**：将所有 URL 转换为使用 `https` 协议。
- **路径清理**：去除多余的斜杠（`//`）并标准化路径格式。
- **静态文件排除**：过滤掉指向静态文件（如图片、JavaScript、CSS 等）的 URL。
- **内容过滤**：忽略博客文章、新闻文章和分页内容。
- **动态路径标准化**：将路径中的数字 ID 和日期替换为占位符（例如：`/cat/9/details.html` 转换为 `/cat/id/details.html`）。
- **查询参数处理**：
  - 去除多余的跟踪参数（如 `utm_source`、`ref`、`session_id` 等）。
  - 标准化并统一处理特定的查询参数，如 `id` 和 `page`。
  - 按字母顺序排序查询参数，确保一致的排序。
- **去除锚点**：去掉 URL 中的锚点（`#` 后面的部分）。
- **域名标准化**：将域名转换为小写。
- **去重**：确保输出的 URL 仅包含唯一的地址。

---

## 安装

1. 克隆该项目：
   ```bash
   git clone https://github.com/XiaomingX/url-declustering-tool.git
   cd url-declustering-tool
   ```
2. 确保你已经安装了 Python 3：
   ```bash
   python3 --version
   ```
3. （可选）创建一个虚拟环境并安装依赖：
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

---

## 使用

1. 运行脚本并查看示例输入：
   ```bash
   python3 decluster_urls_optimized.py
   ```
2. 修改 `main()` 函数中的 `input_urls` 列表，以测试自定义的 URL。

---

## 示例

### 输入
```plaintext
http://example.com/page.php?id=1
http://example.com/page.php?id=3&page=2
http://example.com/cat/9/details.html
http://example.com/2021/08/01/article-title
http://example.com/assets/background.jpg
http://example.com/?utm_source=google&utm_medium=cpc
```

### 输出
```plaintext
https://example.com/page.php?id=id
https://example.com/cat/id/details.html
https://example.com/yyyy/mm/dd/
```

---

## 工作原理

1. **解析**：使用 `urllib.parse` 对每个 URL 进行解析，提取出协议、域名、路径、查询参数等组件。
2. **转换**：
   - 清理并标准化路径。
   - 处理查询参数，移除无关参数并规范化重要参数。
3. **去重**：将处理后的 URL 与已处理的 URL 集合进行对比，确保不重复。
4. **输出**：返回一组去重后的 URL 列表。

---

## 自定义

你可以通过编辑 `decluster_urls` 函数中的相应部分来调整过滤逻辑或标准化规则。例如：
- 在 `endswith` 检查中添加或移除静态文件扩展名。
- 修改不必要的查询参数列表。
- 更新正则表达式以匹配额外的动态路径。
