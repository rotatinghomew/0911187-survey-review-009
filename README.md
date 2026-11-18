# 科研训练量表审阅

项目分析不同学期的训练问卷版本、学生答卷和阶段记录。问卷题目以 `item` 表示并带版本号；答卷按 `response` 记录，`withdrawn` 或无效答卷不参与均值。跨版本映射只有状态为 `confirmed` 时才会出现在确认映射列表中。

每个版本的题目仍分别报告，不因文字相似就视为同一测量。阶段记录用于解释样本构成。当前报告按输入的题目、答卷和映射计算，尚未追踪量表负责人修订映射后哪些历史 cohort 需要重新评估，也未封存旧总结口径。

需要 Python 3.11 或更新版本，不依赖外部服务。运行 `PYTHONPATH=src python -m unittest discover -s tests -v` 执行测试。`survey_review.facts` 校验输入，`survey_review.comparability.confirmed_mappings` 只选取负责人确认的题目对应，`survey_review.analysis.summarize` 计算版本内覆盖与阶段样本，`survey_review.reports.build_report` 生成修订报告。样例见 `examples/sample.json`。
