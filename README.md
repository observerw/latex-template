# 基于 VSCode 的 LaTeX 写作模板库

## 更新

- 2025-06-23：
  - 增加了 `.devcontainer` 配置，现在你可以直接在 GitHub 上创建一个 Codespace，打开这个仓库，然后就可以在 Codespace 中使用 VSCode 进行 LaTeX 写作了。无需安装任何环境，更加开箱即用😋；详见[下方说明](#可选使用-github-codespace)；
  - 增加了 `.rules` 目录，用于存放各类 AI IDE 可能会用到的规则文件，比如 `.cursorrules` 等；
  - [自带了 IEEE Conference Proceedings 模板](https://www.ieee.org/conferences/publishing/templates)；

## 简介

使用 VSCode 进行 LaTeX 写作需要[配置一些环境](https://zhuanlan.zhihu.com/p/166523064)，此外还需要手动设置目录结构等，较为繁琐。针对这些问题，本模板提供了开箱即用的实现：

- 在 `.vscode` 中做好了必要的设置并推荐安装 `latex-workshop` 等若干插件，一旦插件安装完成，即可无痛编译 `.tex` 文档；
- 预先设置好了目录结构，将文档中的各类内容归类放置到对应目录即可；
- 提供了一些[方便的脚本](#内容导出)，用于在写作完成后对文档进行处理，从而便于进行提交；

## ⚠️ （重要）环境安装

在编译文档前请先正确安装 TeX 环境。

按照 [`TinyTeX`](https://yihui.org/tinytex/#installation) 的文档安装即可。安装 `TinyTeX` 会比完整安装 TexLive 的体积小很多，因此十分推荐。

安装完后，若编译 LaTeX 文件时提示缺少某些包，可以使用 `tlmgr install 包名` 安装。

你也可以使用 [GitHub Codespace](#可选使用-github-codespace) 来进行 LaTeX 写作，这样就不需要在本地安装任何环境了。

如果你希望能够使用 Docker 管理所有 LaTeX 相关的环境，可以参考 [该 Dockerfile](./.devcontainer/Dockerfile)，基于 `TinyTeX` 自己构建一个 Docker 镜像。LaTeX Workshop 插件为 Docker 环境[提供了不错的支持](https://github.com/James-Yu/latex-workshop/wiki/Install#using-docker)。

## 编译/预览

文章主体在 `main.tex` 文件中；各章内容分别在 `sections` 文件夹的对应文件中，如文章的引言部分就在 `sections/intro.tex`中；图片在 `figures` 文件夹中；算法、伪代码等在 `algorithms` 文件夹中。

打开 `main.tex` 文件，点击右上角的绿色箭头（或 `Ctrl + S` 保存）即可执行编译；点击绿色箭头旁边的图标可以预览。由于设置了文件保存时自动编译，所以一般情况下不需要手动按绿色箭头。

如果编译出错，点击弹窗中的 `Open compiler log` 按钮，在输入窗口中按 `Ctrl + F` **搜索 `LaTeX Error` 或者 `error` 之类的关键词**，快速定位到问题。

编辑器部分和预览部分可以双向定位：

- 在**编辑器中修改了某些内容并保存**后，预览部分将会自动定位到修改的内容；
- 在编辑器中将**光标置于某个位置**，**按快捷键：****`Ctrl + Alt + J`** **Ctrl + Alt + J**，预览部分将会自动跳转到光标所在处；
- 在**预览部分双击某个内容**，编辑器将会自动定位到对应的位置；

## 快捷输入

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

## 附件

图片全部放在 `figures` 目录下，引用的路径为 `figures/figure.pdf`。

- **最好使用 `pdf` 格式的图片**；
`svg` 图片虽然也是矢量的，但 LaTeX 对其的支持并不好；
其他图片格式通常不是矢量的，无法无损放大，因此可能会被认为是写作不规范；

引用图片可以使用 `Figure` 缩写，然后在 `label` 中输入图片的文件名，比如：

```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.5\textwidth]{figures/figure.pdf}
    \caption{Caption}
    \label{fig:figure}
\end{figure}
```

## 交叉引用

在每一个章节、图、表、公式、算法等地方都要设置一个 `label`，**`label`** **label** **最好遵循一定的命名规范**，比如图片使用 `fig:figure`，表格使用 `tab:table`，章节使用 `sec:section`，公式使用 `eq:equation`，算法使用 `algo:algorithm` 等。

引用时可以输入相应的缩写，然后在 `label` 中输入引用的 `label`，比如想要引用 `label` 为 `fig:figure` 的图片，可以使用 `Figure:Ref` 缩写，然后在 `label` 中输入 `fig:figure`。

## 文献引用

假设大家都会用 Zotero，尤其是 [Better BibTeX 插件](https://snailwish.com/291/)。

正确安装该插件后：

1. 为当前正在写作的项目单独创建一个 Zotero 分类；
2. 右键，导出分类，选择导出格式为 `Better BibTeX`，勾选保持更新，选择导出路径为当前项目的根目录；
3. 将导出名称修改为 `main.bib`（名称最好不要随便起，arXiv要求 `bib` 必须与 `tex`的名称保持一致），随后根目录下就会生成相应的 `bib` 文件了；

在 `main.tex` 中将 `\bibliography{}` 命令指向这个 `bib` 文件，比如：

```latex
\bibliography{main.bib}
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

## 内容导出

写作完成后将会有可能面临需要上传 LaTeX 源代码的场景（如提交到 arXiv），这时可以使用 `scripts/` 目录中提供的 `export` 脚本将 LaTeX 项目进行导出。

在项目根目录下运行：

```bash
./scripts/export
```

（虽然 `export`是一个 Python 脚本，但很神奇不需要 `python` 命令来运行，因为脚本中添加了 `shebang` 来指定解释器）

运行后将会在项目根目录下生成一个 `export` 目录，里面包含了导出的内容。

**该目录中所包含的内容由根目录下的 `.export` 文件指定**，比如：

```bash
algorithms/**/*.tex
main.tex
*.cls
```

其中每一条规则都是一个 `glob` 表达式，可以匹配多个文件，比如 `algorithms/**/*.tex` 将会匹配 `algorithms/algorithm1.tex`、`algorithms/subdir/algorithm2.tex` 等。请根据实际情况修改 `.export` 文件。

脚本还有几个可选参数：

````bash
usage: export [-h] [--single-file] [--ignore-comments] [--compress] [--export-dir EXPORT_DIR] [--main-file MAIN_FILE]

Export files based on .export configuration

options:
  -h, --help            show this help message and exit
  --single-file, -s     Export main.tex only
  --ignore-comments, -i
                        Remove comments from exported .tex files
  --compress, -c        Compress export directory
  --export-dir EXPORT_DIR, -d EXPORT_DIR
                        Custom name for the export directory
  --main-file MAIN_FILE, -m MAIN_FILE
                        Custom name for the main .tex file
````

- `--single-file` 参数将会只导出 `main.tex` 文件，其中的所有 `\input{}` 命令将会被递归替换为对应的内容；随后，这些已经被替换的内容将不会被导出；
- `--ignore-comments` 参数将会在导出的 `.tex` 文件中删除所有的注释；
- `--compress` 参数将会在导出后将导出的内容压缩为一个 `zip` 文件。

因此推荐使用如下命令进行导出：

```bash
./scripts/export -s -i -c
```

随后就可以把在根目录下生成的 `export.zip` 文件上传到 arXiv 或者其他地方了。

## 内容备份

- 为了防止内容丢失，写完一个部分之后 `git commit` 一下；
- 将仓库推送到一个私人的远程仓库或设置为 private 的 GitHub 仓库中；
- 或者使用一个单独的外接硬盘定期对仓库进行备份；

## TODO 标注

安装 `TODO tree` 插件，可以在左侧栏看到所有的 LaTeX 文件中的 TODO 。

## 拼写提示/检查

使用 `ltex` 实现拼写检查和单词提示。

- 写作过程中输入部分英文单词时会出现提示；
- 某些句子不符合语法规范时会有蓝色波浪线提示；

## Copilot

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

## 与 Overleaf 同步

万恶的资本主义 Overleaf 必须要充会员才能使用 Git 同步功能，在没有会员的情况下我们只能**手动将本地项目打包成压缩包，然后上传到 Overleaf 上**。

在本地项目根目录下运行：

```bash
./scripts/archive
```

运行后将会在根目录下生成一个 `archive.zip` 文件，然后在 Overleaf 上新建一个项目，选择上传压缩包，上传 `archive.zip` 文件即可。

上传成功后将会创建一个新的项目。后续如果在本地进行了修改，可以直接把修改后的文本复制粘贴到 Overleaf 上的对应文件中。当然如果你不嫌麻烦，可以每次都删掉旧项目，重新上传压缩包。

## （可选）使用 GitHub Codespace

如果你不想在本地安装任何环境，或你希望能够与他人进行实时协作，那可以考虑使用 [GitHub Codespace](https://github.com/features/codespaces)。本项目中提供了一个 `.devcontainer` 目录，其中包含了一个基础的 `Dockerfile` 文件，对应的 Docker 镜像中已经安装了 `TinyTeX-2` 环境（包含了所有 TexLive 的包），因此你可以直接在 Codespace 中使用 VSCode 进行 LaTeX 写作。

## （可选）使用 Agent 规则文件

⚠️ 声明：不要让 Agent 帮你凭空生成论文！这样的行为通常会被认为是学术不端行为，甚至可能导致论文被拒稿或撤稿。推荐的使用场景为，你写好了论文的主体内容，想要让 Agent 帮你润色、校对、翻译等。

使用规则文件对 Agent 行为进行规范目前已经是一个常见的实践，各类 AI IDE 都开始支持这种功能，包括 [Cursor](https://docs.cursor.com/context/rules) 等。因此，如果你想要让 Agent 在帮你写作时遵循某些特定的规则，建议在 `.rules` 目录下编辑相应的规则文件。

一个常见的需求是让 Agent 在帮你写作的时候保证用词和语气的一致性。为此，推荐对 [`WRITING.md`](./.rules/WRITING.md) 文件进行编辑，更新其中的翻译术语表以及写作规范内容。
