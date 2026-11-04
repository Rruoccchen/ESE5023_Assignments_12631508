# ESE5023_Assignments_12631508

Comments on HW2 from Yali （93/100）

下次作业请尽量写成一个.ipynb 文件，另外请运行代码，jupyter会自动保存运行结果（.pdf只写处理思路即可）。谢谢！

1.1 ["Deaths"]分组不对，应考虑按["Total Deaths"]分组 （-1p)

1.3 数据有多个震级类型 "Ms", "Mw", "Mag", "Mb", "Ml", "Mfa" ，
Ms在巨震时会饱和，采用Ms优先漏掉了最大地震 Japan 2011 本州（Mw 9.1）
先用 Mw/Mag 更好。另外，你没有考虑Ms缺失时如何处理。（-3p）

3.3  `BASIN` 的取值里有`NA` （North Atlantic），pandas 默认把`NA` 当缺失值,你没有统计NA的数据。（-3p）