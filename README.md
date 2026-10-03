# 有容乃大原文归档

本仓库保存 SmallArmsBigHeart 有容乃大的现有文章原文、来源索引和离线阅读文件。**尚未全量补齐。**

## 2026 年 10 月 3 日复检

[查看复检报告与 8 个图文样本](docs/audits/2026-10-03/README.md)。确认当前归档不完整：图片文字尚未 OCR，封面未单独归档，4 篇漏提了正文容器外的说明或转载信息；旧有缺失正文和媒体仍待补。补充文字已单独保存，原 Release 尚未重打包。下方 3,947 个图片文件的校验范围仅为已提取到的正文图片清单，不包括所有封面与背景图片。

## 当前内容

- 已知文章目录：1,270 篇。
- 已恢复正文：1,257 篇。
- 已知原图链接：3,947 个，对应 7,795 次文章内引用；全部下载并通过校验。
- 已有原始页面缓存：1,263 份，以压缩 HTML 保留，缓存可能包含错误页面，并不代表每份都有有效正文。
- 缺口：7 篇无正文缓存、3 篇缓存无有效正文、3 篇图文仅部分恢复。
- 49 篇含未离线保存的音视频或其他嵌入内容。
- 第 56、57 期及 2026 年 9 月 7 日后的文章范围尚未核齐。

## 下载和阅读

在 [Releases](https://github.com/wrenwrenwren79-bit/yourong-article-archive/releases/tag/archive-2026-10-02) 下载：

- `yourong-offline-reader-2026-10-02.zip`：正文、图片、索引和校验结果。解压后打开 `index.html`，即可离线阅读。
- `yourong-raw-html-2026-10-02.zip`：原始 HTML 缓存，解压得到 `raw/`，其中每份页面使用 gzip 压缩。
- `SHA256SUMS.txt`：两个压缩包的 SHA-256 校验值。

Git 仓库中保留正文和索引；图片及原始缓存放在 Release，避免每次克隆下载全部二进制文件。若要在克隆目录中显示图片，把阅读包解压到仓库根目录即可。

```sh
gh release download archive-2026-10-02 --repo wrenwrenwren79-bit/yourong-article-archive --pattern 'yourong-offline-reader-2026-10-02.zip'
unzip -o yourong-offline-reader-2026-10-02.zip
python3 tools/verify_archive.py
```

## 数据库与知识库方案

[精细提取与知识库数据库方案](docs/YOURONG_ARTICLE_KNOWLEDGE_INGESTION_DESIGN.md) 定义原文分块、字段字典、知识单元、文章版本、证据引用、审核及分阶段入库流程，并包含 RAG 混合检索、带引用问答、索引更新和验收方案。方案中的现有代码路径指 SIP&DRINK 应用仓库；本归档仓库仅保存方案与来源样例。

[提取样例](docs/yourong-ingestion-examples.json) 包含 3 篇原文的 11 条候选断言、16 个已校验原文锚点，以及 1 个派生值示例。`archiveRelativePath` 相对于本仓库根目录，`projectArchivePath` 用于应用工作区。样例不是已写入数据库或已独立验证的事实。

## 文件说明

- `articles/`：每篇文章的 HTML 阅读页、TXT 正文和 JSON 元数据。
- `manifest.json`：文章级状态、来源及校验值。
- `image_manifest.json`：原图 URL、本地路径和校验值。
- `原文文字汇总.txt`：现有原文文字汇总。
- `待补原文.html`、`missing_or_partial.csv`：已知正文缺口。
- `embedded_media_pending.json`：待归档的嵌入媒体引用。
- `verification.json`：本次文件完整性检查结果。
- `incoming_originals/`：补充原文的约定放置目录。

文件校验通过只表示归档文件一致，不代表公众号全量覆盖或原文完整性已逐篇在线核实。文章和图片保留原始来源；内容版权归原作者。
