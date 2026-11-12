# PDF批次清单工具

在技能根目录用 Python 3.11+ 执行 `scripts/pdf_batch_manifest.py`，依赖 PyMuPDF。仅在缺依赖且确有需要时按环境约束配置，不自动更改全局设置。

```powershell
python scripts/pdf_batch_manifest.py "D:\明确提供的论文目录" --output "D:\本次输出\manifest.json"
```

接受多个明确目录/PDF；默认只读目录直接文件。用户要求递归时才加 `--recursive`。输出JSON与CSV记录绝对来源、SHA、大小、重复关系、页数、损坏/加密阻塞。输出存在时退出，避免覆盖。只盘点，不代表提取或审读完成。

不扫描未指定目录，不修改源文件。后续状态按证据推进：DISCOVERED → EXTRACTED → SINGLE_ANALYZED → SINGLE_QC_PASSED → FROZEN → SYNTHESIZED。
