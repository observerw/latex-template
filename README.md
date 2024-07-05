# 环境安装

按照 [tinytex](https://yihui.org/tinytex/#installation) 的文档安装即可。安装 tinytex 会比完整安装 TexLive 的体积小很多，因此十分推荐。

安装完后，若编译 LaTeX 文件时提示缺少某些包，可以使用 `tlmgr install 包名` 安装。

安装完毕后可以在命令行中运行：

```bash
make check
```

检查所需的包是否都已安装。

# 编译/预览

文章主体在 `main.tex` 文件中；各章内容分别在 `sections` 文件夹的对应文件中，比如文章的 Introduction 就在 `sections/intro.tex`中；图片在 `figures` 文件夹中；算法、伪代码等内容可放在 `algorithms` 文件夹中。

打开 `main.tex` 文件，点击右上角的绿色箭头执行编译；点击绿色箭头旁边的图标可以预览。由于设置了文件保存时自动编译，所以一般情况下不需要手动按绿色箭头。

如果编译出错，点击弹窗中的 `Open compiler log` 按钮，在输入窗口中按 `Ctrl + F` 搜索 `LaTeX Error` 或者 `error` 之类的关键词，快速定位到问题。

编辑器部分和预览部分可以双向定位：

- 在**编辑器中修改了某些内容并保存**后，预览部分将会自动定位到修改的内容；
- 在编辑器中将**光标置于某个位置**，**按快捷键：`Ctrl + Alt + J`**，预览部分将会自动跳转到光标所在处；
- 在**预览部分双击某个内容**，编辑器将会自动定位到对应的位置；

# 快捷输入

`LaTeX Snippets` 插件提供了一些常见的缩写：

| 缩写                       | 对应内容                                     |
| -------------------------- | -------------------------------------------- |
| `Align(ed)`                | Align(ed).                                   |
| `Cases`                    | Cases.                                       |
| `Chapter`                  | Chapter.                                     |
| `Description`              | Description.                                 |
| `Math`                     | Add a Math.                                  |
| `DisplayMath`              | Display Math.                                |
| `Equation`                 | Add an Equation.                             |
| `Display Math — \\[ … \\]` | Display Math.                                |
| `Theorem`                  | Add a theorem.                               |
| `Definition`               | Add a definition.                            |
| `Proof`                    | Add a proof.                                 |
| `Algorithm`                | Add an algorithm.                            |
| `Algorithm:State`          | Add a statement of algorithm.                |
| `Algorithm:If`             | Add an if statement of algorithm.            |
| `Algorithm:For`            | Add a for statement of algorithm.            |
| `Algorithm:While`          | Add a for statement of algorithm.            |
| `Algorithm:Ref`            | Ref for Algorithm.                           |
| `Figure:Ref`               | Ref for Figure.                              |
| `Gather(ed)`               | Gather(ed).                                  |
| `Itemize`                  | Itemize.                                     |
| `Listing:Ref`              | Listing.                                     |
| `Matrix`                   | Matrix.                                      |
| `Page`                     | Page.                                        |
| `Paragraph`                | Paragraph.                                   |
| `Part`                     | Part.                                        |
| `Region Start`             | Folding Region Start.                        |
| `Region End`               | Folding Region End.                          |
| `Section:Ref`              | Section Reference.                           |
| `Split`                    | Section.                                     |
| `Sub Paragraph`            | Sub Paragraph.                               |
| `Sub Section`              | Sub Section.                                 |
| `Sub Sub Section`          | Sub Sub Section.                             |
| `Table:Ref`                | Table Reference.                             |
| `Tabular`                  | Tabular.                                     |
| `\\begin{}…\\end{}`        | Begin - End.                                 |
| `Figure`                   | Add a figure.                                |
| `Figure:ACM`               | Add a figure (ACM).                          |
| `Figure:ACM:*`             | Add a figure (ACM).                          |
| `Table`                    | Add a table.                                 |
| `Table:ACM`                | Add a table (ACM).                           |
| `Table:ACM:*`              | Add a table (ACM).                           |
| `Enumerate`                | Add an enumerate.                            |
| `Compactitem`              | Add a compactitem (from package `paralist`). |
| `Cite`                     | Add a cite.                                  |
| `EmptyPage`                | Add an empty page.                           |


在编辑器中输入这些缩写，按回车，将会展开为对应的 LaTeX 代码。具体每个缩写对应的内容可以自己输入试试。

# 附件

图片全部放在 `figures` 目录下，引用的路径为 `figures/figure.pdf`。最好使用 `pdf` 格式的图片。

引用图片可以使用 `Figure` 缩写，然后在 `label` 中输入图片的文件名，比如：

```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.5\textwidth]{figures/figure.pdf}
    \caption{Caption}
    \label{fig:figure}
\end{figure}
```

# 交叉引用

在每一个章节、图、表、公式、算法等地方都要设置一个 `label`，**`label` 最好遵循一定的命名规范**，比如图片使用 `fig:figure`，表格使用 `tab:table`，章节使用 `sec:section`，公式使用 `eq:equation`，算法使用 `algo:algorithm` 等。

引用时可以输入相应的缩写，然后在 `label` 中输入引用的 `label`，比如想要引用 `label` 为 `fig:figure` 的图片，可以使用 `Figure:Ref` 缩写，然后在 `label` 中输入 `fig:figure`。

# 文献引用

假设大家都会用 Zotero。

给 Zotero 安装一个名为 `Zotero Better BibTeX` 的插件，为当前正在写作的项目单独创建一个 Zotero 文件夹，右键，导出分类，选择导出格式为 `Better BibTeX`，勾选保持更新，选择导出路径为当前项目的根目录，随后根目录下就会生成一个 `*.bib` 文件。

在 `main.tex` 中将 `\bibliography{}` 命令指向这个 `*.bib` 文件，比如：

```latex
\bibliography{references.bib}
```

这样就可以自动生成参考文献列表了。

`LaTeX Utilities` 提供了一个从 Zotero 中导入文件的命令，但 Zotero 自带的文献导入框太丑了🤣，不如用如下介绍的方法。

首先设置 `Ctrl + Alt + Z` 作为打开文献搜索面板的快捷键。打开命令面板，搜索 `首选项：打开键盘快捷方式(JSON)`，打开 `keybindings.json` 文件，在数组末尾添加如下内容：

```json
{
    "key": "alt+ctrl+z",
    "command": "latex-workshop.citation"
}
```

设置完毕后，一个完整的文献引用流程将会是：

1. 在需要引用文献的内容后输入空格 + `Cite`，回车，此时内容为 `一些内容 ~\cite{|}`；
2. 按下 `alt+ctrl+z`，弹出文献搜索框，输入关键词，选择文献，此时内容为 `一些内容 ~\cite{citekey}`，完成引用；
3. 如果需要在同一个位置引用多篇文献，则在前一个 `citekey` 后输入逗号，重复第 2 步即可，此时内容为 `一些内容 ~\cite{citekey1,citekey2}`。

# 内容导出

有的会议要求所有的 LaTeX 内容必须写在一个文件中，不能使用 `\input{}` 命令来分别导入各章节，因此当写作完成后有可能还需要将所有的内容导出到一个文件中。

对于 Unix 系统，在控制台中运行：

```bash
make export
```

在 Windows 下没有安装 `make` 的话，可以在根目录下打开控制台，运行：

```bash
python scripts/replace-input.py -b %cd% -i main.tex -o export.tex
```

运行后将会在根目录下生成一个 `export.tex` 文件。

为了保证生成内容无误，最好在生成之后将其编译一遍，检查是否可以正常编译。

# 内容备份

为了防止内容丢失，写完一个部分之后 `git commit` 一下；将仓库推送到一个私人的远程仓库或设置为 private 的 GitHub 仓库中；或者使用一个单独的外接硬盘定期对仓库进行备份。

# TODO

安装 `TODO tree` 插件，可以在左侧栏看到所有的 LaTeX 文件中的 TODO 。

# 拼写提示/检查

使用 `ltex` 实现拼写检查和单词提示。

- 写作过程中输入部分英文单词时会出现提示；
- 某些句子不符合语法规范时会有蓝色波浪线提示；

# Copilot

[GitHub Copilot](https://github.com/features/copilot)

有两种用法：

- 编写内容时让它续写，提供写作思路，但一般给的思路都不太靠谱；
- 写完中文稿后，在下一行输入一些单词给他起个头，让他将中文稿翻译为英文稿；

可以把每一段的中文稿写在注释里，让 Copilot 翻译，比如：

```latex
% 钵钵鸡是一种传统的川菜，属于川菜中的冷菜。钵钵鸡的主要原料是鸡肉，口感鲜美，麻辣鲜香，是川菜中的一道经典菜品。

Braised chicken in chili sauce is a traditional Sichuan dish, which belongs to the cold dish of Sichuan cuisine. The main ingredient of braised chicken in chili sauce is chicken, which has a fresh and delicious taste, and is a classic dish in Sichuan cuisine.

% 钵钵鸡的制作方法主要有两种，一种是将鸡肉切成块状，用沸水焯水，再用冷水浸泡，最后加入调料拌匀即可。另一种是将鸡肉切成丝状，用沸水焯水，再用冷水浸泡，最后加入调料拌匀即可。

There are mainly two ways to make braised chicken in chili sauce. One is to cut the chicken into pieces, blanch it in boiling water, soak it in cold water, and finally add seasoning and mix well. The other is to cut the chicken into shreds, blanch it in boiling water, soak it in cold water, and finally add seasoning and mix well.
```

当然 Copilot 的学术写作能力还是有限的，翻译得到的英文稿只能作为参考，还需要专门的校对和润色。

当 Copilot 出现提示时：

- 按 `Tab` 接收全部提示；
- 按 `Ctrl + ->` 可以只接受一个单词的提示；
- 只接受一行的提示没有默认快捷键，非常建议在 `keybindings.json` 文件中添加 `Ctrl + Shift + ->` 作为快捷键：

```json
{
    "key": "shift+ctrl+right",
    "command": "editor.action.inlineSuggest.acceptNextLine"
}
```

众所周知 Copilot 写作的时候需要足够的上下文，因此如果写当前内容需要其他部分提供的上下文（比如写 Method 的时候可能需要 Intro 中提到的内容），可以把内容复制到当前文件并全部注释掉。