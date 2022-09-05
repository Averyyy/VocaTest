# VOCATEST

- GRE 单词背不下来？ 好不容易背下来了又忘了？ 本脚本采用简单重复的理念，随机挑选同义单词，第一次确认你是否记得，第二次确认你记得的意思是不是真正的意思。根据每次的选择每个单词的权重（weight）会保存进 weight.json。
- 采用邹中杰老师的 GRE 词汇意群，把众多词记进同一个中文释义，减少记忆负担

## Prerequites

Code is intended to work with `Python 3.6.x` or later versions

### [gtts/pyttsx3]

假如你需要发音功能，你需要：

#### 在线版（使用 google gtts）

```
pip3 install gtts
```

#### 离线版（使用 pyttsx）

```
pip3 install pyttsx3
```

## 优缺点

😄 熟手快速过单词
😄 重复单词容易记忆
😄 自定义程度比较高 （高情商

😅 二十分钟写的简陋程序 （低情商
😅 pronunciation 功能（optional）无 async 处理会阻塞
😅 命令行小黑框框没有 GUI

## 如何使用？

### 1. 设置 voca.json， 每次单词个数

- 目前 repo 里的 voca.json 是我的生词本，假如你需要自定义，你可以参考我的数据结构重写一个生词本，在 main.py 里的 glossary 自定义文件名即可。
- num_iter 是每次循环的次数，循环结束后权重会保存

### 2. 运行脚本

在 terminal 中打开当前目录，输入

```
python main.py
```

则可以运行

### 3. 说明

第一次输入代表你能否认识这个单词，认识则按 j， 不认识则按 k （可自定义）此时：

- 第一次认识： 显示单词释义，此释义是否和你脑中的一致，假如一致按 j， 否则按 k
- 第一次不认识: 直接显示释义，进入下一个单词

Enjoy！

## Future improvements （假如有人要的话

- 用 pygame 整个 GUI 出来
- 解决 async pronunciation

## License

This project is licensed under the GPL v3 License - see the [LICENSE.md](LICENSE.md) file for details
