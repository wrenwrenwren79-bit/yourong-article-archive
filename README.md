# 有容乃大原文归档

本仓库保存 SmallArmsBigHeart 有容乃大的现有文章原文、来源索引和离线阅读文件。**尚未全量补齐。**

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
